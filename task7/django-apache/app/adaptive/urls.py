from django.urls import path

from . import views


urlpatterns = [
    path('userdata/<key>/', views.user_data, name='user_data'),
    path('pdf-files/download/<filename>/', views.download_pdf_file, name='download_pdf_file'),
    path('pdf-files/', views.pdf_files, name='pdf_files'),
    path('', views.index, name='index'),
]
