from django.shortcuts import render, redirect
from group.models import Group, Announcement
from group.forms import GroupForm, AnnouncementForm

# meeting
from meeting.models import Meeting
from meeting.forms import MeetingForm
from datetime import datetime

# document
from django.views.generic import TemplateView
from .models import FileHandler
from .forms import FileHandlerForm

# Create your views here.
def group(request):
    groups = Group.objects.all()
    return render(request, 'group/group.html', {
        'groups': groups,
   	})

def add_group(request):
	submitted = False
	if request.method == "POST":
		form = GroupForm(request.POST, request.FILES)
		if form.is_valid():
			group = form.save(commit=False)
			group.save()
			return redirect('group:group')	
	else:
		form = GroupForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'group/group_add.html', {'form':form, 'submitted':submitted})

def update_group(request, group_id):
	group = Group.objects.get(pk=group_id)
	form = GroupForm(request.POST or None, request.FILES or None, instance=group)
	if form.is_valid():
		form.save()
		return redirect('group:group')

	return render(request, 'group/group_update.html', 
		{'group': group,
		'form':form})

def delete_group(request, group_id):
	group = Group.objects.get(pk=group_id)
	group.delete()
	return redirect('group:group')

# announcement
def announcement(request, group_id):
	announcements = Announcement.objects.filter(group__pk = group_id)
	return render(request, 'group/announcement.html', {'announcements': announcements})

def add_announcement(request):
	submitted = False
	if request.method == "POST":
		form = AnnouncementForm(request.POST, request.FILES)
		if form.is_valid():
			announcement = form.save(commit=False)
			announcement.user = request.user
			announcement.save()
			return redirect('group:group')	# should be announcement
	else:
		form = AnnouncementForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'group/announcement_add.html', {'form':form, 'submitted':submitted})

def update_announcement(request, announcement_id):
	announcement = Announcement.objects.get(pk=announcement_id)
	form = AnnouncementForm(request.POST or None, request.FILES or None, instance=announcement)
	if form.is_valid():
		form.save()
		return redirect('group:group') # should be announcement

	return render(request, 'group/announcement_update.html', 
		{'announcement': announcement,
		'form':form})

def delete_announcement(request, announcement_id):
	announcement = Announcement.objects.get(pk=announcement_id)
	announcement.delete()
	return redirect('group:group') # should be announcement

# meeting
def group_meeting(request, group_id):
	meeting = Meeting.objects.get(group__pk = group_id)
	upcoming = meeting.filter(dates__gt = datetime.now())
	past = meeting.filter(dates__lte = datetime.now())
	return render(request, 'group/meeting.html',
		{
			'meeting': meeting,
			'upcoming': upcoming,
			'past': past,
		})

def add_meeting(request):
	submitted = False
	if request.method == "POST":
		form = MeetingForm(request.POST, request.FILES)
		if form.is_valid():
			meetings = form.save(commit=False)
			meetings.user = request.user # logged in user
			meetings.save()
			return redirect('group:group')	
	else:
		form = MeetingForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'group/meeting_add.html', {'form':form, 'submitted':submitted})

def update_meeting(request, meeting_id):
	meeting = Meeting.objects.get(pk=meeting_id)
	form = MeetingForm(request.POST or None, request.FILES or None, instance=meeting)
	if form.is_valid():
		form.save()
		return redirect('group:group')

	return render(request, 'meeting/update_meeting.html', 
		{'meeting': meeting,
		'form':form})

def delete_meeting(request, meeting_id):
	meeting = Meeting.objects.get(pk=meeting_id)
	meeting.delete()
	return redirect('group:group')

class IndexView(TemplateView):
    template_name = 'group/documents.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_files = FileHandler.objects.all()
        context = {'form':FileHandlerForm, 'get_files':get_files}
        return context
    
    def post(self, request, **kwargs):
        context = {}
        if request.method == 'POST':
            form = FileHandlerForm(request.POST, request.FILES)
            
            if form.is_valid():
                FileHandler.objects.get_or_create(file_upload=form.cleaned_data.get('file_upload'))

                return redirect('group:index')
            else:
                context['form'] = form
        else:
            context['form'] = form

        return redirect('group:index')