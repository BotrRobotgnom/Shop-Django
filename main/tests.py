from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

class RegistrationTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('main/registration.html')

    def test_registration_form(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')

    def test_registration(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse(''))
        self.assertTrue(User.objects.filter(username='testuser').exists())

class LoginTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login.html')
        self.username = 'testuser'
        self.password = 'testpassword'
        User.objects.create_user(username=self.username, password=self.password)

    def test_login_form(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse(''))
        self.assertTrue(response.client.session['_auth_user_id'])

    def test_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'invalidpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertFalse(response.client.session.get('_auth_user_id'))
