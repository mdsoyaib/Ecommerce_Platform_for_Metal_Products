from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

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
    name = models.CharField(max_length=255)
    original_price = models.PositiveIntegerField(max_length=12)
    discount_price = models.PositiveIntegerField(max_length=12)
    product_details = models.TextField()
    quantity = models.PositiveIntegerField(null=True, blank=True)
    unit = models.CharField(max_length=10, choices=unit)
    photo = models.ImageField(upload_to= 'uploads/product')
    status = models.BooleanField(default=True)
    featured = models.BooleanField()
    best_seller =models.BooleanField()
    created_at = models.DateTimeField('date time created at', auto_now_add=True)
    updated_at = models.DateTimeField('date time updated at', auto_now=True)


    def __str__(self):
        return self.name


    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all().order_by('-id')


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


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("user must have an email address")

        user = self.model(email=self.normalize_email(email), )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, default=None, null=True)
    last_name = models.CharField(max_length=255, default=None, null=True)

    email = models.EmailField(max_length=100, unique=True)

    username = None
    user_permissions = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    session_token = models.CharField(max_length=10, default=0)

    is_active = models.BooleanField(default=False)
    # a admin user; non super-user
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # a superuser

    phone = models.CharField(max_length=255, default=None, null=True, blank=True)
    address = models.TextField(default=None, null=True, blank=True)
    city = models.CharField(max_length=255, default=None, null=True, blank=True)
    state = models.CharField(max_length=255, default=None, null=True, blank=True)
    zip_code = models.CharField(max_length=255, default=None, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    profile_image = models.FileField(upload_to='uploads/user', null=True, blank=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    

#----------- for order -----------------

class Order(models.Model):
    status = (
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Canceled", "Canceled"),
        ("Delivered", "Delivered"),
    )
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    # user = models.EmailField(max_length=255, null=True, blank=True)
    order_date = models.DateField(auto_now_add=True, null=True, blank=True)
    order_time = models.TimeField(auto_now_add=True, null=True, blank=True)
    total_price = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending', choices=status, auto_created=True)
    created_at = models.DateTimeField('date time created at', auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField('date time updated at', auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.pk}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField('date time created at', auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField('date time updated at', auto_now=True, null=True, blank=True)


class BillingInfo(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    address= models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=50, null=True, blank=True)


# ----------------- for order end ------------------


class ContactForm(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length = 255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
