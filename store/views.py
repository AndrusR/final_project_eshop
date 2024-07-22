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


# Product Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'views templates/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'views templates/product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm()
    return render(request, 'views templates/product_form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'views templates/product_form.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product-list')
    return render(request, 'views templates/product_confirm_delete.html', {'product': product})
