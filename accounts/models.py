from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    avatar = models.ImageField(null=True, blank = True, upload_to='./image/user-avatar', verbose_name='avatar')
    friends = models.ManyToManyField("self", blank=True)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        CustomUser, related_name="from_user", on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        CustomUser, related_name="to_user", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'От {self.from_user}, к {self.to_user}'