"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Purpose: in this module we create jwt_token for email verification 
author:  Sachin Shrikant Jadhav
since :  25-09-2019

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
import jwt
import requests

from Fundoo import settings


def Jwt_Token(payload):
    """
    :param payload: here we passing user information
    :return:this function return jwt token
    """
    jwt_token = {'token': jwt.encode(payload, "SECRET_KEY", algorithm="HS256").decode('utf-8')}
    return jwt_token['token']


def Jwt_token(payload):
    response = requests.post(settings.Token, payload)
    return response.json()['access']
