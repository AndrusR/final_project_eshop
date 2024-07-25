from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<str:category_name>', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('lease/', views.lease, name='lease'),

    path('product/<int:pk>/', views.product_detail, name="product"),

]
