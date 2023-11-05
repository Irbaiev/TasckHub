from django.shortcuts import render, get_object_or_404
from django.views import generic

from tasks.models import Tasks, Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {"projects": projects})


def task_detail(request, pk):
    project = get_object_or_404(Project, id=pk)
    tasks = Tasks.objects.filter(project=project)
    return render(request, 'detail.html', {'project': project, 'tasks': tasks})
