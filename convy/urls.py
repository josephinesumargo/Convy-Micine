from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('calendar/', include('convy_calendar.urls')),
    path('group/', include('group.urls')),
    path('meeting/', include('meeting.urls')),
    path('task/', include('task.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)