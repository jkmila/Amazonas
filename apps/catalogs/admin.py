from django.contrib import admin
from apps.catalogs.models import Product, Category, Comment

#para mostrar a administração dos produtos na pagina do administrador
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)