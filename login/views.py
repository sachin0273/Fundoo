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
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Services import redis
from login.decoraters import login_required
from .serializers import UserSerializer, EmailSerializer, PasswordSerializer
from Services.pyjwt_token import Jwt_Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from Services.bitly_api import Connection
from Services.event_emmiter import ee
import logging
from utils import validate_email
from urlshortening.models import get_short_url, invalidate_url, get_full_url, Url
from utils import Smd_Response

logger = logging.getLogger(__name__)


class User_Create(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        :purpose: in this function we register a new user via sending jwt token on email
        :param request: here we get post request
        :return:in this function we take user input for registration and sent mail to email id

        """

        try:
            smd = {'success': False,
                   'Message': 'something went wrong',
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
                    message1 = 'activate' + '/' + Tokan
                    short_url = get_short_url(message1)  # Url object
                    print(type(short_url.short_id))
                    print(short_url.short_id)  # id for short url
                    # API_USER = settings.API_USER
                    # API_KEY = settings.API_KEY
                    # bitly = Connection(API_USER, API_KEY)
                    # response = bitly.shorten(message1)s
                    # url = response["url"]
                    message = render_to_string('login/token.html', {
                        'name': user.username,
                        'domain': get_current_site(request).domain,
                        'url': short_url.short_id
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


def activate(request, short_id, *args, **kwargs):
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
        gh = Url.objects.get(short_id=short_id)
        ty = gh.url.split('/')
        print(ty[1])
        decodedPayload = jwt.decode(ty[1], "SECRET_KEY")
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


class Reset_Passward(GenericAPIView):
    serializer_class = EmailSerializer

    def post(self, request, *args, **kwargs):
        """
        :param request: here is post request por set password
        :return: in this function we take email from user and send toaken for verification
        """
        try:
            email = request.data['email']
            if email == "":
                raise KeyError
            if not validate_email(email):
                raise ValueError
            user = User.objects.get(email=email)
            if user:
                payload = {
                    'username': user.username,
                    'email': user.email,
                }
                jwt_token = Jwt_Token(payload)
                Tokan = jwt_token['token']
                message1 = 'reset_password' + '/' + Tokan
                # API_USER = settings.API_USER
                # API_KEY = settings.API_KEY
                # bitly = Connection(API_USER, API_KEY)
                # response = bitly.shorten(message1)
                short_url = get_short_url(message1)  # Url object
                print(short_url.short_id)  # id for short url
                print('http://' + str(short_url.short_id))

                # short_url = response["url"]
                message = render_to_string('login/reset_token.html', {
                    'name': user.username,
                    'url': short_url
                })
                recipient_list = [user.email, ]
                ee.emit("myevent2", message, recipient_list)
                smd = Smd_Response(True, 'you"re email is verified for reset password check you"re mail', [])

                return Response(smd)
            else:
                return Response('dfffd')
        except ValueError:
            return Response('dfhdhdhdhdhdhdhdhdhdhdhdhdh')
        except KeyError:
            return Response('=========================>')
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

    def post(self, request, userReset, *args, **kwargs):

        smd = {'success': False,
               'Message': 'please enter valid password',
               'Data': []}
        try:
            print(userReset)
            username = userReset
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


@method_decorator(login_required, name='dispatch')
class HelloView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
        print(request.user)
        print(request.META['HTTP_AUTHORIZATION'])
        content = {'message': 'Hello, World!'}
        return Response(content)


@method_decorator(login_required, name='dispatch')
class Logout(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        rty = request.META['HTTP_AUTHORIZATION']
        gh = rty.split(' ')
        decoded = jwt.decode(gh[1], settings.SECRET_KEY, algorithm="HS256")
        redis.Del(decoded['user_id'])
        content = {'message': 'safely logged out'}
        return Response(content)
#
# class S3Api(GenericAPIView):

