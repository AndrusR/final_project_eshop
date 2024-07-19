from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


# Categories of Products
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50) # Name of the category

    def __str__(self):
        return self.name


# Categories of User
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False) # Allows the user to access the admin site.
    last_login = models.DateTimeField(blank=True, null=True) # A datetime of the user’s last login.

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# All of our Products
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    stock_quantity = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE) # Links the product to a category

    def __str__(self):
        return self.name


# Order represents the ready-to-purchase details by a user
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) # ForeignKey linking to the user who made the order
    order_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    status = models.BooleanField(default=False) # Status of the order, whether completed, pending etc.

    def __str__(self):
        return f'Your order {self.user_id} is {self.status}.'


# OrderItem represents a specific product added in an order
class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE) # ForeignKey linking to the order
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE) # ForeignKey linking to the product
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.product_id} x {self.quantity}'


# ShoppingCart represents a collection of products that a user intends to buy
class ShoppingCart(models.Model):
    shopping_cart_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self, shopping_cart_id=None):
        return f'Shopping cart {shopping_cart_id} for {self.user_id}'


# CartItem represents a specific product added to a ShoppingCart
class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    shopping_cart_id = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product_id} x {self.quantity}'


# Review represents feedback by a user about a product
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0) # Rating given by the user
    comment = models.TextField() # Comment added by the user
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Review on {self.product_id} by {self.user_id} on {self.review_date}.'

