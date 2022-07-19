from django.urls import path
from . import views

app_name = 'group'

urlpatterns = [
    path('group/', views.group, name="group"),
    path('group-add/', views.add_group, name="add-group"),
    path('group-update/<group_id>', views.update_group, name="update-group"),
    path('group-delete/<group_id>', views.delete_group, name="delete-group"),
]