from django.contrib import admin

from .models import Products
from .models import Categories

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'subcategory', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subcategory')
    list_display_links = ('id', 'name', 'subcategory')
    search_fields = ('id', 'name', 'subcategory')

admin.site.register(Products, ProductsAdmin)
admin.site.register(Categories, CategoriesAdmin)
