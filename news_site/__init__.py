from .celery import celery

celery.config_from_object('django.conf:settings',namespace='CELERY')