#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for PostgreSQL..."

    while ! nc -z $DB_HOST $DB_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo -e "\nInstalling python packages...\n"
pip install -r requirements.txt

echo -e "\nMakemigrations...\n"
python manage.py makemigrations

echo -e "\nMigrate...\n"
python manage.py migrate

exec "$@"