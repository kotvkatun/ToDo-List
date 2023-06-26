from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """
    User model

    """

    username = models.CharField(name="username", max_length=20, unique=True)
    password = models.CharField(max_length=20, name="password")

    def __str__(self):
        """
        Magic method for model representation in Django Admin

        Returns:
            _type_: str
        """
        return f"User {self.username}"
