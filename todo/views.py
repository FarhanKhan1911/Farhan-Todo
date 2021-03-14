from django.shortcuts import render,redirect
from .forms import TODOform
from .models import TODO
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def add(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOform(request.POST)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("main")
        else:
            return render (request,'index.html',context={'form': form}) 

def home(request):
    return render (request,'home1.html')

@login_required(login_url='login')
def main(request):
    if request.user.is_authenticated:
        user = request.user    
        todos = TODO.objects.filter(user = user)
        return render (request,'main.html',context={'todos': todos})

def delete_todo(request , id):
    TODO.objects.get(pk = id).delete()
    return redirect('main')

def change_status(request , id , status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('main')

