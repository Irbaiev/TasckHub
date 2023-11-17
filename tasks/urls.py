from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("project/<int:pk>/", views.project_detail, name="project_detail"),
    path("create-project", views.createproject, name="createproject"),
    path("project/<int:pk>/delete/", views.delete_project, name="delete_project"),
    path("project/<int:pk>/edit/", views.edit_project, name="edit_project"),
    path("project/<int:pk>/create-tasks", views.create_task, name="create_tasks"),
    path("project/<int:pk>/create-tasks-category/", views.create_tasks_category, name="create_tasks_category"),
    path('project/<int:project_id>/edit-tasks-category/<int:category_id>/', views.edit_tasks_category, name='edit_tasks_category'),

]
