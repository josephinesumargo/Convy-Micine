from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    organisation = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    deadline = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.title

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    taskgroup = models.ForeignKey(TaskGroup, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']