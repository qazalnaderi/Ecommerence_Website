from django.db import models
import datetime

#Category of products
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Costumer(models.Model):
    fname =models.CharField(max_length=50)
    lname =models.CharField(max_length=50)
    phone =models.IntegerField(max_length=12)
    email =models.EmailField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.fname} {self.lname}'
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default=1)
    description = models.CharField(max_length=200,default='',blank=True,null=True)
    image = models.ImageField(upload_to='uploads/product/')
    def __str__(self):
        return self.name
