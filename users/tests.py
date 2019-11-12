from django.test import TestCase
import pytest
import requests
from utils import load

from django.conf import settings


class Test_Registration_Api:
    def test_Registration_valid_input(self):
        url = settings.BASE_URL + '/register/'
        data = load('users/test.json')
        print(data)
        user = data['register'][0]
        Response = requests.post(url, user)
        assert Response.status_code == 200

    def test_Registration_blank_input(self):
        url = settings.BASE_URL + '/register/'
        data = load('users/test.json')
        user = data['register'][1]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_Registration_email(self):
        url = settings.BASE_URL + '/register/'
        data = load('users/test.json')
        user = data['register'][2]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_Registration_blank_username(self):
        url = settings.BASE_URL+'/register/'
        data = load('users/test.json')
        user = data['register'][3]
        Response = requests.post(url, user)
        assert Response.status_code == 400


class Test_Login_Api:
    def test_login_valid_input(self):
        url = settings.BASE_URL + '/login/'
        data = load('users/test.json')
        user = data['login'][2]
        Response = requests.post(url, user)
        assert Response.status_code == 200

    def test_login_invalid_input(self):
        url = settings.BASE_URL + '/login/'
        data = load('users/test.json')
        user = data['login'][0]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_login_blank_input(self):
        url = settings.BASE_URL + '/login/'
        data = load('users/test.json')
        user = data['login'][1]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_login_username_blank_input(self):
        url = settings.BASE_URL + '/login/'
        data = load('users/test.json')
        user = data['login'][3]
        Response = requests.post(url, user)
        assert Response.status_code == 400


class Test_Reset_Password_API:

    def test_reset_password_valid_input(self):
        url = settings.BASE_URL + '/send_email/'
        data = load('users/test.json')
        user = data['Reset_password'][4]
        Response = requests.post(url, user)
        assert Response.status_code == 200

    def test_reset_password_invalid_input(self):
        url = settings.BASE_URL + '/send_email/'
        data = load('users/test.json')
        user = data['Reset_password'][1]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_reset_password_iinvalid_input(self):
        url = settings.BASE_URL + '/send_email/'
        data = load('users/test.json')
        user = data['Reset_password'][2]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_reset_password_blank_input(self):
        url = settings.BASE_URL + '/send_email/'
        data = load('users/test.json')
        user = data['Reset_password'][3]
        Response = requests.post(url, user)
        assert Response.status_code == 400

    def test_reset_password_email_not_exist(self):
        url = settings.BASE_URL + '/send_email/'
        data = load('users/test.json')
        user = data['Reset_password'][0]
        Response = requests.post(url, user)
        assert Response.status_code == 400

<<<<<<< HEAD
=======
    def test_resetpassword(self):
        url = settings.BASE_URL + '/setnewpassword/sachin0273'
        data = load('users/test.json')
        user = data['reset_password'][0]
        Response = requests.post(url, user)
        assert Response.status_code == 200

    def test_resetpassword_blank(self):
        url = settings.BASE_URL + '/setnewpassword/sachin0273'
        data = load('users/test.json')
        user = data['reset_password'][1]
        Response = requests.post(url, user)
        assert Response.status_code == 200

    def test_resetpassword_no_confirm_password(self):
        url = settings.BASE_URL + '/setnewpassword/sachin0273'
        data = load('users/test.json')
        user = data['reset_password'][2]
        Response = requests.post(url, user)
        assert Response.status_code == 200

    def test_resetpassword_no_password(self):
        url = settings.BASE_URL + '/setnewpassword/sachin0273'
        data = load('users/test.json')
        user = data['reset_password'][3]
        Response = requests.post(url, user)
        assert Response.status_code == 200


>>>>>>> 2f1c5cd5... elastic search done
