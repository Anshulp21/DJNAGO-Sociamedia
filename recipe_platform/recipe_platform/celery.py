# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_platform.settings')

# app = Celery('recipe_platform')

# # Load task modules from all registered Django app configs.
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()







from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_platform.settings')

app = Celery('recipe_platform')

# Load configuration from Django settings, using a custom namespace 'CELERY'
app.config_from_object('django.conf:settings', namespace='CELERY')

# Ensure the broker retries connection on startup
app.conf.broker_connection_retry_on_startup = True

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
