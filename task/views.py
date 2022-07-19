from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from task.forms import TaskGroupForm, TaskForm
from task.models import Task, TaskGroup

# Create your views here.
def list_taskgroup(request):
    taskgroup_list = TaskGroup.objects.filter(user__pk = request.user.id)
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


def list_task(request, taskgroup_id):
    task_list = Task.objects.filter(taskgroup__pk = taskgroup_id)
    return render(request, 'task/task_list.html', {
        'task_list': task_list
	})

def add_task(request):
	submitted = False
	if request.method == "POST":
		form = TaskForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			task = form.save(commit=False)
			task.user = request.user
			task.save()
			return redirect('task:taskgroup-list')	
	else:
		form = TaskForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'task/task_add.html', {'form':form, 'submitted':submitted})

def update_task(request, task_id):
	task = Task.objects.get(pk=task_id)
	form = TaskForm(request.POST or None, request.FILES or None, instance=task)
	if form.is_valid():
		form.save()
		return redirect('task:taskgroup-list')

	return render(request, 'task/task_update.html', 
		{'task': task,
		'form':form})

def delete_task(request, task_id):
	task = Task.objects.get(pk=task_id)
	task.delete()
	return redirect('task:taskgroup-list')