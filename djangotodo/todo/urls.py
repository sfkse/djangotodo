from django.urls import path
from .views import listTodo, editTodo

urlpatterns = [
    path('', listTodo, name='list'),
    path('edit/<int:id>', editTodo, name='edit')
]
