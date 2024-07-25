from django.db import models
from django.contrib.auth.models import User


# Categories of Products
class Category(models.Model):
    name = models.CharField(max_length=50)  # Name of the category

    def __str__(self):
        return self.name


# All of our Products
class Product(models.Model):
    name = models.CharField(max_length=250, help_text='Enter a name for the product')
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    description = models.CharField(max_length=250, default='', blank=True, null=True, help_text='Enter a description of the product')
    image = models.ImageField(upload_to='media/product/')
    stock_quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Links the product to a category

    def __str__(self):
        return self.name


# Order represents the ready-to-purchase details by a user
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)  # ForeignKey linking to the user who made the order
    number = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)  # Status of the order, whether completed, pending etc.
    shipping_info = models.ForeignKey("ShippingInfo", on_delete=models.CASCADE, null=True)
    shopping_cart = models.ForeignKey("ShoppingCart", on_delete=models.CASCADE)

    def __str__(self):
        return f'Order {self.number} is {self.completed}.'


class ShippingInfo(models.Model):
    full_name = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=128, null=False)
    address = models.CharField(max_length=250, default='')
    city = models.CharField(max_length=32, default='')
    phone = models.CharField(max_length=16, default='')
    country = models.CharField(max_length=32, default='')
    index = models.CharField(max_length=32, default='')


# ShoppingCart represents a collection of products that a user intends to buy
class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Link the cart to a user
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return f'Shopping cart {self.id}.'


# Review represents feedback by a user about a product
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)  # Rating given by the user
    comment = models.TextField()  # Comment added by the user
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Review on {self.product} by {self.user} on {self.date}.'
