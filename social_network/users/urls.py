from django.urls import path, include
from .views import login, registration, profile, logout, friends, add_friend, delete_friend


app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/<int:user_id>/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('friends/', friends, name='friends'),
    path('add_friend/<int:friend_id>/', add_friend, name='add_friend'),
    path('delete_friend/<int:friend_id>/', delete_friend, name='delete_friend'),
]

