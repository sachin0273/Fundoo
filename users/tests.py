from django.test import TestCase
from Note.models import Note, Label
from django.urls import reverse
import pytest
import requests
from utils import load
import time
from django.conf import settings
from django.test import Client
from django.test.client import RequestFactory
from users.views import Login


class TestModel(TestCase):
    def test__str__method(self):
        note = Note(title="My entry title")
        self.assertEqual(str(note), note.title)

    def test__str__invalid(self):
        note = Note(title='hi hello', note="it's important")
        self.assertNotEqual(str(note), note.note)

    def test__str__valid(self):
        note = Note(title='hi hello', note="it's important")
        self.assertEqual(str(note), 'hi hello')

    def test__str__(self):
        note = Note(title='hi hello', note="it's important")
        self.assertNotEqual(str(note), 'hello')

    def test__str__label(self):
        label = Label(name='jklm')
        self.assertEqual(label.__str__(), 'jklm')

    def test__str__invalid_label(self):
        label = Label(name='jklm')
        self.assertNotEqual(str(label), 'hi hello')

    def test__str__object(self):
        label = Label(name='hi hello')
        self.assertEqual(str(label), label.name)

    def test__repr__label(self):
        label = Label(name='hi hello')
        expected = 'Object: hi hello'
        self.assertEqual(label.__repr__(), expected)

    def test__repr__label_invalid(self):
        label = Label(name='hi hel')
        expected = 'Object: hi hello'
        self.assertNotEqual(label.__repr__(), expected)

    def test__repr__label_new(self):
        label = Label(name='hello')
        expected = 'Object: hello'
        self.assertEqual(label.__repr__(), expected)

    def test__repr__note(self):
        note = Note(title='hello', note="important", is_archive=True)
        actual = repr(note)
        self.assertEqual(actual, "Note('hello','important',True)")

    def test__repr__note_invalid(self):
        note = Note(title='hello', note="important", is_archive=True)
        actual = repr(note)
        self.assertNotEqual(actual, 'Note(hello,important)')

    def test__repr__note_new(self):
        note = Note(title='hi', note="important", is_archive=True)
        actual = repr(note)
        self.assertEqual(actual, "Note('hi','important',True)")


class TestUsersApp(TestCase):
    fixtures = ['fixtures/django_db']

    def test_Registration_valid_input(self):
        url1 = reverse('register')
        url = settings.BASE_URL + url1
        data = load('users/test.json')
        print(data)
        user = data['register'][0]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 200)

    def test_Registration_blank_input(self):
        url = settings.BASE_URL + reverse('register')
        data = load('users/test.json')
        user = data['register'][1]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_Registration_email(self):
        url = settings.BASE_URL + reverse('register')
        data = load('users/test.json')
        user = data['register'][2]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_Registration_blank_username(self):
        url = settings.BASE_URL + reverse('register')
        data = load('users/test.json')
        user = data['register'][3]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_login_valid_input(self):
        url = settings.BASE_URL + reverse('users')
        c = Client()
        data = load('users/test.json')
        user = data['login'][7]
        response = c.post(url, user)
        self.assertEqual(response.status_code, 200)

    def test_login_invalid_input(self):
        url = settings.BASE_URL + reverse('users')
        data = load('users/test.json')
        user = data['login'][0]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_login_blank_input(self):
        url = settings.BASE_URL + reverse('users')
        data = load('users/test.json')
        user = data['login'][1]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_login_username_blank_input(self):
        url = settings.BASE_URL + reverse('users')
        data = load('users/test.json')
        user = data['login'][3]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_login_5(self):
        url = settings.BASE_URL + reverse('users')
        data = load('users/test.json')
        user = data['login'][4]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_login_6(self):
        url = settings.BASE_URL + reverse('users')
        data = load('users/test.json')
        user = data['login'][5]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_login_7(self):
        url = settings.BASE_URL + reverse('users')
        data = load('users/test.json')
        user = data['login'][6]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_login_8(self):
        url = settings.BASE_URL + reverse('users')
        data = load('users/test.json')
        user = data['login'][2]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_reset_password_valid_input(self):
        url = settings.BASE_URL + reverse('reset_passward')
        data = load('users/test.json')
        user = data['Reset_password'][5]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 200)

    def test_reset_password_invalid_input(self):
        url = settings.BASE_URL + reverse('reset_passward')
        data = load('users/test.json')
        user = data['Reset_password'][1]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_reset_password_iinvalid_input(self):
        url = settings.BASE_URL + reverse('reset_passward')
        data = load('users/test.json')
        user = data['Reset_password'][2]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_reset_password_blank_input(self):
        url = settings.BASE_URL + reverse('reset_passward')
        data = load('users/test.json')
        user = data['Reset_password'][3]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_reset_password_email_not_exist(self):
        url = settings.BASE_URL + reverse('reset_passward')
        data = load('users/test.json')
        user = data['Reset_password'][1]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_reset_password_5(self):
        url = settings.BASE_URL + reverse('reset_passward')
        data = load('users/test.json')
        user = data['Reset_password'][0]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 400)

    def test_resetpassword(self):
        url = settings.BASE_URL + reverse('resetpassword', args=['jadhav123'])
        data = load('users/test.json')
        user = data['reset_password'][0]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 200)

    def test_resetpassword_blank(self):
        url = settings.BASE_URL + reverse('resetpassword', args=['jadhav123'])
        data = load('users/test.json')
        user = data['reset_password'][1]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 200)

    def test_resetpassword_no_confirm_password(self):
        url = settings.BASE_URL + reverse('resetpassword', args=['jadhav123'])
        data = load('users/test.json')
        user = data['reset_password'][2]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 200)

    def test_resetpassword_no_password(self):
        url = settings.BASE_URL + reverse('resetpassword', args=['jadhav123'])
        data = load('users/test.json')
        user = data['reset_password'][3]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 200)

    def test_resetpassword_4(self):
        url = settings.BASE_URL + reverse('resetpassword', args=['jadhav123'])
        data = load('users/test.json')
        user = data['reset_password'][4]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 200)

    def test_resetpassword_5(self):
        url = settings.BASE_URL + reverse('resetpassword', args=['jadhav123'])
        data = load('users/test.json')
        user = data['reset_password'][5]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 200)

    def test_resetpassword_6(self):
        url = settings.BASE_URL + reverse('resetpassword', args=['jadhav123'])
        data = load('users/test.json')
        user = data['reset_password'][6]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 200)

    def test_resetpassword_7(self):
        url = settings.BASE_URL + reverse('resetpassword', args=['jadhav123'])
        data = load('users/test.json')
        user = data['reset_password'][7]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 200)

    def test_resetpassword_8(self):
        url = settings.BASE_URL + reverse('resetpassword', args=['jadhjjav123'])
        data = load('users/test.json')
        user = data['reset_password'][7]
        c = Client()
        response = c.post(url, user)
        self.assertEqual(response.status_code, 200)
