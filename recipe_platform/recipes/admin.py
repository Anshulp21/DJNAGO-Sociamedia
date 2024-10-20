# from django.contrib import admin

# # Register your models here.
# from django_celery_beat.models import PeriodicTask, CrontabSchedule

# # Create daily email task at 6 AM, Monday to Friday
# schedule, _ = CrontabSchedule.objects.get_or_create(hour=6, minute=0, day_of_week='1-5')
# PeriodicTask.objects.get_or_create(crontab=schedule, name='Send daily email', task='recipes.tasks.send_daily_email')



# from django.contrib import admin
# from .models import Recipe, Rating

# # Register your models here.
# admin.site.register(Recipe)
# admin.site.register(Rating)



from django.contrib import admin
from .models import Recipe, Rating

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Rating)
