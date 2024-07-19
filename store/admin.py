from django.contrib import admin
from .models import Category, Product, Order, User, OrderItem, ShoppingCart, CartItem, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(OrderItem)
admin.site.register(ShoppingCart)
admin.site.register(CartItem)
admin.site.register(Review)
