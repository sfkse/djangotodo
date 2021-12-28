from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Todo
from .forms import TodoForm


def listTodo(request):
    if request.method == 'POST':
        todo = TodoForm(request.POST)
        if todo.is_valid():
            add_todo = Todo()
            add_todo.description = todo.cleaned_data['description']
            add_todo.due_date = todo.cleaned_data['due_date']
            add_todo.save()
            todo = TodoForm()
            return HttpResponseRedirect("/")

    todo = TodoForm()
    todos = Todo.objects.all()
    context = {
        'todos': todos,
        'form': todo
    }
    return render(request, 'todo/index.html', context)
