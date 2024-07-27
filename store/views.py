from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, ShoppingCart, Order, ShippingInfo
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from the_weather.weather.views import get_weather


def home(request):
    weather_context = get_weather(request)
    return render(request, 'home.html', weather_context)


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


def product(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product_detail.html', {'product': product})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def lease(request):
    return render(request, 'lease.html',)


# Product Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def calculate_cart_totals(cart_items):
    total_quantity = sum(item.quantity for item in cart_items)
    total_price = sum(item.quantity * item.product.price for item in cart_items)
    return total_quantity, total_price


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


@method_decorator(login_required(login_url='/registration/login/'), name='dispatch')
class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not provided

        cart_item, created = ShoppingCart.objects.get_or_create(user=request.user, product=product)
        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity

        cart_item.save()

        # Redirect back to the product page with a success query parameter
        return redirect(f'/product/{product_id}/?added_to_cart=true')


@method_decorator(login_required(login_url='/registration/login/'), name='dispatch')
class RemoveFromCartView(View):
    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        cart_item = ShoppingCart.objects.get(user=request.user, product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        return redirect('cart')


class OrderView(View):
    def get(self, request):
        return render(request, 'order.html')

    def post(self, request):
        full_name = request.POST['full_name']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        phone = request.POST['phone']
        country = request.POST['country']
        index = request.POST['index']

        cart_items = ShoppingCart.objects.filter(user=request.user)
        if not cart_items.exists():
            messages.error(request, "Your cart is empty!")
            return redirect('cart')

        total_quantity, total_price = calculate_cart_totals(cart_items)

        # Create ShippingInfo
        shipping_info = ShippingInfo.objects.create(
            full_name=full_name,
            email=email,
            address=address,
            city=city,
            phone=phone,
            country=country,
            index=index
        )

        # Create Order
        order = Order.objects.create(
            user=request.user,
            number='ORDER123',  # Ideally, generate a unique order number
            shipping_info=shipping_info
        )

        # Associate cart items with the order
        for item in cart_items:
            item.order = order
            item.save()

        # Clear the cart
        cart_items.delete()

        # Redirect to the order info page
        return redirect('order_info', order_id=order.id)  # Pass order_id as argument


@method_decorator(login_required(login_url='/registration/login/'), name='dispatch')
class OrderInfoView(View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id, user=request.user)
        cart_items = ShoppingCart.objects.filter(order=order)
        total_quantity, total_price = calculate_cart_totals(cart_items)
        return render(request, 'order_info.html', {
            'order': order,
            'order_items': cart_items,
            'total_quantity': total_quantity,
            'total_price': total_price,
        })
