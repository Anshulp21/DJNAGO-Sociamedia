# from django.apps import AppConfig


# # class RecipesConfig(AppConfig):
# #     default_auto_field = "django.db.models.BigAutoField"
# #     name = "recipes"


# from django.apps import AppConfig

# class RecipesConfig(AppConfig):
#     name = 'recipes'

#     def ready(self):
#         # Import the model here to avoid AppRegistryNotReady issues
#         from django_celery_beat.models import CrontabSchedule, PeriodicTask

#         # Create the schedule only if it doesn't already exist
#         schedule, created = CrontabSchedule.objects.get_or_create(
#             hour=6, minute=0, day_of_week='1-5'
#         )

#         # Create the periodic task to send daily email
#         PeriodicTask.objects.get_or_create(
#             crontab=schedule,
#             name='Send daily email',
#             task='recipes.tasks.send_daily_email',
#         )






# # class RecipesConfig(AppConfig):
# #     name = 'recipes'

# #     def ready(self):
# #         pass  # Temporarily disable the scheduling code to check if it solves the issue






# from django.apps import AppConfig
# from django_celery_beat.models import CrontabSchedule, PeriodicTask

# class RecipesConfig(AppConfig):
#     name = 'recipes'

#     def ready(self):
#         from django_celery_beat.models import CrontabSchedule, PeriodicTask

#         # Create the schedule for daily email task
#         schedule, created = CrontabSchedule.objects.get_or_create(
#             minute=0, hour=6, day_of_week='1-5'  # Monday to Friday
#         )

#         PeriodicTask.objects.get_or_create(
#             crontab=schedule,
#             name='Send daily email',
#             task='recipes.tasks.send_daily_email',
#         )

#         # Create the schedule for weekly CSV export
#         schedule_csv, created_csv = CrontabSchedule.objects.get_or_create(
#             minute=0, hour=6, day_of_week='1'  # Every Monday
#         )

#         PeriodicTask.objects.get_or_create(
#             crontab=schedule_csv,
#             name='Export users to CSV',
#             task='recipes.tasks.export_users_to_csv',
#         )





# from django.apps import AppConfig
# from django_celery_beat.models import CrontabSchedule, PeriodicTask

# class RecipesConfig(AppConfig):
#     name = 'recipes'

#     def ready(self):
#         # Import the model here to avoid AppRegistryNotReady issues
#         from django_celery_beat.models import CrontabSchedule, PeriodicTask

#         # Create the schedule only if it doesn't already exist
#         schedule, created = CrontabSchedule.objects.get_or_create(
#             hour=6, minute=0, day_of_week='1-5'
#         )

#         # Create the periodic task to send daily email
#         PeriodicTask.objects.get_or_create(
#             crontab=schedule,
#             name='Send daily email',
#             task='recipes.tasks.send_daily_email',
#         )








# from django.apps import AppConfig

# class RecipesConfig(AppConfig):
#     name = 'recipes'

#     def ready(self):
#         # Import the model here to avoid AppRegistryNotReady issues
#         from django_celery_beat.models import CrontabSchedule, PeriodicTask
#         from .tasks import send_daily_email  # Import your task here

#         # Create the schedule only if it doesn't already exist
#         schedule, created = CrontabSchedule.objects.get_or_create(
#             hour=6, minute=0, day_of_week='1-5'
#         )

#         # Create the periodic task to send daily email
#         PeriodicTask.objects.get_or_create(
#             crontab=schedule,
#             name='Send daily email',
#             task='recipes.tasks.send_daily_email',
#         )





from django.apps import AppConfig

class RecipesConfig(AppConfig):
    name = 'recipes'

    def ready(self):
        # No database queries here
        pass
