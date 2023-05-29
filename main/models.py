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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    AWAIT = 'await'
    COMPLETED = 'completed'
    STATUS_CHOICES = (
        (AWAIT, 'Awaiting'),
        (COMPLETED, 'Completed'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=AWAIT)

    items = {}  # словник для зберігання продуктів та їх кількостей

    def add_item(self, product, quantity=1):
        print(product)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product):
        print(product)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        del self.items[product]

    def get_total_price(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total
