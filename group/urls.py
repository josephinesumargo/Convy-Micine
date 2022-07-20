from django.urls import path
from . import views
from .views import IndexView

app_name = 'group'

urlpatterns = [
    path('group/', views.group, name="group"),
    path('group-add/', views.add_group, name="add-group"),
    path('group-update/<group_id>', views.update_group, name="update-group"),
    path('group-delete/<group_id>', views.delete_group, name="delete-group"),
    path('group/<group_id>/announcement/', views.announcement, name="announcement"),
    path('group/announcement-add/', views.add_announcement, name="add-announcement"),
    path('group/announcement-update/<announcement_id>', views.update_announcement, name="update-announcement"),
    path('group/announcement-delete/<announcement_id>', views.delete_announcement, name="delete-announcement"),
    path('group/<group_id>/meeting/', views.group_meeting, name="meeting"),
    path('group/meeting-add/', views.add_meeting, name="add-meeting"),
    path('group/meeting-update/<meeting_id>', views.update_meeting, name="update-meeting"),
    path('group/meeting-delete/<meeting_id>', views.delete_meeting, name="delete-meeting"),
    path('group/documents/', IndexView.as_view(), name='index'),
]