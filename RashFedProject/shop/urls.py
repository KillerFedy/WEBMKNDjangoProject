from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('category/<int:category_id>/', product_list),
]