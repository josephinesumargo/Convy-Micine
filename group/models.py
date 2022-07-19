from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Group(models.Model):
    category = models.CharField(max_length=63, blank=False)
    title = models.CharField(max_length=63, blank=False)
    members = models.ManyToManyField(User)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title + " - " + self.category