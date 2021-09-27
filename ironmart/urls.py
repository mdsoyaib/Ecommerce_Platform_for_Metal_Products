from ironapp.views import About, Cart, Chechkout, Contact, Gallery, Index, My_account, Shop, Shop_details, Wishlist, Search, Signup, Activate
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('about', About.as_view(), name="about"),
    path('cart', Cart.as_view(), name="cart"),
    path('checkout', Chechkout.as_view(), name="checkout"),
    path('contact', Contact.as_view(), name="contact"),
    path('gallery', Gallery.as_view(), name="gallery"),
    path('my_account', My_account.as_view(), name="my_account"),
    path('shop_details/<int:pk>', Shop_details.as_view(), name="shop_details"),
    path('shop', Shop.as_view(), name="shop"),
    path('search/', Search.as_view()),
    path('wishlist', Wishlist.as_view(), name="wishlist"),
    path('signup/', Signup.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', Activate.as_view(), name='activate'),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
