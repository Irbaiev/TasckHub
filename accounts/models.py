from django.db import models
from django.contrib.auth.models import AbstractUser


class FollowerCount(models.Model):
    follower = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.user


class CustomUser(AbstractUser):
    friends = models.ManyToManyField("self", blank=True)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        CustomUser, related_name="from_user", on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        CustomUser, related_name="to_user", on_delete=models.CASCADE
    )
