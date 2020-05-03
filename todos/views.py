from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from datetime import date
from . import models, forms
from django.views.generic import ListView, TemplateView, FormView


class TodoListView(ListView):
    model = models.TodoList
    template_name = "todos.html"
    context_object_name = "todos"


class TodoListingView(FormView):
    template_name = "todos.html"
    form_class = forms.TodoForm
    success_url = reverse_lazy("todos:base")

    def get(self, request):
        todo_list = models.TodoList.objects.all()
        filtered_list = todo_list.filter(user=request.user, created_date=date.today())
        form = forms.TodoForm()
        return render(request, "todos.html", {"todo_list": filtered_list, "form": form})

    def post(self, request, *args, **kwargs):

        # todo 추가 버튼에 대한 POST : todo 추가 작업 진행
        if "add-todo" in request.POST:
            form = self.get_form()
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

        # todo 삭제 버튼에 대한 POST : todo 삭제 작업 진행
        # Front-end에서 POST 요청 시,
        # 해당 버튼의 name이 request.POST의 key로,
        # 해당 버튼의 value는 name key의 value로 넘어온다.
        if "del-todo" in request.POST:
            todo_id = request.POST.get("del-todo")
            del_query = models.TodoList.objects.filter(id=todo_id)
            del_query.delete()
            return HttpResponseRedirect(self.get_success_url())
