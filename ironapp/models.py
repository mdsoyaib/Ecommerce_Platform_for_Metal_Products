from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    unit=(
    ('feet', 'feet'),
    ('kg', 'kg'),
    ('pcs', 'pcs')   
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    original_price = models.PositiveIntegerField(max_length=12)
    discount_price = models.PositiveIntegerField(max_length=12)
    product_details = models.TextField(max_length=300)
    stock = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    unit = models.CharField(max_length=10, choices=unit)
    photo = models.ImageField(upload_to= 'uploads/product')
    featured = models.BooleanField()
    best_seller =models.BooleanField()

class Blog(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to= 'uploads/video')
    details = models.TextField(max_length=500)

class Website_Info(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    address = models.TextField(max_length=100)

    

