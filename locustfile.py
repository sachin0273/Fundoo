import datetime
import json

import requests
from locust import HttpLocust, TaskSet, task

class UserActions(TaskSet):

    def on_start(self):
        self.login()

    def login(self)
        # login to the application
        response = self.client.get('/accounts/login/')
        csrftoken = response.cookies['csrftoken']
        self.client.post('/accounts/login/',
                         {'username': 'username', 'password': 'password'},
                         headers={'X-CSRFToken': csrftoken})

    @task(1)
    def index(self):
        self.client.get('/')

    for i in range(4):
        @task(2)
        def first_page(self):
            self.client.get('/list_page/')


    @task(3)
    def get_second_page(self):
        self.client.('/create_page/', {'name': 'first_obj'}, headers={'X-CSRFToken': csrftoken})

    @task(4)
    def add_advertiser_api(self):
        auth_response = self.client.post('/auth/login/', {'username': 'suser', 'password': 'asdf1234'})
        auth_token = json.loads(auth_response.text)['token']
        jwt_auth_token = 'jwt '+auth_token
        now = datetime.datetime.now()

        current_datetime_string = now.strftime("%B %d, %Y")
        adv_name = 'locust_adv'
        data = {'name', current_datetime_string}
        adv_api_response = requests.post('http://127.0.0.1:8000/api/advertiser/', data, headers={'Authorization': jwt_auth_token})


class ApplicationUser(HttpLocust):
    task_set = UserActions
    min_wait = 0
    max_wait = 0