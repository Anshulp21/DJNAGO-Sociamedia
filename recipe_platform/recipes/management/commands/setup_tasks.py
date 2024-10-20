# from django.core.management.base import BaseCommand
# from django_celery_beat.models import CrontabSchedule, PeriodicTask
# from recipes.tasks import send_daily_email

# class Command(BaseCommand):
#     help = 'Set up scheduled tasks'

#     def handle(self, *args, **kwargs):
#         schedule, created = CrontabSchedule.objects.get_or_create(
#             hour=6, minute=0, day_of_week='1-5'
#         )

#         PeriodicTask.objects.get_or_create(
#             crontab=schedule,
#             name='Send daily email',
#             task='recipes.tasks.send_daily_email',
#         )

#         self.stdout.write(self.style.SUCCESS('Successfully set up tasks'))



#  # Replace 'your_image.jpg' with the actual image filename



from django.core.management.base import BaseCommand
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from recipes.tasks import export_users_to_csv, send_daily_email

class Command(BaseCommand):
    help = 'Set up scheduled tasks'

    def handle(self, *args, **kwargs):
        # Schedule for exporting users to CSV at 2 AM daily
        csv_schedule, csv_created = CrontabSchedule.objects.get_or_create(
            hour=2, minute=35  # Schedule at 2 AM
        )
        # Create or get the periodic task for exporting users
        csv_task, csv_task_created = PeriodicTask.objects.get_or_create(
            crontab=csv_schedule,
            name='Export users to CSV',  # Name of the task
            defaults={'task': 'recipes.tasks.export_users_to_csv'}  # Specifying the task function to run
        )

        # Schedule for sending daily email at 2 AM daily
        email_schedule, email_created = CrontabSchedule.objects.get_or_create(
            hour=2, minute=35 # Schedule at 2 AM
        )
        # Create or get the periodic task for sending daily email
        email_task, email_task_created = PeriodicTask.objects.get_or_create(
            crontab=email_schedule,
            name='Send daily email',  # Name of the task
            defaults={'task': 'recipes.tasks.send_daily_email'}  # Specifying the task function to run
        )

        # Print success message only if tasks were created
        if csv_task_created or email_task_created:
            self.stdout.write(self.style.SUCCESS('Successfully set up tasks for 2 AM daily'))
        else:
            self.stdout.write(self.style.WARNING('Tasks for 2 AM daily are already set up'))
