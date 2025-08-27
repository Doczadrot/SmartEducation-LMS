import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SmartEducation.settings')

app = Celery('SmartEducation')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()