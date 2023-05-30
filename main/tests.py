from main.models import User, Product, Order
from django.test import TestCase, RequestFactory
from django.urls import reverse
from main.views import checkout

class MTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.product = Product.objects.create(name='Product 1', price=10.99, quantity=5)

    def test_user_model(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_product_model(self):
        self.assertEqual(str(self.product), 'Product 1')

    def test_order_add_item(self):
        order = Order.objects.create(user=self.user)
        order.add_item(self.product, quantity=3)
        self.assertEqual(order.items, {self.product: 3})

    def test_order_remove_item(self):
        order = Order.objects.create(user=self.user)
        order.add_item(self.product, quantity=3)
        order.remove_item(self.product)
        self.assertEqual(order.items, {})

