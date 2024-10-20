from celery import shared_task
from PIL import Image
from django.core.mail import send_mail
import pandas as pd
import os
from tempfile import NamedTemporaryFile
import boto3
from django.conf import settings
import datetime
import logging
from .models import Recipe

logger = logging.getLogger(__name__)

@shared_task
def resize_image(image_path):
    try:
        with Image.open(image_path) as img:
            img = img.resize((800, 600))
            img.save(image_path)
        logger.info(f"Resized image at {image_path}")
        return f"Image resized successfully at {image_path}"
    except Exception as e:
        logger.error(f"Failed to resize image {image_path}: {e}")
        return None

@shared_task
def send_daily_email():
    today = datetime.date.today()
    if today.weekday() < 5:  # Monday to Friday
        recipients = ['user@example.com']  # Replace with dynamic emails if needed
        send_mail(
            'Daily Recipe Digest',
            'Here are today\'s recipes...',
            'from@example.com',
            recipients,
            fail_silently=False,
        )
        logger.info("Sent daily email to users.")

@shared_task
def export_users_to_csv():
    recipes = Recipe.objects.all().values('seller__username', 'name', 'description', 'created_at')
    
    df = pd.DataFrame(list(recipes))
    
    # Create a temporary file
    with NamedTemporaryFile(delete=False, suffix='.csv') as tmp_file:
        df.to_csv(tmp_file.name, index=False)
        
        # Upload the CSV to S3
        s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        
        with open(tmp_file.name, 'rb') as csv_file:
            s3.upload_fileobj(csv_file, settings.AWS_STORAGE_BUCKET_NAME, 'users_recipes.csv')

        logger.info("Uploaded CSV to S3")

    # Optionally delete the local file after upload
    os.remove(tmp_file.name)
