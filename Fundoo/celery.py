import os
from celery import Celery
from django.conf import settings
import Note

project = Celery('Fundoo', include=['Note.tasks'])
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fundoo.settings')
project.config_from_object('django.conf:settings')
