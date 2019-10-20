"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this views module we created rest_api for user users ,register,forgot_password
author:  Sachin Shrikant Jadhav
since :  25-09-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
from Fundoo.settings import s3
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
import json
import jwt
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from jwt import DecodeError
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from Lib import redis
from users.decoraters import login_required
# from users.models import Profile
from users.models import Profile
from .serializers import UserSerializer, EmailSerializer, PasswordSerializer, LoginSerializer, ImageSerializer
from Lib.pyjwt_token import Jwt
from rest_framework.permissions import IsAuthenticated, AllowAny
from Lib.event_emmiter import email_event
from Lib.amazons3 import AmazonS3
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
                    token = Jwt().register_token(payload)
                    long_url = 'activate' + '/' + token
                    short_url = get_short_url(long_url)  # Url object
                    message = render_to_string('users/token.html', {
                        'name': user.username,
                        'domain': get_current_site(request).domain,
                        'url': short_url.short_id
                    })
                    recipient_list = [self.request.data['email'], ]
                    response = Smd_Response(True, 'you registered successfully for activate your account please check '
                                                  'your email', [])
                    email_event.emit("account_activate_event", message, recipient_list)
                    return HttpResponse(json.dumps(response))
                response = Smd_Response(False, 'you are not validated try again', [])
                return response
            logger.warning('not valid input warning from users.views.register_api')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            logger.warning('something was wrong warning from users.views.register_api')
            smd = Smd_Response()
        return smd


