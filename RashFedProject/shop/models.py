from tabnanny import verbose
from unicodedata import category
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name='Продукт')
    category = models.CharField(max_length=50, verbose_name='Категория')
    subcategory = models.CharField(max_length=50, verbose_name='Подкатегория')
    price = models.PositiveSmallIntegerField(verbose_name="Цена")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['-price']

class Categories(models.Model):
    name = models.CharField(max_length=50, verbose_name="Категория")
    subcategory = models.CharField(max_length=50, verbose_name="Подкатегория")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['subcategory']