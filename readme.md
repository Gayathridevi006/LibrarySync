# LibrarySync

LibrarySync is a Django-based web application for managing and synchronizing books, authors, borrow records, and generating reports. The project utilizes Django for backend development, MySQL as the database, and Redis for task management with Celery.

## Features

- **Book Management**: Add, update, and delete books.
- **Author Management**: Add, update, and delete authors.
- **Borrow Records**: Keep track of borrowing activity.
- **Reports**: Generate reports for library activities.
- **Celery Tasks**: Background task management with Redis and Celery.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.12 or higher
- MySQL Database
- Redis (for Celery)
- Django 5.1.4 or higher

## Installation

### 1. Clone the repository

```bash
html - https://github.com/Gayathridevi006/LibrarySync.git
github cli - gh repo clone Gayathridevi006/LibrarySync
ssh - git@github.com:Gayathridevi006/LibrarySync.git
cd LibrarySync



# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',
#     ),
# } in settings.py for json output of api 



## steps for users
for macOS 
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


change  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'librarysync_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
in settings.py 

python manage.py migrate
redis-server
python manage.py runserver
