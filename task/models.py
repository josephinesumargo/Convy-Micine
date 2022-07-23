from django.db import models
from django.contrib.auth.models import User
from group.models import Group

# Create your models here.
class TaskGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    deadline = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.title

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    taskgroup = models.ForeignKey(TaskGroup, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']