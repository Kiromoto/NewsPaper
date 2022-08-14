from django_apscheduler.models import DjangoJobExecution

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import *

def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)

def weekly_mails():
    print('Print from TASKS.py every 10 seconds! weekly_mails')
    for cat in Category.objects.all():
        print(cat.name)

