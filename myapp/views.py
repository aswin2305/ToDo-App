from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm, TaskForm
from .models import Task
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.username}! You have successfully logged in.')  # ✅ correct usage
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard_view(request):
    return render(request, 'dashboard.html')
@login_required
def add_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the task to the current user
            task.save()
            return redirect('view_task')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

@login_required
def view_task_view(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'view_task.html', {'tasks': tasks})


@login_required
def update_task_view(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view_task')
    return render(request, 'update_task.html', {'form': form, 'task': task})


@login_required
def delete_task_view(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('view_task')

