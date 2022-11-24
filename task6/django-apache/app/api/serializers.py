from rest_framework import serializers

from .models import Product, Customer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
            'name': {'write_only': True},
        }

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
        }
