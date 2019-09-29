import re
import json
import jwt
from pyee import BaseEventEmitter

mail = BaseEventEmitter


# email_from = settings.EMAIL_HOST_USER


def Jwt_Token(payload):
    jwt_token = {'token': jwt.encode(payload, "SECRET_KEY", algorithm="HS256").decode('utf-8')}
    return jwt_token


def load(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data

# @mail.on('event')
# def event_handler():
#     print('BANG BANG')
#
#
# mail.emit('event')
