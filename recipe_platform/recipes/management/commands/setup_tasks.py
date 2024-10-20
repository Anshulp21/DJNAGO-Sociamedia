from django.core.management.base import BaseCommand
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from recipes.tasks import send_daily_email

class Command(BaseCommand):
    help = 'Set up scheduled tasks'

    def handle(self, *args, **kwargs):
        schedule, created = CrontabSchedule.objects.get_or_create(
            hour=6, minute=0, day_of_week='1-5'
        )

        PeriodicTask.objects.get_or_create(
            crontab=schedule,
            name='Send daily email',
            task='recipes.tasks.send_daily_email',
        )

        self.stdout.write(self.style.SUCCESS('Successfully set up tasks'))



 # Replace 'your_image.jpg' with the actual image filename
