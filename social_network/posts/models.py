from django.db import models
from users.models import User

class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts_images', blank=True, null=True)

    def __str__(self):
        return f'Post by {self.user.username} on {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'


class Comment(models.Model):
    post = models.ForeignKey(to=Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'