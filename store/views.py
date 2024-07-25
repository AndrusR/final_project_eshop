from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, ShoppingCart, Order, ShippingInfo, ShoppingCart
from .forms import ProductForm, LoginForm, SignUpForm
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse


def home(request):
    return render(request, 'home.html',)


def category(request, category_name):
    # Grab the category from the url
    try:
        # Look Up The Category
        category = Category.objects.get(name=category_name)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, ("That Category Doesn't Exist..."))
        return redirect('home')


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product_detail.html', {'product': product})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def lease(request):
    return render(request, 'lease.html',)


def calculate_cart_totals(cart_items):
    total_quantity = sum(item.quantity for item in cart_items)
    total_price = sum(item.quantity * item.product.price for item in cart_items)
    return total_quantity, total_price


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        cart, created = ShoppingCart.objects.get_or_create(user=request.user, completed=False)
        cart_item, created = Product.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()

        return redirect('cart')  # Redirect to the cart page after adding the product

    return render(request, 'product_detail.html', {'product': product})


@method_decorator(login_required(login_url='/registration/login/'), name='dispatch')
class CartView(View):
    def get(self, request):
        cart_items = ShoppingCart.objects.filter(user=request.user)
        total_quantity, total_price = calculate_cart_totals(cart_items)
        return render(request, 'cart.html', {
            'cart': cart_items,
            'total_quantity': total_quantity,
            'total_price': total_price
        })


class OrderView(View):
    @method_decorator(login_required(login_url='/registration/login/'))
    def get(self, request):
        return render(request, 'order.html')

    @method_decorator(login_required(login_url='/registration/login/'))
    def post(self, request):
        full_name = request.POST['full_name']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        phone = request.POST['phone']
        country = request.POST['country']
        index = request.POST['index']

        cart_items = ShoppingCart.objects.filter(user=request.user)
        total_quantity, total_price = calculate_cart_totals(cart_items)

        shipping_info = ShippingInfo.objects.create(
            full_name=full_name,
            email=email,
            address=address,
            city=city,
            phone=phone,
            country=country,
            index=index
        )
        order = Order.objects.create(
            user=request.user,
            number='ORDER123',
            shipping_info=shipping_info,
            shopping_cart=cart_items.first()
        )

        return render(request, 'order_info.html', {
            'order': order,
            'order_items': cart_items,
            'total_quantity': total_quantity,
            'total_price': total_price,
        })



