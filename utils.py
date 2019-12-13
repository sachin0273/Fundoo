"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this utils module we created common functions hence most of the code can be reused
author:  Sachin Shrikant Jadhav
since :  25-09-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
import json
import re

from django.http import JsonResponse


def load(filename):
    """

    :param filename: here we passing file name for open
    :return:this function return the content in the file

    """
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def validate_email(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    if match and 7 < len(email) < 120:
        return True
    else:
        return False


def Smd_Response(success=False, message='something was wrong', data=[], status_code=400):
    smd = {
        'success': success,
        'message': message,
        'data': data,
    }
    response = JsonResponse(smd, status=status_code)
    return response


def smd_response(success=False, message='something was wrong', data=[]):
    smd = {
        'success': success,
        'message': message,
        'data': data,
    }
    return smd


# 'import urllib'


from urllib import parse


def build_url(baseurl, path):
    """

    :param baseurl: here we passing base url
    :param path: here we passing actual path
    :return:this function is used for return the long url or actual url of given path

    """
    url_parts = list(parse.urlparse(baseurl))
    url_parts[2] = path
    return parse.urlunparse(url_parts)


# args = {'arg1': 'value1', 'arg2': 'value2'}
# # works with double slash scenario
# token = 'dfffffffffffffffffffffffffff'
# url1 = build_url('http://127.0.0.1:8000/readprofile/', token)
# print(url1)

#
#
# def call():
#     tt = Note.objects.all()
#     return tt
