from unicodedata import category
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    price = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.name