from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect, render


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if username and password:
            if User.objects.filter(username=username).exists():
                return HttpResponse('Username already exists!')

            user = User.objects.create_user(
                username=username,
                password=password
            )

            login(request, user)
            return redirect('task_list')

        return HttpResponse('Please provide username and password.')

    return render(request, 'accounts/register.html')


