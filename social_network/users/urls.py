from django.urls import path, include
from .views import login, registration, profile, logout, friends, add_friend, delete_friend, accept_friend_request, reject_friend_request, send_friend_request


app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/<int:user_id>/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('friends/', friends, name='friends'),
    path('add_friend/<int:friend_id>/', add_friend, name='add_friend'),
    path('delete_friend/<int:friend_id>/', delete_friend, name='delete_friend'),
    path('send_friend_request/<int:user_id>/', send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:request_id>/', accept_friend_request, name='accept_friend_request'),
    path('reject_friend_request/<int:request_id>/', reject_friend_request, name='reject_friend_request'),


]

