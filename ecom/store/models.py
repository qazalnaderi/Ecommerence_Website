from django.db import models
import datetime


# Category of products
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Costumer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.fname} {self.lname}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)


    objects = models.Manager()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    quantity = models.ImageField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
