from django.shortcuts import render, redirect
from group.models import Group, Announcement
from group.forms import GroupForm, AnnouncementForm

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