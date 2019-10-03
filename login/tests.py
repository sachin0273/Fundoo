from django.test import TestCase
import pytest
import requests
from login import urls
from utils import load


def test_Registration_valid_input():
    url = 'http://127.0.0.1:8000/register/'
    data = load('login/login.json')
    print(data)
    user = data['login'][0]
    Response = requests.post(url, user)
    assert Response.status_code == 400


def test_Registration_blank_input():

    url = 'http://127.0.0.1:8000/register/'
    data = load('login/login.json')
    user = data['login'][1]
    Response = requests.post(url, user)
    assert Response.status_code == 200


def test_Registration_email():

    url = 'http://127.0.0.1:8000/register/'
    data = load('login/login.json')
    user = data['login'][2]
    Response = requests.post(url, user)
    assert Response.status_code == 400


def test_Registration_blank_username():
    url = 'http://127.0.0.1:8000/register/'
    data = load('login/login.json')
    user = data['login'][3]
    Response = requests.post(url, user)
    assert Response.status_code == 400
