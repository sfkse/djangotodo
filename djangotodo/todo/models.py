from django.db import models


class Todo(models.Model):
    description = models.TextField(max_length=200, null=False)
    due_date = models.DateField(auto_now=False)
    created_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.description} {self.due_date} {self.completed}'
