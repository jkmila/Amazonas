from django.urls import path
#importando uma view
from apps.catalogs.views import (
    products_list,
    product_detail,
    add_comment_to_product,
    comment_approve,
    comment_remove
)

#definindo um end point e definindo qual view será executada e passando um name
urlpatterns = [
    path('products/', products_list, name='products-list'),
    #20190810
    path('products/<int:pk>', product_detail, name='product-detail'),
    path('products/<int:pk>/comment', add_comment_to_product, name='add_comment_to_product'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    
]