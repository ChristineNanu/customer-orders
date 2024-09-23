#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Install requirements
pip install --no-cache-dir -r requirements.txt

# Run migrations
python manage.py migrate

# Start the Django server
exec python manage.py runserver 0.0.0.0:8000
