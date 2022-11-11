"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()


from django import db
from django.contrib.auth import get_user_model

User = get_user_model()


def check_password(environ, user, password):
    db.reset_queries()
    try:
        try:
            user = User.objects.get(username=user,
                                    is_active=True,
                                    is_superuser=True)
        except User.DoesNotExist:
            return None
        return user.check_password(password)
    finally:
        db.connection.close()
