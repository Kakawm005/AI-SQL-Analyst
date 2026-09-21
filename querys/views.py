from django.shortcuts import render
from querys.models import products
from rest_framework.generics import ListCreateAPIView
from querys.serializers import ProductSerializer

class ListCreateProductView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = products.objects.all()
