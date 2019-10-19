from django.test import TestCase

# Create your tests here.
import requests
from users import urls
from utils import load

BASE_URL = 'http://127.0.0.1:8000'


class Test_Social_share_Api:
    def test_social_share_Api_twitter_input(self):
        data = load('Note/note_test.json')
        print(data)
        note_id = data['social_share'][0]['note_id']
        provider = data['social_share'][0]['provider']
        url = BASE_URL + '/share_note/' + note_id + '/' + provider
        Response = requests.get(url)
        assert Response.status_code == 200

    def test_social_share_Api_invalid_note_id(self):
        data = load('Note/note_test.json')
        print(data)
        note_id = data['social_share'][1]['note_id']
        provider = data['social_share'][1]['provider']
        url = BASE_URL + '/share_note/' + note_id + '/' + provider
        Response = requests.get(url)
        assert Response.status_code == 400

    def test_social_share_Api_blank_input(self):
        data = load('Note/note_test.json')
        print(data)
        note_id = data['social_share'][2]['note_id']
        provider = data['social_share'][2]['provider']
        url = BASE_URL + '/share_note/' + note_id + '/' + provider
        Response = requests.get(url)
        assert Response.status_code == 400

    def test_social_share_Api_reddit_input(self):
        data = load('Note/note_test.json')
        print(data)
        note_id = data['social_share'][3]['note_id']
        provider = data['social_share'][3]['provider']
        url = BASE_URL + '/share_note/' + note_id + '/' + provider
        Response = requests.get(url)
        assert Response.status_code == 200

    def test_social_share_Api_invalid_provider(self):
        data = load('Note/note_test.json')
        print(data)
        note_id = data['social_share'][4]['note_id']
        provider = data['social_share'][4]['provider']
        url = BASE_URL + '/share_note/' + note_id + '/' + provider
        Response = requests.get(url)
        assert Response.status_code == 400


