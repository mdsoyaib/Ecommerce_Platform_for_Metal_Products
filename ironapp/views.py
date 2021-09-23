from django.shortcuts import render
from django.views import View

# Create your views here.
class About(View):
    def get(self, request):
        return render(request, 'about.html')

class Cart(View):
    def get(self, request):
        return render(request, 'cart.html')

class Chechkout(View):
    def get(self, request):
        return render(request, 'checkout.html')

class Contact(View):
    def get(self, request):
        return render(request, 'contact-us.html')

class Gallery(View):
    def get(self, request):
        return render(request, 'gallery.html')

class Index(View):
    def get(self, request):
        return render(request, 'index.html')

class My_account(View):
    def get(self, request):
        return render(request, 'my-account.html')

class Shop_details(View):
    def get(self, request):
        return render(request, 'shop-detail.html')

class Shop(View):
    def get(self, request):
        return render(request, 'shop.html')

class Wishlist(View):
    def get(self, request):
        return render(request, 'wishlist.html')
