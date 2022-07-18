from django.db import models

from django.contrib.auth.models import User
from convy_calendar.models import Event, EventAbstract


class EventMember(EventAbstract):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_members")

    class Meta:
        unique_together = ["event", "user"]

    def __str__(self):
        return str(self.user)
