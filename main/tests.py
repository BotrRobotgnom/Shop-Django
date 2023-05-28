from django.test import TestCase
from .models import User

class UserTests(TestCase):
    def test_create_user(self):
        username = 'testuser'
        password = 'testpassword'
        user = User.objects.create(username=username, password=password)
        self.assertEqual(user.username, username)
        self.assertEqual(user.password, password)