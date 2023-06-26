from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """
    User model

    """

    username = models.CharField(
        name="username", min_length=5, max_length=20, name="username", unique=True
    )
    password = models.CharField(min_length=6, max_length=20, name="password")

    def __str__(self):
        """
        Magic method for model representation in Django Admin

        Returns:
            _type_: str
        """
        return f"User {self.username}"
