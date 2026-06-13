from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):

    USER_TYPES = (
        ("employer", "کارفرما"),
        ("job_seeker", "متقاضی کار"),
    )

    username = None

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=11,
        unique=True
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email