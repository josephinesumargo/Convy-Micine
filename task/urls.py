from re import A
from django.urls import path
from . import views

app_name='task'

urlpatterns = [
    path('taskgroup-list/', views.list_taskgroup, name="taskgroup-list"),
    path('taskgroup-add/', views.add_taskgroup, name="taskgroup-add"),
    path('taskgroup-update/<taskgroup_id>', views.update_taskgroup, name="taskgroup-update"),
    path('taskgroup-delete/<taskgroup_id>', views.delete_taskgroup, name="taskgroup-delete"),
    path('task-list/<taskgroup_id>', views.list_task, name="task-list"),
    path('task-add/', views.add_task, name="task-add"),
    path('task-update/<task_id>', views.update_task, name="task-update"),
    path('task-delete/<task_id>', views.delete_task, name="task-delete"),
]