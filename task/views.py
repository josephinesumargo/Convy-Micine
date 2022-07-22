from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy

from task.forms import TaskGroupForm, TaskForm
from task.models import Task, TaskGroup

from django.views import generic

# Create your views here.
def list_taskgroup(request):
    taskgroup_list = TaskGroup.objects.filter(group__members__username = request.user)
    return render(request, 'task/taskgroup_list.html', {
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
			return redirect('task:taskgroup-list')	
	else:
		form = TaskGroupForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'task/taskgroup_add.html', {'form':form, 'submitted':submitted})

def update_taskgroup(request, taskgroup_id):
	taskgroup = TaskGroup.objects.get(pk=taskgroup_id)
	form = TaskGroupForm(request.POST or None, request.FILES or None, instance=taskgroup)
	if form.is_valid():
		form.save()
		return redirect('task:taskgroup-list')

	return render(request, 'task/taskgroup_update.html', 
		{'taskgroup': taskgroup,
		'form':form})

def delete_taskgroup(request, taskgroup_id):
	taskgroup = TaskGroup.objects.get(pk=taskgroup_id)
	taskgroup.delete()
	return redirect('task:taskgroup-list')

class TaskList(generic.ListView):
	model = Task
	template_name = 'task/task_list.html'

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
			return redirect('task:taskgroup-list')	
	else:
		form = TaskForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'task/task_add.html', {'form':form, 'submitted':submitted})

class EditTask(generic.UpdateView):
	model = Task
	fields = ["taskgroup", "title", "complete"]
	template_name = "task/task_update.html"	
	success_url = reverse_lazy("task:taskgroup-list")

class DeleteTask(generic.DeleteView):
    model = Task
    template_name = "task/task_delete.html"
    success_url = reverse_lazy("task:taskgroup-list")