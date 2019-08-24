#from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from apps.catalogs.models import Category, Product
from apps.api.serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer

class CategoryListView(ListAPIView, CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

