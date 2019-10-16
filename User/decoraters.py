import jwt
import redis
from django.contrib.auth.models import User
from django.http import HttpResponse
from jwt import DecodeError
from rest_framework.response import Response
from Services import redis
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
                smd = Smd_Response(False, 'invalid token redirected to User page', [])
                return HttpResponse(smd)
            user = User.objects.get(pk=decoded['user_id'])
            tokan = redis.Get(user.username)
            try:
                print('isssss token')
                payload = jwt.decode(tokan, settings.SECRET_KEY, algorithm="HS256")
            except DecodeError:
                smd = Smd_Response(False, 'invalid user redirected to User page', [])
                return HttpResponse(smd)
            user = User.objects.get(pk=payload['user_id'])
            if user:
                print('in wrapper', user)
                return function(request, *args, **kwargs)
            else:
                smd = Smd_Response(False, 'invalid user redirected to User page', [])
                return HttpResponse(smd)
        except Exception:
            smd = Smd_Response()
            return HttpResponse(smd)

    return wraper
