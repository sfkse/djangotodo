from django import forms


class TodoForm(forms.Form):
    desription_attr = {
        'class': 'form-control form-control-lg border-0 add-todo-input bg-transparent rounded',
        'placeholder': 'Add new...'
    }

    due_attr = {
        'id': 'example',
        'class': 'form-control',
        'placeholder': 'Select date',
        'type': 'date'
    }
    description = forms.CharField(max_length=200, widget=forms.TextInput(attrs=desription_attr))
    due_date = forms.DateField(widget=forms.DateInput(attrs=due_attr))
