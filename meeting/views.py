from django.shortcuts import redirect, render

from meeting.forms import MeetingForm
from .models import Meeting

# Create your views here.
def meeting(request):
    meeting = Meeting.objects.all()
    upcoming = Meeting.upcomingobjects.all()
    past = Meeting.pastobjects.all()
    return render(request, 'meeting/meeting.html', {
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
			return redirect('meeting:meeting')	
	else:
		form = MeetingForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'meeting/add_meeting.html', {'form':form, 'submitted':submitted})

def update_meeting(request, meeting_id):
	meeting = Meeting.objects.get(pk=meeting_id)
	form = MeetingForm(request.POST or None, request.FILES or None, instance=meeting)
	if form.is_valid():
		form.save()
		return redirect('meeting:meeting')

	return render(request, 'meeting/update_meeting.html', 
		{'meeting': meeting,
		'form':form})

def delete_meeting(request, meeting_id):
	meeting = Meeting.objects.get(pk=meeting_id)
	meeting.delete()
	return redirect('meeting:meeting')