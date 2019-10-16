"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this utils module we created common functions hence most of the code can be reused
author:  Sachin Shrikant Jadhav
since :  25-09-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

import json
from django.http import JsonResponse


def load(filename):
    """

    :param filename: here we passing file name for open
    :return:this function return the content in the file

    """
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


import re


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

