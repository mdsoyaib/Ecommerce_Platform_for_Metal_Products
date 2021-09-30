from ironapp.cart import Cart
from ironapp.models import Category, Product, Blog, Website_Info, Order, OrderDetail, BillingInfo, ContactForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.contrib.auth.tokens import default_token_generator
from ironapp.forms import SignUpForm, CartAddProductForm
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.views.decorators.http import require_POST
from django.db.models import F

# Create your views here.
class About(View):
    def get(self, request):
        return render(request, 'about.html')

# ----------------for cart-----------------

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if product.quantity == 0:
        return redirect('cart_detail')
    else:

        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])

        return redirect('cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True,
        })
    return render(request, 'cart.html', {'cart': cart})

# ----------------for cart-----------------

#---------------for order-----------------

def checkout(request):
    cart = Cart(request)
    user = request.user
    if user.is_authenticated:
        return render(request, 'checkout.html', {'cart': cart})
    else:
        return redirect('login')


def insert_order(request):
    cart = Cart(request)
    if request.method == "POST":
        total_price = request.POST["total_price"]
        user = request.user

# -------------billing info-------------------
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        zip_code = request.POST['zip_code']
        phone = request.POST['phone']
        email = request.POST['email']

# -------------billing info------------------

        order = Order(total_price=total_price, customer=user)

        # print(order.id)

        billing = BillingInfo(first_name=first_name, last_name=last_name, address=address, zip_code=zip_code, phone=phone, order=order, customer=user, email=email)

        order.save()
        billing.save()
        cart.clear()

        for item in cart:
            product = item['product']
            quantity = item['quantity']
            price = item['total_price']
            order_details = OrderDetail(quantity=quantity, price=price, product=product, order=order)
            order_details.save()
            # find product by id
            # print(item)
            Product.objects.filter(id=item['id']).update(quantity=F('quantity')-item['quantity'])
            # update product qauntity old_qyt - cartqyt
    return redirect("order_history")

#------------------for order end ----------------


class OrderHistory(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            orders = Order.objects.filter().order_by('-id')
            return render(request, 'order_history.html', {'orders': orders})
        else:
            return redirect('login')


class CancelOrder(View):
    def post(self, request):
        id = request.POST['order_id']
        Order.objects.filter(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])





class Contact(View):
    def get(self, request):
        web_info = Website_Info.objects.all()
        return render(request, 'contact-us.html', {'web_info': web_info})
    
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        contact = ContactForm(name=name, email=email, subject=subject, message=message)
        contact.save()
        return redirect('contact')

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
        user = request.user
        if user.is_authenticated:
            return render(request, 'my-account.html')
        else:
            return redirect('login')

class Shop_details(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        cart_product_form = CartAddProductForm()
        return render(request, 'shop-detail.html', {'product': product, 'cart_product_form': cart_product_form})

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


class Search(View):
    def get(self, request):
        q = request.GET.get('q')
        product = Product.objects.filter(name__icontains=q).order_by('-id')
        return render(request, 'search.html', {'product': product})


class Header(View):
    def get(self, request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={
                'quantity': item['quantity'],
                'override': True,
            })
        return render(request, 'header.html', {'cart': cart})


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)

        customer_group, created = Group.objects.get_or_create(name='Customer')

        # print(SignUpForm)
        # print(form.fields)
        # print(form.errors.as_json())
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            customer_group.user_set.add(user)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'acc_active_sent.html')
        else:
            # form = SignUpForm()
            return render(request, 'signup.html', {'form': form})


class Activate(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_user_model()._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            # print(TypeError)
            # print(ValueError)
            # print(OverflowError)
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, 'acc_active_done.html')
        else:
            return render(request, 'acc_active_invalid.html')