from django.contrib import admin

from tasks.models import Tasks, Project, TaskCategory

admin.site.register(Tasks)
admin.site.register(Project)
admin.site.register(TaskCategory)
