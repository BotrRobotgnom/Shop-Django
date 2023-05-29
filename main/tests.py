from main.models import User, Product, Order
from django.contrib import messages
from django.test import TestCase, RequestFactory
from django.urls import reverse
from main.views import checkout

class ModelTestCase(TestCase):

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

    def test_order_get_total_price(self):
        order = Order.objects.create(user=self.user)
        order.add_item(self.product, quantity=2)
        total_price = self.product.price * 2
        self.assertEqual(order.get_total_price(), total_price)


class ViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_checkout_insufficient_quantity(self):
        request = self.factory.post(reverse('checkout'))
        request.user = self.user
        response = checkout(request)
        self.assertRedirects(response, reverse('cart'))
        self.assertContains(response, 'Insufficient quantity for product')

    def test_checkout_empty_cart(self):
        request = self.factory.post(reverse('checkout'))
        request.user = self.user
        messages.error(request, 'Error: You have not ordered anything')
        response = checkout(request)
        self.assertRedirects(response, reverse('cart'))
        self.assertContains(response, 'Error: You have not ordered anything')

    def test_checkout_not_authenticated(self):
        request = self.factory.post(reverse('checkout'))
        response = checkout(request)
        self.assertRedirects(response, reverse('login'))
        self.assertContains(response, 'Please log in.')

    def test_checkout_successful(self):
        # Create a sample order for the user
        order = Order.objects.create(user=self.user)
        request = self.factory.post(reverse('checkout'))
        request.user = self.user
        response = checkout(request)
        self.assertRedirects(response, '/')
        self.assertFalse(Order.objects.filter(user=self.user, status=Order.AWAIT).exists())
        self.assertTrue(Order.objects.filter(user=self.user, status=Order.COMPLETED).exists())
