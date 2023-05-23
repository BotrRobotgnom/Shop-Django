from django.test import TestCase
from .models import User, Account

class UserTests(TestCase):
    def test_create_user(self):
        username = 'testuser'
        password = 'testpassword'
        user = User.objects.create(username=username, password=password)
        self.assertEqual(user.username, username)
        self.assertEqual(user.password, password)

class AccountTests(TestCase):
    def test_create_account(self):
        user = User.objects.create(username='testuser', password='testpassword')
        account_number = '1234567890'
        balance = 1000.0
        account = Account.objects.create(user=user, account_number=account_number, balance=balance)
        self.assertEqual(account.user, user)
        self.assertEqual(account.account_number, account_number)
        self.assertEqual(account.balance, balance)
