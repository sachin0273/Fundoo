import jwt
import redis
from django.contrib.auth.models import User
from django.shortcuts import redirect
from jwt import DecodeError
from Services import redis

from Fundoo import settings


def login_required(function):
    def wraper(request, *args, **kwargs):
        try:
            rty = request.META['HTTP_AUTHORIZATION']
            gh = rty.split(' ')
            print(gh)
            try:
                decoded = jwt.decode(gh[1], settings.SECRET_KEY, algorithm="HS256")
            except DecodeError:
                return redirect('loginpage', '000000000000000000')
            print(decoded)
            tokan = redis.Get(decoded['user_id'])
            if tokan is None:
                print('is token')
                redis.Set(decoded['user_id'], gh[1])
                user = User.objects.get(pk=decoded['user_id'])
                if user:
                    print('in wrapper', user)
                    return function(request, *args, **kwargs)
            else:
                try:
                    print('isssss token')
                    payload = jwt.decode(tokan, settings.SECRET_KEY, algorithm="HS256")
                except DecodeError:
                    return redirect('loginpage', '1111111111111111111111111111')
                user = User.objects.get(pk=payload['user_id'])
                if user:
                    print('in wrapper', user)
                    return function(request, *args, **kwargs)
                return redirect('loginpage', '22222222222222222222222222')

        except Exception:
            return redirect('loginpage', '33333333333333333333333333333333333')

    return wraper
