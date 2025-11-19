#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

echo "DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE"

python manage.py collectstatic --no-input
python manage.py migrate