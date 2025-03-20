#!/bin/sh
set -e

echo "Waiting for PostgreSQL to become available..."
# Loop until PostgreSQL is ready on host "db" and port 5432
while ! nc -z db 5432; do   
  sleep 1
done

echo "PostgreSQL is up, running migrations..."
cd /app/sistema_pedidos
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000
