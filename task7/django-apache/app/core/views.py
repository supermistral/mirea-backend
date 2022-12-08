from django.shortcuts import render

from . import services


def catalog(request):
    products_queryset = services.get_products()
    context = {'products': products_queryset}
    return render(request, 'catalog.html', context)


def users(request):
    users_queryset = services.get_users()
    context = {'users': users_queryset}
    return render(request, 'users.html', context)
