from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Product, Order, ShippingInfo, ShoppingCart


class BasicViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name="Shipwreck")
        self.product = Product.objects.create(
            name="Old Oil Tanker",
            price=100000.00,
            description="A great piece of metal",
            image='path/to/image.jpg',
            stock_quantity=10,
            category=self.category
        )

    def test_home_view(self):
        """Test the home view."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_view(self):
        """Test the about view."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Jet skis')
        self.assertEqual(category.name, 'Jet skis')
        self.assertEqual(str(category), 'Jet skis')

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Jet skis')

    def test_product_creation(self):
        product = Product.objects.create(
            name='Kawasaki',
            price=999.99,
            description='Very good jet skis!',
            image='media/product/kawasaki.jpg',
            stock_quantity=10,
            category=self.category
        )
        self.assertEqual(product.name, 'Kawasaki')
        self.assertEqual(product.price, 999.99)
        self.assertEqual(product.description, 'Very good jet skis!')
        self.assertEqual(product.image, 'media/product/kawasaki.jpg')
        self.assertEqual(product.stock_quantity, 10)
        self.assertEqual(product.category, self.category)
        self.assertEqual(str(product), 'Kawasaki')

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Jet skis')
        self.product = Product.objects.create(
            name='Kawasaki',
            price=999.99,
            description='Very good jet skis!',
            image='media/product/kawasaki.jpg',
            stock_quantity=10,
            category=self.category
        )
        self.cart_item = ShoppingCart.objects.create(user=self.user, product=self.product, quantity=1, total_price=999.99)
        self.shipping_info = ShippingInfo.objects.create(
            full_name='John Doe',
            email='john@example.com',
            address='123 Main St',
            city='Anytown',
            phone='1234567890',
            country='Country',
            index='12345'
        )

    def test_order_creation(self):
        order = Order.objects.create(
            user=self.user,
            number='ORDER123',
            shipping_info=self.shipping_info,
            shopping_cart=self.cart_item
        )
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.number, 'ORDER123')
        self.assertFalse(order.completed)
        self.assertEqual(order.shipping_info, self.shipping_info)
        self.assertEqual(order.shopping_cart, self.cart_item)
        self.assertIn('Order ORDER123 is False.', str(order))
