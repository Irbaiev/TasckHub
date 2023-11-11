from django.contrib import admin

from accounts.models import FollowerCount, FriendRequest

admin.site.register(FollowerCount)
admin.site.register(FriendRequest)
