import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','news_site.settings')

celery = Celery('news_site')

celery.config_from_object('django.conf:settings',namespace='CELERY')

celery.autodiscover_tasks()