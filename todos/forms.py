from django import forms
from .models import TodoList, TimeTask


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = [
            "contents",
        ]
        labels = {
            "contents": "",
        }
        widgets = {
            "contents": forms.TextInput(attrs={"placeholder": "Write what to do"}),
        }


class TimeTaskForm(forms.ModelForm):
    class Meta:
        model = TimeTask
        fields = [
            "contents",
        ]
        labels = {
            "contents": "",
        }
        widgets = {
            "contents": forms.TextInput(attrs={"placeholder": "Write what to do"}),
        }
