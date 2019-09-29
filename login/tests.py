from django.test import TestCase
import pytest
import requests
from login import urls
from utils import load


def test_Registration():
    url = 'http://127.0.0.1:8000/register/'
    data = load('login/login.json')
    user = data['login'][2]
    Response = requests.post(url, user)
    assert Response.status_code == 400
