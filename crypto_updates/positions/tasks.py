from celery import shared_task
from .models import Test

# from celery.decorators import periodic_task
from celery.schedules import crontab

@shared_task
def create_test_object(name):
    Test.objects.create(name=name)

# @periodic_task(run_every=(crontab(minute='*/1')))
# def run_create_objs():
#     create_test_object.delay(name='new2020')

