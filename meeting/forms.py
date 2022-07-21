from django import forms
from django.forms import ModelForm
from .models import Meeting

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ('group', 'agenda', 'meeting_date', 'location', 'meeting_link', 'meeting_minutes')
        labels = {
            'group': 'Group',
            'agenda': 'Agenda',
            'meeting_date': 'Meeting Date',
            'location': 'Location',
            'meeting_link': 'Meeting Link',
            'meeting_minutes': 'Meeting Minutes',
        }
        widgets = {
            'group': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Organisation Name'}),
            'agenda': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Project Title'}),
            'meeting_date': forms.DateInput(attrs={"type": "datetime-local", "class": "form-control"}, format="%Y-%m-%dT%H:%M"),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Organisation Name'}),
            'meeting_link': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Enter Your Organisation Name'}),
            'meeting_minutes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Organisation Name'})
        }