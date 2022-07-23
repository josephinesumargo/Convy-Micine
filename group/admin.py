from django.contrib import admin
from .models import Group, Announcement, FileHandler

# Register your models here.
admin.site.register(Group)
admin.site.register(Announcement)
admin.site.register(FileHandler)