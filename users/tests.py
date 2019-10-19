from django.test import TestCase
import pytest
import requests
from users import urls
from utils import load

BASE_URL = 'http://127.0.0.1:8000'


class Test_Registration_Api:
    def test_Registration_valid_input(self):
        url = 'http://127.0.0.1:8000/register/'
        data = load('users/test.json')
        print(data)
        user = data['register'][0]
        Response = requests.post(url, user)
        assert Response.status_code == 200

    def test_Registration_blank_input(self):
        url = 'http://127.0.0.1:8000/register/'
        data = load('users/test.json')
        user = data['register'][1]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_Registration_email(self):
        url = 'http://127.0.0.1:8000/register/'
        data = load('users/test.json')
        user = data['register'][2]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_Registration_blank_username(self):
        url = 'http://127.0.0.1:8000/register/'
        data = load('users/test.json')
        user = data['register'][3]
        Response = requests.post(url, user)
        assert Response.status_code == 400


class Test_Login_Api:
    def test_login_valid_input(self):
        url = BASE_URL + '/users/'
        data = load('users/test.json')
        user = data['users'][2]
        Response = requests.post(url, user)
        assert Response.status_code == 200

    def test_login_invalid_input(self):
        url = BASE_URL + '/users/'
        data = load('users/test.json')
        user = data['users'][0]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_login_blank_input(self):
        url = BASE_URL + '/users/'
        data = load('users/test.json')
        user = data['users'][1]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_login_username_blank_input(self):
        url = BASE_URL + '/users/'
        data = load('users/test.json')
        user = data['users'][3]
        Response = requests.post(url, user)
        assert Response.status_code == 400


class Test_Reset_Password_API:

    def test_reset_password_valid_input(self):
        url = BASE_URL + '/Reset_Passward/'
        data = load('users/test.json')
        user = data['Reset_password'][4]
        Response = requests.post(url, user)
        assert Response.status_code == 200

    def test_reset_password_invalid_input(self):
        url = BASE_URL + '/Reset_Passward/'
        data = load('users/test.json')
        user = data['Reset_password'][1]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_reset_password_iinvalid_input(self):
        url = BASE_URL + '/Reset_Passward/'
        data = load('users/test.json')
        user = data['Reset_password'][2]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_reset_password_blank_input(self):
        url = BASE_URL + '/Reset_Passward/'
        data = load('users/test.json')
        user = data['Reset_password'][3]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_reset_password_email_not_exist(self):
        url = BASE_URL + '/Reset_Passward/'
        data = load('users/test.json')
        user = data['Reset_password'][0]
        Response = requests.post(url, user)
        assert Response.status_code == 400
