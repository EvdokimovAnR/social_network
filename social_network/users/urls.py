from django.urls import path, include
from .views import login, registration, profile, logout


app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/<int:user_id>/', profile, name='profile'),
    path('logout/', logout, name='logout')
]

