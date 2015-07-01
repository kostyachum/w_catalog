from __future__ import absolute_import

from django.conf import settings

from celery import Celery

app = Celery('catalog')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task
def alive():
	""" Task for testing """
	print "alive"