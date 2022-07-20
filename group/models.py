import os
from django.utils import timezone
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

class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=225, blank=False)
    body = models.TextField(blank=True)
    published = models.DateTimeField(default=timezone.now)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

class FileHandler(models.Model):
    title = models.CharField(max_length=200)
    file_upload = models.FileField(upload_to='file_path')

    def __str__(self):
        return str(self.file_upload)

def file_path(instance, filename):
    path="groups/"
    format= "uploaded-" + filename
    return os.path.join(path, format)