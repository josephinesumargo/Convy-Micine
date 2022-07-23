from django.shortcuts import render
from group.models import Announcement
from meeting.models import Meeting
from django.utils import timezone
from task.models import TaskGroup

# Create your views here.
def dashboard(request):
    announcement = Announcement.objects.filter(group__members__username=request.user)
    meeting = Meeting.objects.filter(group__members__username=request.user)
    upcomingmeeting = meeting.filter(meeting_date__gt = timezone.now())
    taskgroup = TaskGroup.objects.filter(group__members__username=request.user)
    return render(request, 'dashboard/dashboard.html', {
        'announcement': announcement,
        'upcomingmeeting': upcomingmeeting,
        'taskgroup': taskgroup,
    })