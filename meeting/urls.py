from django.urls import path
from . import views

app_name = 'meeting'

urlpatterns = [
    path('', views.meeting, name="meeting"),
    path('add_meeting/', views.add_meeting, name="add-meeting"),
    path('update_meeting/<meeting_id>', views.update_meeting, name="update-meeting"),
    path('delete_meeting/<meeting_id>', views.delete_meeting, name="delete-meeting"),
]