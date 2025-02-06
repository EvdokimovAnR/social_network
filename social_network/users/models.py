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


class FriendShip(models.Model):
    user = models.ForeignKey(to=User, related_name='friendships', on_delete=models.CASCADE)
    friend = models.ForeignKey(to=User, related_name='friend_of', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} is friends with {self.friend.username}"


class FriendRequest(models.Model):
    from_user = models.ForeignKey(to=User, related_name='sent_friend_request', on_delete=models.CASCADE)
    to_user = models.ForeignKey(to=User, related_name='received_friend_request', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.from_user.username} -> {self.to_user.username}"

