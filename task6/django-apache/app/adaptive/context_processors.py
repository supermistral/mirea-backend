from django.conf import settings


def user_data(request):
    return {'USER_DATA_KEYS': settings.USER_DATA_KEYS}
