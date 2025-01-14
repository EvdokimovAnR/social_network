from django.urls import path
from .views import chats, message

app_name = 'chats'

urlpatterns = [
    path('chats/', chats, name='chats'),
    path('message/<int:recipient_id>/', message, name='message'),

]
