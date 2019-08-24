from django.urls import path
from apps.api.views import CategoryListView, ProductListView, ProductDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='api-categories-list'),
    path('products/', ProductListView.as_view(), name='api-products-list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='api-product-detail'), 
]