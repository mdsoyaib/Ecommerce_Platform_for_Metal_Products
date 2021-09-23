from ironapp.views import About, Cart, Chechkout, Contact, Gallery, Index, My_account, Shop, Shop_details, Wishlist
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('about', About.as_view(), name="about"),
    path('cart', Cart.as_view(), name="cart"),
    path('checkout', Chechkout.as_view(), name="checkout"),
    path('contact', Contact.as_view(), name="contact"),
    path('gallery', Gallery.as_view(), name="gallery"),
    path('my_account', My_account.as_view(), name="my_account"),
    path('shop_details', Shop_details.as_view(), name="shop_details"),
    path('shop', Shop.as_view(), name="shop"),
    path('wishlist', Wishlist.as_view(), name="wishlist")
]
