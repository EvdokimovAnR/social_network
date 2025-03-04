from django.db import models
from users.models import User


class Message(models.Model):
    sender = models.ForeignKey(to=User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(to=User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.recipient.username}'


