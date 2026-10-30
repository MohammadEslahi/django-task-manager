from django.http import HttpResponse
from .models import Task
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task,id=task_id,user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title','').strip()
        if title:
            task.title = title
            task.save()
            return redirect('task_list')
    return render(request, 'tasks/edit_task.html', {'task':task})



    
    



@login_required
def add_task_form(request):
    return render(request, 'tasks/add_task.html')


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks':tasks})


@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title','').strip()

        if title:
            Task.objects.create(title=title, user=request.user)
            return redirect('task_list')

        return HttpResponse('Please enter a title.')

    return HttpResponse('Invalid request method.')



@login_required
def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        Task.objects.filter(id=task_id,user=request.user).delete()
        return redirect('task_list')
    return HttpResponse('Invalid request method.')