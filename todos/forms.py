from django import forms
from .models import TodoList


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = [
            "contents",
        ]
