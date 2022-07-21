from datetime import datetime
from django.db import models
from group.models import Group
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    # meeting schedule need to be added to calendars
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=1) # group to be changed to Foreign Key
    agenda = models.CharField(max_length=225, blank=False)
    meeting_date = models.DateTimeField()
    location = models.CharField(max_length=225, blank=True)
    meeting_link = models.URLField(max_length=225, null=True)
    meeting_minutes = models.TextField(blank=True)

    def __str__(self):
        return self.agenda
