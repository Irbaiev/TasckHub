from django.contrib import admin

from accounts.models import CustomUser, FriendRequest

admin.site.register(CustomUser)
admin.site.register(FriendRequest)
