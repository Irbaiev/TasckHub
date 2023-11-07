from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model

from tasks.forms import ProjectForm, EditProjectForm
from tasks.models import Tasks, Project

User = get_user_model()


def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {"projects": projects})



def task_detail(request, pk):
    project = get_object_or_404(Project, id=pk)
    tasks = Tasks.objects.filter(project=project)
    return render(request, 'detail.html', {'project': project, 'tasks': tasks})



def createproject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user  
            project.save()
            return redirect('index')  
    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})



def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = EditProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=pk)  # Перенаправляем на страницу с деталями проекта
    else:
        form = EditProjectForm(instance=project)

    return render(request, 'edit_project.html', {'form': form, 'project': project})



def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('index')  # Перенаправляем на страницу с проектами или другую целевую страницу

    return render(request, 'delete_project.html', {'project': project})



def user_profile(request, username):
    user = request.user

    projects = Project.objects.filter(author=user)
    
    return render(request, 'profile.html', {'user': user, 'projects': projects})