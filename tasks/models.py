from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    name = models.CharField(max_length=250)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.name
    
   

class Tasks(models.Model):
    project = models.ForeignKey(Project, null=True ,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    content = models.TextField()


    def __str__(self) -> str:
        return f"Проект{self.project}, Название {self.name}"

# class ProjectTasks(models.Model):
#     Project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return self.Project.name

    






