from django.contrib import admin
from .models import User, FriendShip, FriendRequest


admin.site.register(User)
admin.site.register(FriendShip)
admin.site.register(FriendRequest)
