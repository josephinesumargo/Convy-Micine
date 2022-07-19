from datetime import datetime
from django.db import models

# Create your models here.
class Meeting(models.Model):

    class UpcomingObjects(models.Manager):
        def get_queryset(self):
            if self.dates == datetime.now().date():
                return super().get_queryset().filter(end_time__gte=datetime.now().time())
                
            return super().get_queryset().filter(dates__gte = datetime.now().date())

    class PastObjects(models.Manager):
        def get_queryset(self):
            if self.dates == datetime.now().date():
                return super().get_queryset().filter(end_time__lt=datetime.now().time())
            
            return super().get_queryset().filter(dates__lt=datetime.now().date())

    # meeting schedule need to be added to calendars
    group = models.CharField(max_length=225) # group to be changed to Foreign Key
    agenda = models.CharField(max_length=225, blank=False)
    dates = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=225, blank=True)
    meeting_link = models.URLField(max_length=225, null=True)
    meeting_minutes = models.TextField(blank=True)
    objects = models.Manager()
    upcomingobjects = UpcomingObjects()
    pastobjects = PastObjects()

    class Meta:
        ordering = ('dates', '-start_time',)

    def __str__(self):
        return self.agenda
