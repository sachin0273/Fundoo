import json

import requests

from utils import load

#
# data = load('note_test.json')
# print(data['note'][0])


# data = load('note_test.json')
# notes = data['note_create'][0]
# tt = json.dumps(notes)
# print(notes)
# url = 'http://127.0.0.1:8000' + '/note/' + 'create_note/'
# Response = requests.post(url,notes)
# print(Response.content)
url = 'http://127.0.0.1:8000/register/'
data = load('users/test.json')
print(data)
user = data['register'][0]
Response = requests.post(url, user)
print(Response.content)
