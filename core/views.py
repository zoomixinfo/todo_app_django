from django.shortcuts import redirect, render
from . models import Todo

from .forms import TodoForm

def home(request):
    form = TodoForm()
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            form = TodoForm()
            return redirect('home')
    return render(request, 'home.html', {'form': form, 'todo': todos})
def update(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'update.html', {'form': form})
def delete(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'delete.html', {'todo': todo})

