#!/bin/bash

# Wait for database to be ready
echo "Waiting for database..."
sleep 5

# Run database migrations
echo "Running database migrations..."
python src/manage.py migrate

# Create superuser if not exists
echo "Creating superuser if not exists..."
python src/manage.py createsuperuser --noinput || true

# Collect static files
echo "Collecting static files..."
python src/manage.py collectstatic --noinput

# Start development server
echo "Starting development server..."
python src/manage.py runserver 0.0.0.0:8000
