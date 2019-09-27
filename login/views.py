from django.contrib import messages
from django.shortcuts import redirect
import json
import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.shortcuts import render
from utils import Jwt_Token
from rest_framework.permissions import IsAuthenticated, AllowAny


class User_Create(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """

        :param request: here we get post request
        :return:in this function we take user input for registration and sent mail to email id

        """
        try:
            response = {'success': False,
                        'Message': 'please register again',
                        'Data': []}
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                user.is_active = False
                user.save()

                if user:
                    payload = {
                        'username': self.request.data['username'],
                        'email': self.request.data['email'],
                    }
                    token = Jwt_Token(payload)
                    Tokan = token['token']
                    # subject = 'Thank you for registering to our site'
                    # email_from = settings.EMAIL_HOST_USER
                    # message = 'please click below link for activate your account'
                    # recipient_list = [self.request.data['email'], ]
                    response['success'] = True
                    response['Message'] = 'you registered succesfully for activate your account please check your email'
                    response['Data'] = Tokan
                    # send_mail(subject, message + '\n' "http://localhost:8000/activate/" + Tokan, email_from,
                    #           recipient_list)
                    return Response(response)
                return Response(response)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status.HTTP_417_EXPECTATION_FAILED)


class Active_user(APIView):

    def get(self, request, id, *args, **kwargs):
        """

        :param request: here we use get request
        :param id:in this id we gate token
        :return:in this function we get tokan when user click the link and we decode the token and
                activate the user
        """
        try:
            decodedPayload = jwt.decode(id, "SECRET_KEY")
            username = decodedPayload["username"]
            email = decodedPayload["email"]
            user = User.objects.get(username=username, email=email)
            if user:
                user.is_active = True
                user.save()

                return HttpResponseRedirect(redirect_to="http://localhost:8000/loginpage/")
            else:
                return HttpResponseRedirect(redirect_to="http://localhost:8000/register/")
        except Exception:
            messages.info(request, "activation failed")
            return HttpResponseRedirect(redirect_to="http://localhost:8000/register/")


class Login(APIView):

    def post(self, request, *args, **kwargs):
        """

        :param request: here we get post request
        :return:this is login api view for user login after login its generate the token

        """
        try:
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user:
                payload = {
                    'username': user.username,
                    'email': user.email,
                }
                jwt_token = {'token': jwt.encode(payload, "SECRET_KEY", algorithm="HS256").decode('utf-8')}
                Tokan = jwt_token['token']
                response = json.dumps({"success": True, "message": "successful", "data": Tokan})

            messages.info(request, "credential not authorized")
            return redirect('loginpage')
        except Exception:
            return redirect('loginpage')


class Reset_Passward(APIView):

    def post(self, request, *args, **kwargs):
        """

        :param request: here is post request por set password
        :return: in this function we take email from user and send toaken for verification
        """
        try:
            email = request.POST["email"]
            print(email)
            user = User.objects.get(email=email)
            print(user, '...........')
            if user:
                payload = {
                    'username': user.username,
                    'email': user.email,
                }
                jwt_token = {'token': jwt.encode(payload, "SECRET_KEY", algorithm="HS256").decode('utf-8')}
                Tokan = jwt_token['token']
                subject = 'reset password'
                message = 'please click below link for activate your account'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail(subject, message + " \n " + "http://localhost:8000/reset_password/" + Tokan, email_from,
                          recipient_list)
                return Response("please check you're email")
            else:
                return Response("you are not valid user")
        except Exception:
            return redirect('Reset_Passward')


def reset_password(request, id):
    """

    :param request: request for reset password
    :param id: here we token for decoding
    :return:this function used for reset password
    """
    try:
        # here decode is done with jwt
        decode = jwt.decode(id, "SECRET_KEY")
        username = decode['username']
        user = User.objects.get(username=username)

        # if user is not none then we will fetch the data and redirect to the reset password page
        if user is not None:

            return redirect('http://localhost:8000/resetpassword/' + str(user))
        else:
            messages.info(request, 'was not able to sent the email')
            return redirect('reset_password')
    except KeyError:
        messages.info(request, 'was not able to sent the email')
        return redirect('reset_password')
    except Exception:
        messages.info(request, 'activation link expired')
        return redirect('reset_password')


def resetpassword(request, userReset):
    """
    :param request:  user will request for resetting password
    :param userReset: username is fetched
    :return: will chnage the password
    """
    try:
        if request.method == 'POST':
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            # password validation is done in this form
            if password == "" or confirm_password == "":
                messages.info(request, "please check the re entered password again")
                return redirect('http://localhost:8000/resetpassword/' + str(userReset))

            elif password != confirm_password:
                messages.info(request, "please check the re entered password again")
                return redirect('http://localhost:8000/resetpassword/' + str(userReset))

            else:
                user = User.objects.get(username=userReset)
                user.set_password(password)
                # here we will save the user password in the database
                user.save()
                messages.info(request, "password reset done")
                return redirect('http://localhost:8000/loginpage/')
        else:
            return render(request, 'login/set_password.html')
    except Exception:
        return redirect('http://localhost:8000/resetpassword/' + str(userReset))


def logout(request):
    """

    :return: here is logout function redirect to loginpage

    """
    return HttpResponseRedirect(redirect_to="http://localhost:8000/loginpage/")


class HelloView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
