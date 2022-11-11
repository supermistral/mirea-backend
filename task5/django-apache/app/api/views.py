from rest_framework import generics, status
from rest_framework.response import Response

from .models import Product, Customer
from .serializers import (
    ProductSerializer, ProductDetailSerializer,
    CustomerSerializer, CustomerDetailSerializer)


class BaseListAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwags):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BaseDetailAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductListAPIView(BaseListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailAPIView(BaseDetailAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


class CustomerListAPIView(BaseListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerDetailAPIView(BaseDetailAPIView):
    serializer_class = CustomerDetailSerializer
    queryset = Customer.objects.all()
