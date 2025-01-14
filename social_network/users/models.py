from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):
    username = models.CharField(max_length=128, unique=True)
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    telephone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='users_images', blank=True, null=True)


    def __str__(self):
        return self.username
