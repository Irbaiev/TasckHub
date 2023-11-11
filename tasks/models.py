from django.db import models
from accounts.models import CustomUser


class Project(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    content = models.TextField(default="Описание проекта...")

    def __str__(self) -> str:
        return f"Создатель {self.author}, Название {self.name}"


class Tasks(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    content = models.TextField(default="Описание задачи...")

    def __str__(self) -> str:
        return self.name


# class Project_tasks(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
#     tasks = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
