from django import forms
from django.shortcuts import render, get_object_or_404, redirect


from tasks.forms import ProjectForm, EditProjectForm, TasksForm, EditTasksForm, TasksCategoryForm, EditTasksCategoryForm
from tasks.models import Tasks, Project, TaskCategory


def index(request):
    return render(request, "index.html")


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.tasks_set.all()  # Получаем все задачи проекта
    categories = TaskCategory.objects.all()  # Получаем все категории
    return render(request, 'project_detail.html', {'project': project, 'tasks': tasks, 'categories': categories})


def createproject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect("index")
    else:
        form = ProjectForm()

    return render(request, "create_project.html", {"form": form})


def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        form = EditProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect(
                "project_detail", pk=pk
            )  # Перенаправляем на страницу с деталями проекта
    else:
        form = EditProjectForm(instance=project)

    return render(request, "edit_project.html", {"form": form, "project": project})


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        project.delete()
        return redirect(
            "index"
        )  # Перенаправляем на страницу с проектами или другую целевую страницу

    return render(request, "delete_project.html", {"project": project})


def create_task(request, pk):
    if request.method == "POST":
        form = TasksForm(request.POST)
        if form.is_valid():
            project = get_object_or_404(Project, pk=pk)
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', pk=pk)
    else:
        form = TasksForm()

    return render(request, 'create_task.html', {'form': form})


def create_tasks_category(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        form = TasksCategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect("project_detail", pk=pk)
    else:
        form = TasksCategoryForm()
    return render(request, "create_tasks_category.html", {"form": form, "project": project})


def edit_tasks_category(request, category_id):
    category = get_object_or_404(TaskCategory, pk=category_id)
    tasks_in_category = Tasks.objects.filter(category=category)

    if request.method == "POST":
        formset = forms.inlineformset_factory(
            TaskCategory,
            Tasks,
            form=EditTasksForm,
            extra=0,  # Указывает, что не нужны дополнительные формы
            can_delete=False,  # Запрет на удаление существующих задач
        )
        formset = formset(request.POST, request.FILES, instance=category, queryset=tasks_in_category)

        if formset.is_valid():
            formset.save()
            return redirect('tasks_category_detail', pk=category_id)
    else:
        formset = forms.inlineformset_factory(
            TaskCategory,
            Tasks,
            form=EditTasksForm,
            extra=0,
            can_delete=False,
        )
        formset = formset(instance=category, queryset=tasks_in_category)

    return render(request, 'edit_tasks_category.html', {'formset': formset, 'category': category})