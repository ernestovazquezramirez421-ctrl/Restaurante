#!/usr/bin/env bash
# Exit on error
set -o errexit

# Forzar variable de entorno por seguridad
export DJANGO_SETTINGS_MODULE=restaurante.settings

# Ejecutar Gunicorn
gunicorn restaurante_marisco.wsgi:application --bind 0.0.0.0:$PORT --workers 4
