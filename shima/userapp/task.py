import requests
from celery import shared_task
from userapp.models import Users,Payment,Attendance
from hubs.models import Hub
import logging

@shared_task
def asign_payment():
    logging.info()
    pass
@shared_task
def asign_attendance():
    users=User.objects.all()
    for user in users:
        Attendance.objects.create(user=user,is_present=False)
    