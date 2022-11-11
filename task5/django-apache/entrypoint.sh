#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for PostgreSQL..."

    while ! nc -z $DB_HOST $DB_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "\nMakemigrations...\n"
python3 app/manage.py makemigrations

echo "\nMigrate...\n"
python3 app/manage.py migrate


if [ -n "$DJANGO_SUPERUSER_EMAIL" ]; then
    echo "\nCreating superuser...\n"
    echo "from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.filter(email='$DJANGO_SUPERUSER_EMAIL')
if not user.exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_LOGIN', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
else:
    user_admin = user.first()
    user_admin.set_password('$DJANGO_SUPERUSER_PASSWORD')
    user_admin.save()" | python3 app/manage.py shell
fi

exec "$@"