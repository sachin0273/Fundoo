from __future__ import absolute_import, unicode_literals

import os
import sys


from celery import Celery
from celery.schedules import crontab
from django.conf import settings

sys.path.append(os.path.abspath('Fundoo'))
# app = Celery('Fundoo')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fundoo.settings.development')
app = Celery('Fundoo')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-1-minute': {
        'task': 'Note.tasks.task_check_reminder',
        'schedule': crontab(),
    },
}

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     # import utils
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
#
#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)
#
#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s('Happy Mondays!'),
#     )
#
#
# @app.task
# def test(arg):
#     import Note
#     print(arg)


