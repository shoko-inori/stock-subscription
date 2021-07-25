import os

from celery import Celery
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stocksubscription.settings')

app = Celery('stocksubscription')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Scheduling of the task
app.conf.beat_schedule = {
    'workdays_every_hour_between_9_and_5': {
        'task': 'mail.tasks.send_digest',
        'schedule': crontab(
            day_of_week='mon, tue, wed, thu, fri',
            hour='9-5'
        )
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
