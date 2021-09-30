from django.contrib import admin
from .models import Category, CustomUser, Product, Blog, Website_Info, Order, OrderDetail, BillingInfo, ContactForm

# Register your models here.

@admin.register(Category)
class CategoryAmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_per_page = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "original_price", "discount_price", "quantity",
    "unit", "photo", "status", "featured", "best_seller")
    search_fields = ("name", "unit", "status", "featured", "best_seller")
    list_filter = ("category", "unit", "status", "featured", "best_seller")
    list_per_page = 10
    list_editable = ("original_price", "discount_price", 'status', 'quantity')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("name", "photo", "active")
    search_fields = ("name",)
    list_per_page = 10
    list_editable = ("active",)


@admin.register(Website_Info)
class Website_InfoAdmin(admin.ModelAdmin):
    list_display = ("phone", "email", "address", "active")


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'email', 'phone', 'city')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'order_time', 'total_price', 'status')
    search_fields = ('customer', 'order_date', 'order_time', 'status')
    list_filter = ('status',)
    # readonly_fields = ('buyer', 'order_date', 'order_time')
    list_per_page = 10


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    # readonly_fields = ('order', 'product', 'quantity', 'price')
    search_fields = ('order',)
    list_per_page = 10


@admin.register(BillingInfo)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'customer', 'first_name', 'last_name', 'email', 'phone', 'address', 'zip_code')
    search_fields = ('order', 'customer', 'first_name', 'last_name', 'phone', 'email')
    list_filter = ('order', 'customer', 'first_name', 'last_name', 'phone', 'city', 'state')
    list_per_page = 10


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email')
    list_per_page = 10