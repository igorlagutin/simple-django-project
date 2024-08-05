#!/bin/sh

echo "Starting server..."
python manage.py migrate
#python manage.py collectstatic --noinput

gunicorn simpleDjangoProject.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
