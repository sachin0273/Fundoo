"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this utils module we created common functions hence most of the code can be reused
author:  Sachin Shrikant Jadhav
since :  25-09-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
import json
import jwt
from django.core.mail import send_mail
from pymitter import EventEmitter

from Fundoo import settings

ee = EventEmitter()


def Jwt_Token(payload):
    """

    :param payload: here we passing user information
    :return:this function return jwt token
    """
    jwt_token = {'token': jwt.encode(payload, "SECRET_KEY", algorithm="HS256").decode('utf-8')}
    return jwt_token


def load(filename):
    """

    :param filename: here we passing file name for open
    :return:this function return the content in the file

    """
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


# decorator usage
@ee.on("myevent")
def email_handler(message, recipient_list):
    """

    :param message: here we passing message for mail
    :param recipient_list: here we passing receiver mail
    :return:this function send the email
    """
    email_from = settings.EMAIL_HOST_USER
    subject = 'Thank you for registering to our site'
    send_mail(subject, message, email_from, recipient_list)


@ee.on("myevent2")
def reset_handler(message, recipient_list):
    """

    :param message: here we passing message for mail
    :param recipient_list: here we passing receiver mail
    :return:this function send the email

    """
    email_from = settings.EMAIL_HOST_USER
    subject = 'Reset your password'
    send_mail(subject, message, email_from, recipient_list)
