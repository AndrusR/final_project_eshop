from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<str:category_name>', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('category/<str:category_name>', views.category, name="category"),

    path('product/<int:pk>/', views.product, name="product"),


    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('products/new/', views.product_create, name='product-create'),
    path('products/<int:pk>/edit/', views.product_update, name='product-update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product-delete'),
]
