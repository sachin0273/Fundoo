import jwt
import redis
from django.contrib.auth.models import User
from django.shortcuts import redirect
from jwt import DecodeError


def login_required(function):
    def wraper(request, *args, **kwargs):
        try:
            token = (eval(request.body))
            decoded = jwt.decode(token, "SECRET_KEY", algorithm="HS256")
            tokan = redis.get(decoded['username'])
            try:
                payload = jwt.decode(tokan, "SECRET_KEY", algorithm="HS256")
            except DecodeError:
                return redirect('loginpage')
            user = User.objects.get(username=payload['username'])
            if user:
                print('in wrapper', user)
                return function(request, *args, **kwargs)
            return redirect('loginpage')

        except Exception:
            return redirect('loginpage')
    return wraper
