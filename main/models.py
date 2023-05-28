from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username