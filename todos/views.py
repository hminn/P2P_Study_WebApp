from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from datetime import date
from . import models, forms
from django.views.generic import ListView, TemplateView, FormView


class TodoListView(FormView):
    template_name = "todos.html"
    form_class = forms.TodoForm
    success_url = reverse_lazy("todos:todos")

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


class TimeTableView(FormView):
    template_name = "timetable.html"
    form_class = forms.TimeTaskForm
    success_url = reverse_lazy("todos:timetable")

    def get(self, request):
        todo_list = models.TodoList.objects.all()
        timetask_list = models.TimeTask.objects.all()
        filtered_list = todo_list.filter(user=request.user, created_date=date.today())
        filtered_one_list = timetask_list.filter(
            user=request.user, created_date=date.today(), part="one"
        )
        filtered_two_list = timetask_list.filter(
            user=request.user, created_date=date.today(), part="two"
        )
        filtered_three_list = timetask_list.filter(
            user=request.user, created_date=date.today(), part="three"
        )
        form = forms.TodoForm()
        return render(
            request,
            "timetable.html",
            {
                "todo_list": filtered_list,
                "form": form,
                "part_one": filtered_one_list,
                "part_two": filtered_two_list,
                "part_three": filtered_three_list,
            },
        )

    def post(self, request, *args, **kwargs):
        todo_list = models.TodoList.objects.all()
        filtered_list = todo_list.filter(user=request.user, created_date=date.today())

        if "add-task" in request.POST:
            form = self.get_form()
            obj = form.save(commit=False)
            obj.user = request.user
            obj.part = request.POST.get("add-task")
            obj.save()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

        if "del-task" in request.POST:
            task_id = request.POST.get("del-task")
            del_query = models.TimeTask.objects.filter(id=task_id)
            del_query.delete()
            return HttpResponseRedirect(self.get_success_url())

        # Cheked Save 버튼에 대한 작업 : cheked data를 저장하는 작업 진행
        # Save 버튼에 대한 POST인지 확인
        # Checked List 여부를 확인
        # 존재한다면 각각의 id에 맞는 TodoList의 Checked에 True 값 대입
        # 존재하지 않는다면 모든 TodoList의 Checked에 False 값 대입

        if "save" in request.POST:
            checked_id = request.POST.getlist("check-todo")
            if "check-todo" in request.POST:
                for filtered_object in filtered_list:
                    if str(filtered_object.id) in checked_id:
                        filtered_object.checked = True
                    else:
                        filtered_object.checked = False
                    filtered_object.save()
            else:
                filtered_list.update(checked=False)

        return HttpResponseRedirect(self.get_success_url())