class Login(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """

        :param request: here we get post request
        :return:this is users api view for user users after users its generate the token

        """
        try:
            username = request.data["username"]
            password = request.data["password"]
            if username == "" and password == "":
                raise KeyError
            if username == "":
                raise KeyError
            if password == "":
                raise KeyError
            user = authenticate(username=username, password=password)
            if user:
                payload = {
                    'username': username,
                    'password': password,
                }
                token = Jwt().login_token(payload)
                redis.Set(username, token)
                smd = {"success": True, "message": "successful", "data": token}
                return HttpResponse(json.dumps(smd))
            else:
                logger.warning('not valid user warning from users.views.login_api')
                smd = Smd_Response(False, 'please provide valid credentials', [])
        except KeyError:
            logger.warning('any one input field is blank warning from users.views.login_api')
            smd = Smd_Response(False, 'one of above field may not be blank', [])
        except Exception:
            logger.warning('something is wrong warning from users.views.login_api')
            smd = Smd_Response()
        return smd


def activate(request, short_id, *args, **kwargs):
    """
    :param request: here we use get request
    :param short_id:in this id we gate token
    :return:in this function we get tokan when user click the link and we decode the token and
            activate the user
    """
    smd = {'success': False,
           'Message': 'account activation failed',
           'Data': []}
    try:
        url = Url.objects.get(short_id=short_id)
        if url is None:
            raise KeyError

        token = url.url.split('/')

        try:
            decodedPayload = jwt.decode(token[1], "SECRET_KEY")
        except DecodeError:
            return HttpResponse(json.dumps(smd))

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
    except ObjectDoesNotExist:
        HttpResponse(json.dumps(smd))
    except KeyError:
        HttpResponse(json.dumps(smd))
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
                token = Jwt().register_token(payload)
                long_url = 'reset_password' + '/' + token
                short_url = get_short_url(long_url)  # Url object
                message = render_to_string('users/reset_token.html', {
                    'name': user.username,
                    'domain': get_current_site(request).domain,
                    'url': short_url.short_id
                })
                recipient_list = [user.email, ]
                email_event.emit("reset_password_event", message, recipient_list)
                smd = Smd_Response(True, 'you"re email is verified for reset password check you"re mail', [])
                return smd
            else:
                smd = Smd_Response(False, 'you are not valid user register first', [])
                logger.warning('not valid user warning from users.views.Reset_password_api')
        except ObjectDoesNotExist:
            smd = Smd_Response(False, 'this email id not registered', [])
            logger.warning('email not registered warning from users.views.Reset_password_api')
        except ValueError:
            smd = Smd_Response(False, 'please provide valid email address', [])
            logger.warning('not valid email address warning from users.views.Reset_password_api')
        except KeyError:
            smd = Smd_Response(False, 'above field not be blank', [])
            logger.warning('input is blank warning from users.views.Reset_password_api')
        except Exception:
            logger.warning('something is wrong warning from users.views.Reset_password_api')
            smd = Smd_Response()
        return smd


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
        try:
            url = Url.objects.get(short_id=id)
            token = url.url.split('/')
            decode = jwt.decode(token[1], "SECRET_KEY")
        except DecodeError:
            smd['Message'] = 'token is invalid'
            return Response(smd)
        username = decode['username']
        user = User.objects.get(username=username)

        # if user is not none then we will redirect to the reset password page
        if user is not None:

            return redirect('http://localhost:8000/resetpassword/' + str(user))
        else:
            return Response(smd)
    except ObjectDoesNotExist:
        smd['Message'] = 'please provide valid credential'
        return Response(smd)
    except Exception:
        smd['Message'] = 'something was wrong try again'
        return Response(smd)


class Resetpassword(GenericAPIView):
    serializer_class = PasswordSerializer

    def post(self, request, userReset, *args, **kwargs):

        smd = {'success': False,
               'Message': 'please enter valid password',
               'Data': []}
        try:
            user = User.objects.get(username=userReset)
            username = user.username
            password = request.data['password']
            confirm_password = request.data['confirm_password']
            # here we will save the user password in the database
            if password == "" or confirm_password == "":
                raise KeyError
            if password == "":
                raise KeyError
            if confirm_password == "":
                raise KeyError
            if password != confirm_password:
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

        except ObjectDoesNotExist:
            smd['Message'] = 'not valid credentials try again'
            return Response(smd)
        except KeyError:
            smd['Message'] = 'above field is may not be blank'
            return Response(smd)
        except Exception:
            smd['Message'] = 'something was wrong try again'
            return Response(smd)


@method_decorator(login_required, name='dispatch')
class HelloView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


@method_decorator(login_required, name='dispatch')
class Logout(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            header = request.META['HTTP_AUTHORIZATION']
            token = header.split(' ')
            decoded = jwt.decode(token[1], settings.SECRET_KEY, algorithm="HS256")
            user = User.objects.get(pk=decoded['user_id'])
            if user:
                redis.Del(user.username)
                smd = Smd_Response(True, 'safely logged out', [])
            else:
                smd = Smd_Response(True, 'you are not authorized user ', [])
        except ObjectDoesNotExist:
            smd = Smd_Response(False, 'not valid credentials', [])
        except Exception:
            smd = Smd_Response()
        return smd


class S3Upload(GenericAPIView):
    serializer_class = ImageSerializer

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """
        :param request: here we using post request for uploading photo
        :return: this function is used for upload a photo on amazon s3
        """
        try:
            serializer = ImageSerializer(data=request.data)
            if serializer.is_valid():
                image = request.data['image']
                user = request.user
                print(user.id)
                exist_image = Profile.objects.get(user_id=user.id)
                if exist_image:
                    url = AmazonS3().upload_file(image, object_name=user.username)
                    exist_image.image = url
                    exist_image.save()
                    smd = Smd_Response(True, 'image uploaded successfully')
                else:
                    url = AmazonS3().upload_file(image, object_name=user.username)
                    Profile.objects.create(image=url, user_id=user.id)
                    smd = Smd_Response(True, 'image uploaded successfully')
            else:
                smd = Smd_Response(False, 'please provide valid image', [])
                logger.warning('not a valid image warning from users.views.s3upload_api')
        except Exception:
            logger.warning('something is wrong warning from users.views.s3upload_api')
            smd = Smd_Response()
        return smd


def s3_read(request, bucket, object_name, *args, **kwargs):
    """

    :param bucket:here we taking bucket name from path parameter
    :param object_name: here we taking object name from parameter
    :return:this function is used for generate preassigned url for view photo

    """
    try:
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket,
                'Key': object_name
            }
        )
        print(url)
        return redirect(url)
    except Exception:
        smd = Smd_Response()
        return smd
