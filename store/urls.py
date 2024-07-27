from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<str:category_name>', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('lease/', views.lease, name='lease'),

    path('product/<int:pk>/', views.product, name="product"),


    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('order/', views.OrderView.as_view(), name='place_order'),
    path('orderinfo/<int:order_id>/', views.OrderInfoView.as_view(), name='order_info'),
]
