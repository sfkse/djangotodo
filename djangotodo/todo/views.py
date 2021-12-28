from django.shortcuts import render


def listTodo(request):
    return render(request, 'todo/index.html')
