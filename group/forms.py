from django import forms
from django.forms import ModelForm
from .models import Group, Announcement

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('category', 'title', 'members',)

class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ('group', 'title', 'body', 'published',)