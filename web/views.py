from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.contrib.auth.models import User
from .models import Todo



@login_required(login_url="login/")
def index(request):
    user = request.user
    todos = Todo.objects.filter(is_done=False, user=user)
    dones = Todo.objects.filter(is_done=True, user=user) 
    if request.method == 'POST':
        name = request.POST.get('name')
        Todo.objects.create(name=name, user=user)
        return redirect('web:index')
    else:
        context = {
            'todos': todos,
            'dones':dones
        }
        return render(request, 'web/index.html',  context=context)

def edit_todo(request, id):
    user = request.user
    todos = Todo.objects.filter(is_done=False, user=user)
    dones = Todo.objects.filter(is_done=True, user=user) 
    task = Todo.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        task.name=name
        task.save()
        return redirect('web:index')
    else:
        context = {
            'task':task,
            'todos': todos,
            'dones':dones
        }
        return render(request, 'web/index.html',  context=context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(request, username=username, password=password,) 

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('web:index'))
        else:
            context = {
                'error':True,
                'message':'Invalid email or password'
            }
            return render(request, 'web/login.html', context=context)
    else:
        return render(request, 'web/login.html')
    
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(
            first_name=first_name, 
            last_name=last_name,
            username=username,
            password=password,
        )
        user.save()
        return HttpResponseRedirect(reverse('web:login'))
    
    else:
        return render(request, 'web/register.html')
    
    
def logout(request):
   user = request.user
   auth_logout(request)
  
   return HttpResponseRedirect(reverse('web:index'))


@login_required(login_url='/login')
def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('web:index')


@login_required(login_url='/login')
def todo_done(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_done=True
    todo.save()
    
    return redirect('web:index')


