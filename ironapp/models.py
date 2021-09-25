from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
        
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
    unit = models.CharField(max_length=10, choices=unit)
    photo = models.ImageField(upload_to= 'uploads/product')
    status = models.BooleanField(default=True)
    featured = models.BooleanField()
    best_seller =models.BooleanField()
    created_at = models.DateTimeField('date time created at', auto_now_add=True)
    updated_at = models.DateTimeField('date time updated at', auto_now=True)

class Blog(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to= 'uploads/video')
    details = models.TextField(max_length=500)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField('date time created at', auto_now_add=True)
    updated_at = models.DateTimeField('date time updated at', auto_now=True)

class Website_Info(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    address = models.TextField(max_length=100)
    active = models.BooleanField()
    created_at = models.DateTimeField('date time created at', auto_now_add=True)
    updated_at = models.DateTimeField('date time updated at', auto_now=True)

    

