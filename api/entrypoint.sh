#!/bin/sh

python manage.py migrate auth
until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

python manage.py collectstatic --noinput

gunicorn Core.wsgi --bind 0.0.0.0:8001 --workers 4 --threads 4