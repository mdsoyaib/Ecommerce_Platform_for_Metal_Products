from ironapp.views import About, Cart, Chechkout, Contact, Gallery, Index, My_account, Shop, Shop_details, Wishlist, Search, Signup, Activate, cart_detail, cart_add, cart_remove
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('about', About.as_view(), name="about"),
    # path('cart', Cart.as_view(), name="cart"),
    path('cart/', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
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
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name='password_reset_complete'),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
