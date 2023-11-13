from django.urls import path, re_path
from accounts.views import Singup
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from . import views

urlpatterns = [
    path("registration/", Singup.as_view(), name="signup"),
    path("profile/<str:username>/", views.user_profile, name="user_profile"),
    path("profile/edit-profile/<int:pk>/", views.edit_profile, name="edit-profile"),
    path("add-friends", views.add_friends, name="add-friend"),
    path("add-friends/<int:id>", views.send_request, name="add_friends"),
    path("accept/<int:id>", views.accept_request, name="accept_friends"),
    path("password-change/", PasswordChangeView.as_view(), name="password_change"),
    path(
        "password-change/done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]
