from django.shortcuts import render
from datetime import date
from . import models
from django.views.generic import ListView, TemplateView


class TodoListView(ListView):
    model = models.TodoList
    template_name = "todos.html"
    context_object_name = "todos"


class TodoListingView(TemplateView):
    def get(self, request):
        template_name = "todos.html"
        todo_list = models.TodoList.objects.all()
        filtered_list = todo_list.filter(user=request.user, created_date=date.today())
        return render(request, template_name, {"todo_list": filtered_list})
