# Recipe Platform

## Overview
This project is a social media platform for sharing and rating recipes.

## Features
- User authentication (Customers and Sellers)
- Rate limiting
- Recipe upload and rating
- Image resizing using Celery
- Daily email notifications
- Weekly CSV export to S3

## Setup
1. Clone the repository
2. Install the dependencies
   ```bash
   pip install -r requirements.txt



elery -A recipe_platform worker --pool=solo --loglevel=info
python manage.py runserver        
celery -A recipe_platform worker --loglevel=debug
celery -A recipe_platform worker --loglevel=info 
celery -A recipe_platform beat --loglevel=info  
