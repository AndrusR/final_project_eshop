from django.contrib import admin
from .models import Category, Product, Order, ShoppingCart, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ShoppingCart)
admin.site.register(Review)

