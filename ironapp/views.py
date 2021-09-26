from ironapp.models import Category, Product, Blog, Website_Info
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
        web_info = Website_Info.objects.all()
        return render(request, 'contact-us.html', {'web_info': web_info})

class Gallery(View):
    def get(self, request):
        gallery = Product.objects.all()
        return render(request, 'gallery.html', {'gallery': gallery})

class Index(View):
    def get(self, request):
        product = Product.objects.all().order_by("-id")
        blog = Blog.objects.all().order_by("-id")
        return render(request, 'index.html', {'blog': blog, 'product': product})

class My_account(View):
    def get(self, request):
        return render(request, 'my-account.html')

class Shop_details(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        return render(request, 'shop-detail.html', {'p': product})

class Shop(View):
    def get(self, request):
        category = Category.objects.all()
        categoryID = request.GET.get('category')
        if categoryID:
            product = Product.get_all_products_by_category_id(categoryID)
        else:
            product = Product.objects.all().order_by('-id')
        return render(request, 'shop.html', {'product': product, 'category': category})

class Wishlist(View):
    def get(self, request):
        return render(request, 'wishlist.html')


class Footer(View):
    def get(self, request):
        web_info = Website_Info.objects.all()
        return render(request, 'footer.html', {'web_info': web_info})
