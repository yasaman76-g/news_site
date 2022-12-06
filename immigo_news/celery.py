import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','immigo_news.settings')

celery = Celery('immigo_news')

celery.config_from_object('django.conf:settings',namespace='CELERY')

celery.autodiscover_tasks()