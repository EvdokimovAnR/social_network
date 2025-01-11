from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=128, unique=True)
    county = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    telephone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.URLField(blank=True, null=True)
    bio = models.TextField(max_length=2048, blank=True, null=True)

    def __str__(self):
        return self.username
