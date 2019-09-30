"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this views module we created rest_api for user login ,register,forgot_password
author:  Sachin Shrikant Jadhav
since :  25-09-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
import json
import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from rest_framework import status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, EmailSerializer, PasswordSerializer
from django.shortcuts import render
from utils import Jwt_Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.validators import validate_email
import re
from bitly_api import Connection
from utils import ee
import logging

logger = logging.getLogger(__name__)


class User_Create(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """

        :param request: here we get post request
        :return:in this function we take user input for registration and sent mail to email id

        """

        try:
            smd = {'success': False,
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
                    message1 = 'http://' + get_current_site(request).domain + '/' + 'activate' + '/' + Tokan
                    API_USER = settings.API_USER
                    API_KEY = settings.API_KEY
                    bitly = Connection(API_USER, API_KEY)
                    response = bitly.shorten(message1)
                    url = response["url"]
                    message = render_to_string('login/token.html', {
                        'name': user.username,
                        'url': url
                    })
                    recipient_list = [self.request.data['email'], ]
                    smd['success'] = True
                    smd['Message'] = 'you registered successfully for activate your account please check your email'
                    ee.emit("myevent", message, recipient_list)
                    return Response(smd)
                return Response(smd)
            logger.warning('something was wrong')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            logger.warning('something was wrong')
            return Response(status.HTTP_417_EXPECTATION_FAILED)


def activate(request, id, *args, **kwargs):
    """

        :param request: here we use get request
        :param id:in this id we gate token
        :return:in this function we get tokan when user click the link and we decode the token and
                activate the user
        """
    smd = {'success': False,
           'Message': 'account activation failed',
           'Data': []}
    try:
        decodedPayload = jwt.decode(id, "SECRET_KEY")
        username = decodedPayload["username"]
        email = decodedPayload["email"]
        user = User.objects.get(username=username, email=email)
        if user:
            user.is_active = True
            user.save()
            smd['success'] = True
            smd['Message'] = 'account activated successfully'
            return HttpResponse(json.dumps(smd))
        else:
            return HttpResponse(json.dumps(smd))
    except Exception:
        return HttpResponse(json.dumps(smd))


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


class Reset_Passward(GenericAPIView):
    serializer_class = EmailSerializer

    def post(self, request, *args, **kwargs):
        """

        :param request: here is post request por set password
        :return: in this function we take email from user and send toaken for verification
        """
        try:
            smd = {'success': False,
                   'Message': 'please enter valid email address',
                   'Data': []}
            email = request.data['email']
            user = User.objects.get(email=email)
            if user:
                payload = {
                    'username': user.username,
                    'email': user.email,
                }
                jwt_token = Jwt_Token(payload)
                Tokan = jwt_token['token']
                message1 = 'http://' + get_current_site(request).domain + '/' + 'reset_password' + '/' + Tokan
                API_USER = settings.API_USER
                API_KEY = settings.API_KEY
                bitly = Connection(API_USER, API_KEY)
                response = bitly.shorten(message1)
                short_url = response["url"]
                message = render_to_string('login/reset_token.html', {
                    'name': user.username,
                    'url': short_url
                })
                recipient_list = [user.email, ]
                ee.emit("myevent2", message, recipient_list)
                smd['success'] = True
                smd['Message'] = 'your email is validated for reset password check email'
                return Response(smd)
            else:
                return Response(smd)
        except Exception:
            return Response(smd)


def reset_password(request, id):
    """

    :param request: request for reset password
    :param id: here we token for decoding
    :return:this function used for reset password

    """
    smd = {'success': False,
           'Message': 'you are not valid user',
           'Data': []}
    try:
        # here decode is done with jwt
        decode = jwt.decode(id, "SECRET_KEY")
        username = decode['username']
        user = User.objects.get(username=username)

        # if user is not none then we will fetch the data and redirect to the reset password page
        if user is not None:

            return redirect('http://localhost:8000/resetpassword/' + str(user))
        else:
            return Response(smd)
    except KeyError:
        smd['Message'] = 'something was wrong try again'
        return Response(smd)
    except Exception:
        return Response(smd)


class Resetpassword(GenericAPIView):
    serializer_class = PasswordSerializer

    def get(self, request, userReset, *args, **kwargs):
        global username
        """
          :param request:  user will request for resetting password
          :param userReset: username is fetched
          :return: will change the password
          """
        smd = {'success': False,
               'Message': 'you are not valid user',
               'Data': []}
        try:
            user = User.objects.get(username=userReset)
            if user:
                username = user.username
                smd['success'] = True
                smd['Message'] = 'successful'
                return Response(smd)
            return Response(smd)
        except Exception:
            smd['Message'] = 'insufficient credential'
            Response(smd)

    def post(self, request, *args, **kwargs):
        smd = {'success': False,
               'Message': 'please enter valid password',
               'Data': []}
        try:
            password = request.data['password']
            confirm_password = request.data['confirm_password']
            # here we will save the user password in the database
            if password == "" or confirm_password == "":
                return Response(smd)
            elif password != confirm_password:
                smd['Message'] = 'password not match'
                return Response(smd)
            else:
                user = User.objects.get(username=username)
                user.set_password(password)
                # here we will save the user password in the database
                user.save()
                smd['success'] = True
                smd['Message'] = 'password changed successfully'
                return Response(smd)
        except Exception:
            smd['Message'] = 'something was wrong try again'
            return Response(smd)


class HelloView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print(request.user)
        print(request.META['HTTP_AUTHORIZATION'])
        content = {'message': 'Hello, World!'}
        return Response(content)
