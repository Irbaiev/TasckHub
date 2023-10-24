from django.shortcuts import render
from tasks.models import Tasks, Project

def index(request):
    projects = Project.objects.all()

    return render(request, 'index.html', {"projects": projects})
