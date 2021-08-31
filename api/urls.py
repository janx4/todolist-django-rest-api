from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api'),
    path('task-list', views.task_list, name='api-task-list'),
    path('task-detail/<int:pk>', views.task_detail, name="api-task-detail"),
    path('task-create', views.task_create, name="api-task-create"),
    path('task-update/<int:pk>', views.task_update, name="api-task-update"),
    path('task-delete/<int:pk>', views.task_delete, name="api-task-delete"),

]
