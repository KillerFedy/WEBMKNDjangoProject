from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Products, Categories
from cart.forms import CartAddProductForm

def index(request):
    products = Products.objects.all()
    categories = Categories.objects.all()
    return render(request, 'shop/index.html', {'products':products, 'categories':categories})

def product_list(request, category_id):
    products = Products.objects.filter(category_id=category_id)
    categories = Categories.objects.all()
    return render(request, 'shop/index.html', {'products':products, 'categories':categories})

def product_detail(request, id, slug):
    product = get_object_or_404(Products, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/index.html', {'product': product, 'cart_product_form' : cart_product_form})
