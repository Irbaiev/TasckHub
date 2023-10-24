from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.forms import RegisterUserForm


class Singup(CreateView):
    form_class = RegisterUserForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        # Сохраняем пользователя и возвращаем успешный HTTP ответ
        self.object = form.save()
        return super().form_valid(form)