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

    def test_ll(self):
        data = load('Note/note_test.json')
        print(data)
        notes = data['note_create'][0]
        print(notes)
        url = BASE_URL + '/note/' + 'note_create/'
        Response = requests.post(url, notes)
        print(Response.content)
        assert Response.status_code == 200

    def test_wrong_collaborator_and_label(self):
        data = load('Note/note_test.json')
        print(data)
        notes = data['note_create'][1]
        print(notes)
        url = BASE_URL + '/note/' + 'note_create/'
        Response = requests.post(url, notes)
        print(Response.content)
        assert Response.status_code == 400

    def test_blank_collaborator_and_label(self):
        data = load('Note/note_test.json')
        print(data)
        notes = data['note_create'][2]
        print(notes)
        url = BASE_URL + '/note/' + 'note_create/'
        Response = requests.post(url, notes)
        print(Response.content)
        assert Response.status_code == 200

    def test_note_delete_valid(self):
        data = load('Note/note_test.json')
        id = data['note_crud'][0]['note_id']
        url = BASE_URL + '/note/' + 'note_crud/' + id
        Response = requests.delete(url)
        assert Response.status_code == 200

    def test_note_delete_blank_input(self):
        data = load('Note/note_test.json')
        id = data['note_crud'][1]['note_id']
        url = BASE_URL + '/note/' + 'note_crud/' + id
        Response = requests.delete(url)
        assert Response.status_code == 400

    def test_note_delete_invalid_input(self):
        data = load('Note/note_test.json')
        id = data['note_crud'][2]['note_id']
        url = BASE_URL + '/note/' + 'note_crud/' + id
        Response = requests.delete(url)
        assert Response.status_code == 400

    def test_note_delete_string_input(self):
        data = load('Note/note_test.json')
        id = data['note_crud'][3]['note_id']
        url = BASE_URL + '/note/' + 'note_crud/' + id
        Response = requests.delete(url)
        assert Response.status_code == 400

    def test_get_all_note_valid_user_id(self):
        data = load('Note/note_test.json')
        id = data['get_all_note'][0]['user_id']
        url = BASE_URL + '/note/' + 'Note/' + id
        Response = requests.get(url)
        assert Response.status_code == 200

    def test_get_all_note_blank_input(self):
        data = load('Note/note_test.json')
        id = data['get_all_note'][1]['user_id']
        url = BASE_URL + '/note/' + 'Note/' + id
        Response = requests.get(url)
        assert Response.status_code == 400

    def test_get_all_note_invalid_input(self):
        data = load('Note/note_test.json')
        id = data['get_all_note'][2]['user_id']
        url = BASE_URL + '/note/' + 'Note/' + id
        Response = requests.get(url)
        assert Response.status_code == 400

    def test_get_all_note_string_input(self):
        data = load('Note/note_test.json')
        id = data['get_all_note'][3]['user_id']
        url = BASE_URL + '/note/' + 'Note/' + id
        Response = requests.get(url)
        assert Response.status_code == 400

    def test_create_label_valid_input(self):
        data = load('Note/note_test.json')
        label = data['label_create'][0]
        url = BASE_URL + '/note/' + 'create_label/'
        Response = requests.post(url, label)
        assert Response.status_code == 200

    def test_create_label_invalid_input(self):
        data = load('Note/note_test.json')
        label = data['label_create'][1]
        url = BASE_URL + '/note/' + 'create_label/'
        Response = requests.post(url, label)
        assert Response.status_code == 400

    def test_put_label_valid_input(self):
        data = load('Note/note_test.json')
        label = data['put_label'][0]
        url = BASE_URL + '/note/' + 'label/'+'3'
        Response = requests.put(url, label)
        assert Response.status_code == 200

    def test_label_delete_valid(self):
        data = load('Note/note_test.json')
        id = data['delete_label'][0]['label_id']
        url = BASE_URL + '/note/' + 'label/' + id
        Response = requests.delete(url)
        assert Response.status_code == 200

    def test_label_delete_blank_input(self):
        data = load('Note/note_test.json')
        id = data['delete_label'][1]['label_id']
        url = BASE_URL + '/note/' + 'label/' + id
        Response = requests.delete(url)
        assert Response.status_code == 400

    def test_label_delete_invalid_input(self):
        data = load('Note/note_test.json')
        id = data['delete_label'][2]['label_id']
        url = BASE_URL + '/note/' + 'label/' + id
        Response = requests.delete(url)
        assert Response.status_code == 400

    def test_label_delete_string_input(self):
        data = load('Note/note_test.json')
        id = data['delete_label'][3]['label_id']
        url = BASE_URL + '/note/' + 'label/' + id
        Response = requests.delete(url)
        assert Response.status_code == 400

    def test_get_all_label_valid_user_id(self):
        data = load('Note/note_test.json')
        id = data['get_all_label'][0]['user_id']
        url = BASE_URL + '/note/' + 'label/' + id
        Response = requests.get(url)
        assert Response.status_code == 200

    def test_get_all_label_blank_input(self):
        data = load('Note/note_test.json')
        id = data['get_all_label'][1]['user_id']
        url = BASE_URL + '/note/' + 'label/' + id
        Response = requests.get(url)
        assert Response.status_code == 400

    def test_get_all_label_invalid_input(self):
        data = load('Note/note_test.json')
        id = data['get_all_label'][2]['user_id']
        url = BASE_URL + '/note/' + 'label/' + id
        Response = requests.get(url)
        assert Response.status_code == 400

    def test_get_all_label_string_input(self):
        data = load('Note/note_test.json')
        id = data['get_all_label'][3]['user_id']
        url = BASE_URL + '/note/' + 'label/' + id
        Response = requests.get(url)
        assert Response.status_code == 400

# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
#     headers={'Accept': 'application/vnd.github.v3.text-match+json'},
# )
