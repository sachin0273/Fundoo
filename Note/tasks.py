# import time
# from Note import views
# from Note import views
# from datetime import timedelta

from celery.task import task, periodic_task
from django.contrib.auth.models import User
from Lib.event_emmiter import email_event
from Note.models import Note
from django.utils import timezone


@task
def rebuild_search_index():
    user = User.objects.get(pk=id)
    # mimicking a long running process
    print(user.email)
    # print(note.title)
    message = 'hi hello'
    recipient_list = [user.email, ]
    email_event.emit("reset_password_event", message, recipient_list)
    print('rebuilt search index')
    return 42


@task
def task_save_latest_flickr_image():
    """

    Saves latest image from Flickr

    """
    notes = Note.objects.filter(reminder__isnull=False)
    for i in notes:
        nextTime = timezone.now() + timezone.timedelta(minutes=1)
        if timezone.now() <= i.reminder < nextTime:
            print('dkjjjjjjjjjjjjjj')
            rebuild_search_index.delay()
