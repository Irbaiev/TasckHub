from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={"class": "w-full mt-2 px-4 py-2 rounded-xl"}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "w-full mt-2 px-4 py-2 rounded-xl"}),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "w-full mt-2 px-4 py-2 rounded-xl"}),
    )
    password2 = forms.CharField(
        label="Повтор пароля",
        widget=forms.PasswordInput(attrs={"class": "w-full mt-2 px-4 py-2 rounded-xl"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
