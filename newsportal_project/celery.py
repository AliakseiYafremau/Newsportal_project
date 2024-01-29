import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsportal_project.settings')

app = Celery('newsportal_project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'newsletter_every_sunday': {
        'task': 'newsportal_app.tasks.send_newsletter',
        'schedule': crontab(hour='08', minute='00', day_of_week='monday'),
    },
}

app.conf.timezone = 'UTC'
