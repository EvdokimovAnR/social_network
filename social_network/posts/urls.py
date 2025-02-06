from django.urls import path
from .views import index, comment_add, all_posts, user_posts

app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('comment/add/', comment_add, name='comment_add'),
    path('all/posts/', all_posts, name='all_posts'),
    path('user/posts/', user_posts, name='user_posts'),
    ]