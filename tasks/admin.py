from django.contrib import admin

from tasks.models import Tasks, Project

admin.site.register(Tasks)
admin.site.register(Project)
# admin.site.register(ProjectTasks)
