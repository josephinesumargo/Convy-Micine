from django.urls import path

from . import views

app_name = "convy_calendar"


urlpatterns = [
    path("", views.CalendarView.as_view(), name="calendars"),
    path("event/new/", views.create_event, name="event_new"),
    path("event/<int:pk>/edit/", views.EventEdit.as_view(), name="event_edit"),
    path("event/<int:event_id>/details/", views.event_details, name="event-detail"),
    path("event/<int:pk>/delete/", views.EventDelete.as_view(), name="event_delete"),
    path("all-event-list/", views.AllEventsListView.as_view(), name="all_events"),
    path("running-event-list/",views.RunningEventsListView.as_view(), name="running_events"),
]