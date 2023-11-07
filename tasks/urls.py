from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:pk>/', views.task_detail, name='project_detail'),
    path('create-project', views.createproject, name='createproject'),
    path('project/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('project/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('profile/<str:username>', views.user_profile, name='user_profile')

]