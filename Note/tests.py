from django.test import TestCase

# Create your tests here.
import requests
from users import urls
from utils import load

BASE_URL = 'http://127.0.0.1:8000'
header = {'Content_Type': 'Application/json',
          'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                           '.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcyMTA4NTQyLCJqdGkiOiI5ODhlZjdkM2NiYzU0NjZlYjRmNDJjMjlkMTA3Y2Q4ZSIsInVzZXJfaWQiOjF9.USnByMSrnKoYrVTLgyKUAvsKHPhOz9E4BBfTqgKTA2s'}


class Test_Note_crud_api:

    def test_create_note(self):
        data = load('Note/note_test.json')
        print(data)
        notes = data['note_create'][0]
        print(notes)
        url = BASE_URL + '/note/' + 'get_or_create_note/'
        Response = requests.post(url, notes, headers=header)
        print(Response.text)
        assert Response.status_code == 200

    def test_wrong_collaborator_and_label(self):
        data = load('Note/note_test.json')
        print(data)
        notes = data['note_create'][1]
        print(notes)
        url = BASE_URL + '/note/' + 'get_or_create_note/'
        Response = requests.post(url, notes, headers=header)
        print(Response.content)
        assert Response.status_code == 400

    def test_note_delete_valid(self):
        data = load('Note/note_test.json')
        id = data['note_crud'][0]['note_id']
        url = BASE_URL + '/note/' + 'update_or_delete_note/' + id
        Response = requests.delete(url, headers=header)
        assert Response.status_code == 200

    def test_note_delete_blank_input(self):
        data = load('Note/note_test.json')
        id = data['note_crud'][1]['note_id']
        url = BASE_URL + '/note/' + 'update_or_delete_note/' + id
        Response = requests.delete(url, headers=header)
        assert Response.status_code == 400

    def test_note_delete_invalid_input(self):
        data = load('Note/note_test.json')
        id = data['note_crud'][2]['note_id']
        url = BASE_URL + '/note/' + 'update_or_delete_note/' + id
        Response = requests.delete(url, headers=header)
        assert Response.status_code == 400

    def test_note_delete_string_input(self):
        data = load('Note/note_test.json')
        id = data['note_crud'][3]['note_id']
        url = BASE_URL + '/note/' + 'update_or_delete_note/' + id
        Response = requests.delete(url, headers=header)
        assert Response.status_code == 400

    def test_get_all_note_valid_user_id(self):
        data = load('Note/note_test.json')
        id = data['get_all_note'][0]['user_id']
        url = BASE_URL + '/note/' + 'get_or_create_note/'
        Response = requests.get(url, headers=header)
        assert Response.status_code == 200

    # def test_get_all_note_blank_input(self):
    #     data = load('Note/note_test.json')
    #     id = data['get_all_note'][1]['user_id']
    #     url = BASE_URL + '/note/' + 'get_or_create_note/'
    #     Response = requests.get(url, headers=header)
    #     assert Response.status_code == 400
    #
    # def test_get_all_note_invalid_input(self):
    #     data = load('Note/note_test.json')
    #     id = data['get_all_note'][2]['user_id']
    #     url = BASE_URL + '/note/' + 'get_or_create_note/'
    #     Response = requests.get(url, headers=header)
    #     assert Response.status_code == 400
    #
    # def test_get_all_note_string_input(self):
    #     data = load('Note/note_test.json')
    #     id = data['get_all_note'][3]['user_id']
    #     url = BASE_URL + '/note/' + 'get_or_create_note/'
    #     Response = requests.get(url, headers=header)
    #     assert Response.status_code == 400


class Test_Label_Crud_Api:
    def test_create_label_valid_input(self):
        data = load('Note/note_test.json')
        label = data['label_create'][0]
        url = BASE_URL + '/note/' + 'get_or_create_label/'
        Response = requests.post(url, label, headers=header)
        assert Response.status_code == 200

    def test_create_label_invalid_input(self):
        data = load('Note/note_test.json')
        label = data['label_create'][1]
        url = BASE_URL + '/note/' + 'get_or_create_label/'
        Response = requests.post(url, label, headers=header)
        assert Response.status_code == 400

    def test_put_label_valid_input(self):
        data = load('Note/note_test.json')
        label = data['put_label'][0]
        url = BASE_URL + '/note/' + 'update_or_delete_label/' + '3'
        Response = requests.put(url, label, headers=header)
        assert Response.status_code == 200

    def test_label_delete_valid(self):
        data = load('Note/note_test.json')
        id = data['delete_label'][0]['label_id']
        url = BASE_URL + '/note/' + 'update_or_delete_label/' + id
        Response = requests.delete(url, headers=header)
        assert Response.status_code == 200

    def test_label_delete_blank_input(self):
        data = load('Note/note_test.json')
        id = data['delete_label'][1]['label_id']
        url = BASE_URL + '/note/' + 'update_or_delete_label/' + id
        Response = requests.delete(url, headers=header)
        assert Response.status_code == 400

    def test_label_delete_invalid_input(self):
        data = load('Note/note_test.json')
        id = data['delete_label'][2]['label_id']
        url = BASE_URL + '/note/' + 'update_or_delete_label/' + id
        Response = requests.delete(url, headers=header)
        assert Response.status_code == 400

    def test_label_delete_string_input(self):
        data = load('Note/note_test.json')
        id = data['delete_label'][3]['label_id']
        url = BASE_URL + '/note/' + 'update_or_delete_label/' + id
        Response = requests.delete(url, headers=header)
        assert Response.status_code == 400

    def test_get_all_label_valid_user_id(self):
        data = load('Note/note_test.json')
        id = data['get_all_label'][0]['user_id']
        url = BASE_URL + '/note/' + 'get_or_create_label/'
        Response = requests.get(url, headers=header)
        assert Response.status_code == 200

    # def test_get_all_label_blank_input(self):
    #     data = load('Note/note_test.json')
    #     id = data['get_all_label'][1]['user_id']
    #     url = BASE_URL + '/note/' + 'get_or_create_label/'
    #     Response = requests.get(url, headers=header)
    #     assert Response.status_code == 400
    #
    # def test_get_all_label_invalid_input(self):
    #     data = load('Note/note_test.json')
    #     id = data['get_all_label'][2]['user_id']
    #     url = BASE_URL + '/note/' + 'get_or_create_label/'
    #     Response = requests.get(url, headers=header)
    #     assert Response.status_code == 400
    #
    # def test_get_all_label_string_input(self):
    #     data = load('Note/note_test.json')
    #     id = data['get_all_label'][3]['user_id']
    #     url = BASE_URL + '/note/' + 'get_or_create_label/'
    #     Response = requests.get(url, headers=header)
    #     assert Response.status_code == 400
