from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """
    User model

    """
    email = models.EmailField(name="email")
    username = models.CharField(name="username", unique=True, max_length=30)
    password = models.CharField(name="password", max_length=100)

    def __str__(self):
        """
        Magic method for model representation in Django Admin

        Returns:
            _type_: str
        """
        return f"User {self.username}"
