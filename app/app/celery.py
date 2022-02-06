import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

app = Celery("tkk")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.CELERYBEAT_SCHEDULE = {
    "refresh_mails": {
        "task": "mails.tasks.refresh_mails",
        "schedule": crontab(minute="*/5"),
    },
}
