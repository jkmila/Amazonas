
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from apps.catalogs.models import Product, Comment
from apps.catalogs.forms import CommentForm

#criando a view
#a view vai receber a requisição, vai renderizar e vai passar o template
# def products_list(request):
#     return render(request, 'catalogs/products_list.html', {})

#criando uma lista e passando o contexto, o contexto é o que esta entre as chaves
def products_list(request):
    products = Product.objects.filter(published_at__isnull=False).order_by('description')
    return render(request, 'catalogs/products_list.html', {'products': products})

#20190810
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'catalogs/product_detail.html', {'product': product})

def add_comment_to_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product-detail', pk=product.pk)
    else:
        form = CommentForm()
    return render(request, 'catalogs/add_comment_to_product.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('product-detail', pk=comment.product.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('product-detail', pk=comment.product.pk)