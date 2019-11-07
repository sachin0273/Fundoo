import time

from celery.task import task, periodic_task


@task(ignore_result=True)
def send_email(recepient, title, subject):
    print('sending email')


@task
def rebuild_search_index():
    # mimicking a long running process
    print('rebuilt search index')
    return 42


from celery.schedules import crontab


# from celery.decorators import periodic_task
# from celery.utils.log import get_task_logger


# logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab()),
    name="task_save_latest_flickr_image",
    ignore_result=True
)
def task_save_latest_flickr_image():
    """
    Saves latest image from Flickr
    """
    rebuild_search_index.delay()
    return 'rhjrfgdghfghf'
