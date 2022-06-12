from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Categories

def index(request):
    products = Products.objects.all()
    categories = Categories.objects.all()
    return render(request, 'shop/index.html', {'products':products, 'categories':categories})

def get_product(request, category_id):
    products = Products.objects.filter(category_id=category_id)
    categories = Categories.objects.all()
    return render(request, 'shop/index.html', {'products':products, 'categories':categories})
