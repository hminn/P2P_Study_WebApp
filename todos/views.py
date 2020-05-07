from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from . import models, forms
from users import models as user_models
from times import models as time_models
from django.views.generic import FormView, ListView
from calendar import HTMLCalendar
from datetime import datetime, timedelta, time, date
from django.utils.safestring import mark_safe
from .models import Event


class TodoListView(FormView):
    template_name = "todolist.html"
    form_class = forms.TodoForm
    success_url = reverse_lazy("todos:todolist")

    def get(self, request):
        todo_list = models.TodoList.objects.all()
        (user,) = user_models.User.objects.filter(username=request.user)
        check = user.times.filter(date=datetime.today()).count()
        filtered_list = todo_list.filter(user=request.user, created_date=date.today())
        form = forms.TodoForm()
        return render(
            request,
            "todolist.html",
            {"todo_list": filtered_list, "form": form, "submit_check": check},
        )

    def post(self, request, *args, **kwargs):

        # todo 추가 버튼에 대한 POST : todo 추가 작업 진행
        if "add-todo" in request.POST:
            form = self.get_form()
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

        # todo 삭제 버튼에 대한 POST : todo 삭제 작업 진행
        # Front-end에서 POST 요청 시,
        # 해당 버튼의 name이 request.POST의 key로,
        # 해당 버튼의 value는 name key의 value로 넘어온다.
        if "del-todo" in request.POST:
            todo_id = request.POST.get("del-todo")
            del_query = models.TodoList.objects.filter(id=todo_id)
            del_query.delete()

        if "submit" in request.POST:
            filtered_list = models.TodoList.objects.filter(
                user=request.user, created_date=date.today()
            )
            filtered_list.update(submit_check=True)
            time = time_models.Times(
                user=request.user,
                date=datetime.today(),
                to_do_submit=datetime.now().time(),
            )
            time.save()

        if "fix" in request.POST:
            filtered_list = models.TodoList.objects.filter(
                user=request.user, created_date=date.today(), submit_check=False,
            )
            filtered_list.update(submit_check=True)

        return HttpResponseRedirect(self.get_success_url())


class TimeTableView(FormView):
    template_name = "timetable.html"
    form_class = forms.TimeTaskForm
    success_url = reverse_lazy("todos:timetable")

    def get(self, request):
        todo_list = models.TodoList.objects.all()
        timetask_list = models.TimeTask.objects.all()
        filtered_list = todo_list.filter(
            user=request.user, created_date=date.today(), submit_check=True
        )
        filtered_one_list = timetask_list.filter(
            user=request.user, created_date=date.today(), part="one"
        )
        filtered_two_list = timetask_list.filter(
            user=request.user, created_date=date.today(), part="two"
        )
        filtered_three_list = timetask_list.filter(
            user=request.user, created_date=date.today(), part="three"
        )
        filtered_four_list = timetask_list.filter(
            user=request.user, created_date=date.today(), part="four"
        )
        filtered_five_list = timetask_list.filter(
            user=request.user, created_date=date.today(), part="five"
        )
        filtered_six_list = timetask_list.filter(
            user=request.user, created_date=date.today(), part="six"
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
                "part_four": filtered_four_list,
                "part_five": filtered_five_list,
                "part_six": filtered_six_list,
            },
        )

    def post(self, request, *args, **kwargs):
        print(dir(request.GET))
        todo_list = models.TodoList.objects.all()
        filtered_list = todo_list.filter(user=request.user, created_date=date.today())

        if "add-task" in request.POST:
            form = self.get_form()
            obj = form.save(commit=False)
            obj.user = request.user
            obj.part = request.POST.get("add-task")
            obj.save()

        if "del-task" in request.POST:
            task_id = request.POST.get("del-task")
            del_query = models.TimeTask.objects.filter(id=task_id)
            del_query.delete()

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


#############################


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # '일'을 td 태그로 변환하고 이벤트를 '일'순으로 필터
    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        d = ""
        for events in events_per_day:
            d += f"<li> {Event.title} </li>"
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul><button type='submit' name='date' value='{self.year},{self.month},{day}'> {d} </button> </ul></td>"
        return "<td></td>"

    # # '주'를 tr 태그로 변환
    def formatweek(self, theweek, events):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f"<tr> {week} </tr>"

    # # '월'을 테이블 태그로 변환
    # # 각 '월'과 '연'으로 이벤트 필터
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(
            start_time__year=self.year, start_time__month=self.month
        )
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, events)}\n"
        return cal


# 시도하였지만 실패한 부분
# def show_todo(request):
#     day = request.Get.get("show")
#     d = get_date(request.GET.get("day", None))
#     show_day = datetime(d.year, d.month, day)
#     return render(request, "cal.html", {"show_day": show_day, "day": day})
class CalendarView(ListView):
    model = Event
    template_name = "calendar.html"
    success_url = reverse_lazy("todos:calendar")

    def get_success_url(self):
        # """Return the URL to redirect to after processing a valid form."""
        # if not self.success_url:
        #    raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return str(self.success_url)  # success_url may be laz

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # use today's date for the calendar
        d = get_date(self.request.GET.get("day", None))
        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)
        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        return context

    def post(self, request, *args, **kwargs):
        if "date" in request.GET:
            year, month, day = request.POST.get("date").split(",")
        return HttpResponseRedirect(self.get_success_url())


# 현재 달력을 보고 있는 시점의 시간을 반환
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return datetime.date(year, month, day=1)
    return datetime.today()
