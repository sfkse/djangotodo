from django.urls import path
from .views import listTodo

urlpatterns = [
    path('', listTodo, name='list')
]
