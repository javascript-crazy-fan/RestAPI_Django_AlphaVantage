import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

app = Celery("BTCPrice")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.CELERYBEAT_SCHEDULE = {
    "price": {
        "task": "quotes.views.post",
        "schedule": crontab(hour="*"),
    },
}
