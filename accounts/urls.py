from django.urls import path
from accounts.views import Singup

urlpatterns = [path("registration/", Singup.as_view(), name="signup")]
