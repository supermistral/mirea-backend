from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)


class CustomerManager(BaseUserManager):
    def create(self, email, name, password=None):
        if not email:
            raise ValueError("Email address is required")

        customer = self.model(
            email=self.normalize_email(email),
            name=name
        )
        customer.set_password(password)
        customer.save()

        return customer


class Customer(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=50)

    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
