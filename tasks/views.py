from django.http import HttpResponse
from .models import Task
from django.shortcuts import render,redirect, get_object_or_404


def add_task_form(request):
    return render(request, 'tasks/add_task.html')



def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks':tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title','').strip()

        if title:
            Task.objects.create(title=title)
            return redirect('task_list')

        return HttpResponse('Please enter a title.')

    return HttpResponse('Invalid request method.')


def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        Task.objects.filter(id=task_id).delete()
        return redirect('task_list')
    return HttpResponse('Invalid request method.')