from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('calendar/', include('convy_calendar.urls')),
    path('group/', include('group.urls')),
    path('meeting/', include('meeting.urls')),
    path('task/', include('task.urls')),
]
