from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    CART = 'cart'
    COMPLETED = 'completed'
    STATUS_CHOICES = [
        (CART, 'Cart'),
        (COMPLETED, 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=CART)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
