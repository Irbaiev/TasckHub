from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.forms import RegisterUserForm

from accounts.models import CustomUser, FriendRequest
from accounts.forms import EditUserForm

from tasks.models import Project



class Singup(CreateView):
    form_class = RegisterUserForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        # Сохраняем пользователя и возвращаем успешный HTTP ответ
        self.object = form.save()
        return super().form_valid(form)
    

def user_profile(request, username):
    user = request.user
    projects = Project.objects.filter(author=user)

    return render(
        request,
        "profile.html",
        {
            "user": user,
            "projects": projects,
        },
    )

def add_friends(request):
    alluser = CustomUser.objects.exclude(username=request.user)
    fr = FriendRequest.objects.filter(to_user=request.user)
    return render(request, 'friends.html', {'alluser': alluser, 'fr':fr})


def send_request(request, id):
    from_user = request.user
    to_user = CustomUser.objects.get(id=id)
    frequest = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
    return redirect('index')

def accept_request(request, id):
    frequest = FriendRequest.objects.get(id=id)
    user1 = request.user
    user2 = frequest.from_user
    user1.friends.add(user2)
    user2.friends.add(user1)
    return redirect('index')


def edit_profile(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)

    if request.method == "POST":
        form = EditUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user_profile", username=user.username)
    else:
        form = EditUserForm(instance=user)

    return render(request, "edit_profile.html", {"form": form, "user": user})