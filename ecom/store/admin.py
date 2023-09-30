from django.contrib import admin
from .models import Costumer, Category, Product, Order

admin.site.register(Category)
admin.site.register(Costumer)
admin.site.register(Product)
admin.site.register(Order)
