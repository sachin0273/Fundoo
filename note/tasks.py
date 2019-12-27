# import time
# from Note import views
# from Note import views
# from datetime import timedelta

from celery.task import task, periodic_task
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from lib.event_emmiter import email_event
from note.models import Note
from django.utils import timezone


@task
def task_send_email_for_reminder(user_id, title, pk):
    """

    :param user_id:here we get user id for geting appropriate user
    :param title:here we gate title of note
    :param pk:here we get id of note
    :return:this function is called when any reminder match and sens mail for reminder

    """
    user = User.objects.get(pk=user_id)
    # mimicking a long running process
    current_site = Site.objects.get_current()

    message = render_to_string('users/note_template.html', {
        'name': user.username,
        'title': title,
        'domain': current_site.domain,
        'note_id': pk
    })

    recipient_list = [user.email, ]
    email_event.emit("reminder_event", message, recipient_list)


@task
def task_check_reminder():
    """

    :return:this function is used for checking reminder every 1 minute

    """
    notes = Note.objects.filter(reminder__isnull=False)
    for note in notes:
        nextTime = timezone.now() + timezone.timedelta(minutes=1)
        if timezone.now() <= note.reminder < nextTime:
            task_send_email_for_reminder.delay(note.user_id, note.title, note.pk)





