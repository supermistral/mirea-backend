from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from api.models import Product

User = get_user_model()


def get_users() -> QuerySet[User]:
    return User.objects.all()


def get_products() -> QuerySet[Product]:
    return Product.objects.all()
