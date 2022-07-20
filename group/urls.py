from django.urls import path
from . import views

app_name = 'group'

urlpatterns = [
    path('group/', views.group, name="group"),
    path('group-add/', views.add_group, name="add-group"),
    path('group-update/<group_id>', views.update_group, name="update-group"),
    path('group-delete/<group_id>', views.delete_group, name="delete-group"),
    path('announcement/<group_id>', views.announcement, name="announcement"),
    path('announcement-add/', views.add_announcement, name="add-announcement"),
    path('announcement-update/<announcement_id>', views.update_announcement, name="update-announcement"),
    path('announcement-delete/<announcement_id>', views.delete_announcement, name="delete-announcement"),
]