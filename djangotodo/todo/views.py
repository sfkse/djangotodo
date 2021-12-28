from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Todo
from django import forms
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


def editTodo(request, id):
    todo_item = get_object_or_404(Todo, id=id)
    todo = TodoForm()
    todo.fields['description'].widget.attrs.update({'placeholder': 'Update...', 'value': todo_item.description})
    todo.fields['due_date'].widget.attrs.update({'value': todo_item.due_date})
    context = {
        'form': todo
    }

    if request.method == 'POST':
        todo = TodoForm(request.POST)
        if todo.is_valid():
            add_todo = Todo()
            add_todo.description = todo.cleaned_data['description']
            add_todo.due_date = todo.cleaned_data['due_date']
            add_todo.save()
            return HttpResponseRedirect("/")
    return render(request, 'todo/edit-todo.html', context)
