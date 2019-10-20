import json

import requests

from utils import load

#
# data = load('note_test.json')
# print(data['note'][0])


data = load('note_test.json')
notes = data['put_label'][0]
tt = json.dumps(notes)
print(notes)
url = 'http://127.0.0.1:8000' + '/note/' + 'label/'+'3'
Response = requests.put(url, notes)
print(Response.content)
