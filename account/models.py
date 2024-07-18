from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=15 , unique=True)
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to="profile")
    user_bio = models.CharField(max_length=100 , blank=True , null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.phone_number