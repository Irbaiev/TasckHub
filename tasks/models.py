from django.db import models
from accounts.models import CustomUser


class Project(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    content = models.TextField(default="Описание проекта...")
    members = models.ManyToManyField(CustomUser, related_name="projects", blank=True)

    def __str__(self) -> str:
        return f"Создатель {self.author}, Название {self.name}"


class TaskCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    content = models.TextField(default="Описание задачи...")
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True)
    assigned_to = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"Проект {self.project}, название {self.name}, исполнитель {self.assigned_to}"
