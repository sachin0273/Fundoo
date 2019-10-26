import jwt
import redis
from django.contrib.auth.models import User
from django.http import HttpResponse
from jwt import DecodeError
from rest_framework.response import Response
from Lib import redis
from utils import Smd_Response
from Fundoo import settings


def login_required(function):
    def wraper(request, *args, **kwargs):
        try:
            header = request.META['HTTP_AUTHORIZATION']
            token = header.split(' ')
            try:
                decoded = jwt.decode(token[1], settings.SECRET_KEY, algorithm="HS256")
            except DecodeError:
                smd = Smd_Response(False, 'invalid token redirected to users page', [])
                return HttpResponse(smd)
            redis_token = redis.Get(decoded['user_id'])
            try:
                jwt.decode(redis_token, settings.SECRET_KEY, algorithm="HS256")
            except DecodeError:
                smd = Smd_Response(False, 'invalid user redirected to users page', [])
                return HttpResponse(smd)
            return function(request, *args, **kwargs)
        except Exception:
            smd = Smd_Response()
            return HttpResponse(smd)

    return wraper
