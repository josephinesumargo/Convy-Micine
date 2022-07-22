from django.shortcuts import render, redirect
from group.models import Group, Announcement
from group.forms import GroupForm, AnnouncementForm

# meeting
from meeting.models import Meeting
from meeting.forms import MeetingForm
from django.utils import timezone

# task
from django.urls import reverse_lazy
from task.forms import TaskGroupForm, TaskForm
from task.models import Task, TaskGroup
from django.views import generic

# document
from django.views.generic import TemplateView
from .models import FileHandler
from .forms import FileHandlerForm

# Create your views here.
def group(request):
    groups = Group.objects.filter(members__username=request.user)
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
def all_announcement(request):
	announcement = Announcement.objects.all()
	return render(request, 'group/announcement.html', {'announcement': announcement})

def group_announcement(request, group_id):
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
    meeting = Meeting.objects.filter(group__pk = group_id)
    upcoming = meeting.filter(meeting_date__gt = timezone.now())
    past = meeting.filter(meeting_date__lte = timezone.now())
    return render(request, 'group/meeting.html', {
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

# task
def list_taskgroup(request, group_id):
    taskgroup_list = TaskGroup.objects.filter(group__pk = group_id)
    return render(request, 'group/taskgroup_list.html', {
        'taskgroup_list': taskgroup_list,
   	})

def add_taskgroup(request):
	submitted = False
	if request.method == "POST":
		form = TaskGroupForm(request.POST, request.FILES)
		if form.is_valid():
			taskgroup = form.save(commit=False)
			taskgroup.user = request.user # logged in user
			taskgroup.save()
			return redirect('group:taskgroup-list')	
	else:
		form = TaskGroupForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'group/taskgroup_add.html', {'form':form, 'submitted':submitted})

def update_taskgroup(request, taskgroup_id):
	taskgroup = TaskGroup.objects.get(pk=taskgroup_id)
	form = TaskGroupForm(request.POST or None, request.FILES or None, instance=taskgroup)
	if form.is_valid():
		form.save()
		return redirect('group:taskgroup-list')

	return render(request, 'group/taskgroup_update.html', 
		{'taskgroup': taskgroup,
		'form':form})

def delete_taskgroup(request, taskgroup_id):
	taskgroup = TaskGroup.objects.get(pk=taskgroup_id)
	taskgroup.delete()
	return redirect('group:taskgroup-list')

class TaskList(generic.ListView):
	model = Task
	template_name = 'group/task_list.html'

# def list_task(request, taskgroup_id):
#     task_list = Task.objects.filter(taskgroup__pk = taskgroup_id)
#     return render(request, 'task/task_list.html', {
#         'task_list': task_list
# 	})

def add_task(request):
	submitted = False
	if request.method == "POST":
		form = TaskForm(request.POST, request.FILES)
		if form.is_valid():
			task = form.save(commit=False)
			task.user = request.user # logged in user
			task.save()
			return redirect('group:taskgroup-list')	
	else:
		form = TaskForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'group/task_add.html', {'form':form, 'submitted':submitted})

class EditTask(generic.UpdateView):
	model = Task
	fields = ["taskgroup", "title", "complete"]
	template_name = "group/task_update.html"	
	success_url = reverse_lazy("group:taskgroup-list")

class DeleteTask(generic.DeleteView):
    model = Task
    template_name = "group/task_delete.html"
    success_url = reverse_lazy("group:taskgroup-list")

# documents
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