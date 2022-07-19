from django import forms
from django.forms import ModelForm
from .models import Task, TaskGroup

class TaskGroupForm(ModelForm):
    class Meta:
        model = TaskGroup
        fields = ('organisation', 'title', 'deadline',)
        labels = {
            'organisation': 'Organisation',
            'title': 'Title',
            'deadline': 'Deadline',
        }
        widgets = {
            'organisation': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Organisation Name'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Project Title'}),
            'deadline': forms.DateInput(attrs={'type': 'datetime-local', 'class': 'form-control', 'placeholder':'Choose the deadline date'}, format="%Y-%m-%dT%H:%M"),
        }

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('taskgroup', 'title', 'complete',)
        labels = {
            'taskgroup': 'Taskgroup',
            'title': 'Title',
            'complete': 'Complete',
        }
        widgets = {
            'taskgroup': forms.Select(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Task Title'}),
        }