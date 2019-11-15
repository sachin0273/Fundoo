import jwt
import redis
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from jwt import DecodeError
from rest_framework.response import Response
from Lib import redis
from utils import Smd_Response


def login_required(function):
    def wraper(request, *args, **kwargs):
        try:
            header = request.META['HTTP_AUTHORIZATION']
            token = header.split(' ')
<<<<<<< HEAD
            try:
                decoded = jwt.decode(token[1], settings.SECRET_KEY, algorithm="HS256")
            except DecodeError:
                smd = Smd_Response(False, 'invalid token redirected to users page', [])
                return smd
=======
            decoded = jwt.decode(token[1], settings.SECRET_KEY, algorithm="HS256")
>>>>>>> c5a1d28d... editing done with middlleware
            redis_token = redis.Get(decoded['user_id'])
            try:
                jwt.decode(redis_token, settings.SECRET_KEY, algorithm="HS256")
            except DecodeError:
                smd = Smd_Response(False, 'invalid user redirected to users page', [])
                return smd
            return function(request, *args, **kwargs)
<<<<<<< HEAD
        except Exception:
            smd = Smd_Response()
            return smd
=======
        except DecodeError:
            smd = Smd_Response(False, 'invalid token redirected to users page', [])
        except KeyError:
            smd = Smd_Response(message='user_id is not inside redis')
        return smd
>>>>>>> b2154c4e... code coverage done

    return wraper
