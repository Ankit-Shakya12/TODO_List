from django.shortcuts import render, redirect
from .models import toDolist
from datetime import datetime
# from django.utils import timezone

# Create your views here.
def to_do_list(request):
    if request.method == "POST":
        data = request.POST
        task = data.get('tasks')
        
        dtime = datetime.now()

        toDolist.objects.create(
            tasks = task,
            create_at = dtime,
        )
        return redirect('/')
    
    queryset= toDolist.objects.all()
    context= {'var': queryset}

    return render(request,"todolist/todolist.html",context)

def edit_task(request ,id):
    queryset = toDolist.objects.get(id=id)

    if request.method == "POST":
        dta = request.POST
        task = dta.get('tasks')
        dtime = datetime.now()

        queryset.tasks = task
        queryset.create_at = dtime
        queryset.save()

        return redirect('/')
    
    context = {'query':queryset}
    return render(request,"todolist/edit_task.html",context)
    
def complete_task(request , id ):
    queryset = toDolist.objects.get(id=id)
    queryset.complete = True
    queryset.save()
    return redirect('/')

def delete_task(request , id):
    queryset = toDolist.objects.get(id=id)
    queryset.delete()
    return redirect('/')