from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, LoginForm, SignUpForm
from django.contrib import messages


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


def product(request, pk):
    products = Product.objects.get(id=pk)
    return render(request, 'category.html', {'products': products})


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



