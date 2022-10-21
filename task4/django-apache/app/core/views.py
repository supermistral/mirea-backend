from django.shortcuts import render
from django.contrib.auth import get_user_model

from api.models import Product

User = get_user_model()


def catalog(request):
    products_queryset = Product.objects.all()
    context = {'products': products_queryset}
    return render(request, 'catalog.html', context)


def users(request):
    users_queryset = User.objects.all()
    context = {'users': users_queryset}
    return render(request, 'users.html', context)
