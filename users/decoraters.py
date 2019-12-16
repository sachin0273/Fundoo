import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from jwt import DecodeError
from rest_framework.response import Response
from Lib import redis_service
from utils import Smd_Response


def login_required(function):
    def wraper(request, *args, **kwargs):
        try:
            header = request.META['HTTP_AUTHORIZATION']
            token = header.split(' ')
            decoded = jwt.decode(token[1], settings.SECRET_KEY, algorithm="HS256")
            redis_token = redis_service.Get(decoded['user_id'])
            if redis_token is None:
                raise KeyError
            return function(request, *args, **kwargs)
        except DecodeError:
            smd = Smd_Response(message='invalid token redirected to users page')
        except KeyError:
            smd = Smd_Response(message='user_id is not inside redis')
        except Exception:
            smd = Smd_Response()
        return smd
    return wraper
