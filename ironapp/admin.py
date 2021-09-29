from django.contrib import admin
from .models import Category, CustomUser, Product, Blog, Website_Info

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
    list_editable = ("original_price", "discount_price", 'status')


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