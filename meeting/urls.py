from django.urls import path
from . import views

app_name = 'meeting'

urlpatterns = [
    path('meeting/', views.meeting, name="meeting"),
    path('meeting/add_meeting/', views.add_meeting, name="add-meeting"),
    path('meeting/update_meeting/<meeting_id>', views.update_meeting, name="update-meeting"),
    path('meeting/delete_meeting/<meeting_id>', views.delete_meeting, name="delete-meeting"),
]