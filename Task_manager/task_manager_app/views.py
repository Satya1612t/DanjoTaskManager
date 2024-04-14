from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import User, Task
from .forms import UserForm, TaskForm
from .utils import make_response_from_query_sets
from django.contrib.auth.decorators import login_required

@login_required(login_url='clogin')
def home(request):
    users = User.objects.all()
    tasks_by_user = {}
    for user in users:
        tasks_by_user[user] = Task.objects.filter(user=user)

    return render(request, 'index.html', {'tasks_by_user': tasks_by_user})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("! ! ! ! ! login failed ! ! ! ! ! ")
    return render(request, 'custom_login.html')

def Add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'Add_user.html', {'form': form})

def Add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()

    users = User.objects.all()
    return render(request, 'Add_task.html', {'form': form, 'users': users})

def export_users_xls(request):
    users =User.objects.all()
    data=[]
    for user in users:
        tasks=Task.objects.filter(user=user)
        for task in tasks:
            data.append({
                'User ID': user.id,
                'Name': user.name,
                'Email': user.email,
                'Mobile': user.mobile,
                'Task Detail': task.task_detail,
                'Task Type': task.get_task_type_display(),
            })

    column_names = ('User ID', 'Name', 'Email', 'Mobile', 'Task Detail', 'Task Type')
    response = make_response_from_query_sets(data, column_names, 'xls')
    response['Content-Disposition'] = 'attachment; filename=users_with_tasks.xls'
    return response

def logout_user(request):
    logout(request)
    return redirect('home')