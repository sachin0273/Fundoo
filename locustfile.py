import json

from django.urls import reverse
from locust import HttpLocust, TaskSet

header = {"Content-Type": "application/json",
          "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                           ".eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0NDgwMTE1LCJqdGkiOiI0OTExNjVlMDU5ZmI0NTVjOWViMTJkZTAwMDA0NmQ4MSIsInVzZXJfaWQiOjF9.qi5kIR0nLp5nAddc4b825MAPMDLw6Cg03acOsHd5sVE"}

def login(l):
    l.client.post("/login/", {"username": "admin", "password": "admin123"})


def logout(l):
    l.client.get("/logout/", headers=header)


def reset_password(l):
    l.client.post("/sendemail/", {"email": "sachinjadhav0273@gmail.com"})


def note_put(l):
    l.client.put("/api/note/9",
                 json.dumps({"title": "stringjkjk", "note": "stringhh"}),
                 headers=header)


def note_post(l):
    l.client.post("/api/note/", json.dumps({
        "title": "string",
        "note": "string",
        "is_archive": True,
        "is_pin": True,
    }), headers=header)


def note_get(l):
    l.client.get("/api/note/", headers=header)


def label_post(l):
    l.client.post("/api/label/", json.dumps({"name": "jklll"}), headers=header)


def label_get(l):
    l.client.get("/api/label/", headers=header)


def label_put(l):
    l.client.put("/api/label/25", json.dumps({"name": "ty"}), headers=header)


def get_archive_note(l):
    l.client.get("/api/note/archive/", headers=header)


def get_trash_note(l):
    l.client.get("/api/note/trash/", headers=header)


def get_reminder_note(l):
    l.client.get("/api/note/reminder/", headers=header)


class UserBehavior(TaskSet):
    tasks = {reset_password: 1, note_post: 1, note_get: 1, note_put: 1, label_post: 1,
             label_get: 1, label_put: 1, get_archive_note: 1, get_trash_note: 1, get_reminder_note: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
