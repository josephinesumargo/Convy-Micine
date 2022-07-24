from django.urls import path
from . import views
from .views import IndexView

app_name = 'group'

urlpatterns = [
    path('', views.group, name="group"),
    path('all/', views.all_group, name="all-group"),
    path('group-add/', views.add_group, name="add-group"),
    path('group-update/<group_id>', views.update_group, name="update-group"),
    path('group-delete/<group_id>', views.delete_group, name="delete-group"),
    path('<group_id>/announcement/', views.group_announcement, name="announcement"),
    path('announcement/', views.all_announcement, name="all-announcement"),
    path('announcement-add/', views.add_announcement, name="add-announcement"),
    path('announcement-update/<announcement_id>', views.update_announcement, name="update-announcement"),
    path('announcement-delete/<announcement_id>', views.delete_announcement, name="delete-announcement"),
    path('<group_id>/meeting/', views.group_meeting, name="meeting"),
    path('meeting-add/', views.add_meeting, name="add-meeting"),
    path('meeting-update/<meeting_id>', views.update_meeting, name="update-meeting"),
    path('meeting-delete/<meeting_id>', views.delete_meeting, name="delete-meeting"),
    path('<group_id>/taskgroup-list/', views.list_taskgroup, name="taskgroup-list"),
    path('taskgroup-add/', views.add_taskgroup, name="taskgroup-add"),
    path('taskgroup-update/<taskgroup_id>', views.update_taskgroup, name="taskgroup-update"),
    path('taskgroup-delete/<taskgroup_id>', views.delete_taskgroup, name="taskgroup-delete"),
    path('task-list/<int:pk>/', views.TaskList.as_view(), name="task-list"),
    path('task-add/', views.add_task, name="task-add"),
    path('task-update/<int:pk>/', views.EditTask.as_view(), name="task-update"),
    path('task-delete/<int:pk>/', views.DeleteTask.as_view(), name="task-delete"),
    path('documents/<group_id>/', IndexView.as_view(), name='index'),
]