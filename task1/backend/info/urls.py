from django.conf import settings
from django.urls import path

from . import views


if settings.DEBUG:
    urlpatterns = [path('', views.PyInfoView.as_view(), name='info')]
