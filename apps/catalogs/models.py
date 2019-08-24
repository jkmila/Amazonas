from django.db import models
from django.utils import timezone

#o produto é um modelo de django, o django sabe que ele deve ser salvo no banco de dados
#tabela: <nome_do_app>
class Product(models.Model):
    #campo texto com limite de caracteres
    description = models.CharField(max_length=100)
    #campo decimal, eh necessario definir o numero de caracters antes e depois da virgula
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    suggested_price = models.DecimalField(max_digits=10, decimal_places=2)
    #campo de imagem que pode ser nulo ou nao
    # o django vai criar a pasta img/products
    #se passar blank = true, ele permite criar o produto sem imagem
    image = models.ImageField(upload_to="imgs/products/", blank = True)
    # 1 = true 0 = false
    has_offer = models.BooleanField(default=False)
    # armazena data e hora
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def publish(self):
        
        self.published_at = timezone.now()
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text