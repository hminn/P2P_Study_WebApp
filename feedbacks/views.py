from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from . import models, forms
from times import models as time_models
from todos import models as todo_models
from users import models as user_models
from users import mixins
from django.views.generic import FormView
from datetime import datetime, time, date


class FeedbackView(mixins.LoggedInOnlyView, FormView):
    template_name = "feedback.html"
    form_class = forms.FeedbackForm
    success_url = reverse_lazy("feedbacks:feedback")

    def get(self, request):
        form = forms.FeedbackForm()
        all_user = user_models.User.objects.exclude(username=request.user)
        todo_list = todo_models.TodoList.objects.all()

        # TodoList 미이행 항목 개수 세기
        filtered_list = todo_list.filter(
            user=request.user, created_date=date.today(), submit_check=True
        )
        nonchecked_count = len(filtered_list.filter(checked=False))

        # TodoList 제출 시간 검사
        user_times = request.user.times.filter(date=datetime.today())
        time_rule = time(9)
        if user_times:
            late_submit = user_times[0].to_do_submit > time_rule
        else:
            late_submit = False

        # 벌금 계산
        unit_penalty = 1000
        total_penalty = (nonchecked_count + late_submit) * (unit_penalty)

        # Feedback 넘겨주기
        user_feedback = request.user.feedbacks.filter(created_date=datetime.today())
        if user_feedback:
            (user_feedback,) = user_feedback
            form.initial["contents"] = user_feedback.contents

        return render(
            request,
            "feedback.html",
            {
                "all_user": all_user,
                "todo_list": filtered_list,
                "penalty": total_penalty,
                "form": form,
                "feedback": user_feedback,
            },
        )

    def post(self, request, *args, **kwargs):

        if "penalty_check" in request.POST:
            user = user_models.User.objects.filter(username=request.user)
            if not user[0].penalty_checked:
                user.update(today_penalty=request.POST.get("penalty_check"))
                user[0].reset_penalty()
                user.update(penalty_checked=True)

        if "submit" in request.POST:
            form = self.get_form()
            obj = form.save(commit=False)
            user = request.user.feedbacks.filter(created_date=datetime.today())
            if user:
                user.update(contents=obj.contents, submit_check=True)
            else:
                obj.user = request.user
                obj.submit_check = True
                obj.save()

        if "fix" in request.POST:
            user = request.user
            user_feedback = user.feedbacks.filter(created_date=datetime.today())
            user_feedback.update(submit_check=False)

        return HttpResponseRedirect(self.get_success_url())


def avatar_detail(request, user_id):
    todo_list = todo_models.TodoList.objects.all()
    all_user = user_models.User.objects.exclude(username=request.user)

    # TodoList 미이행 항목 개수 세기
    filtered_list = todo_list.filter(
        user=user_id, created_date=date.today(), submit_check=True
    )
    nonchecked_count = len(filtered_list.filter(checked=False))

    # TodoList 제출 시간 검사
    user_times = time_models.Times.objects.filter(user=user_id, date=datetime.today())
    time_rule = time(9)
    if user_times:
        late_submit = user_times[0].to_do_submit > time_rule
    else:
        late_submit = False

    # 벌금 계산
    unit_penalty = 1000
    total_penalty = (nonchecked_count + late_submit) * (unit_penalty)

    # Feedback 넘겨주기
    user_feedback = models.Feedback.objects.filter(
        user=user_id, created_date=datetime.today()
    )
    if user_feedback:
        (user_feedback,) = user_feedback

    return render(
        request,
        "avatar_feedback.html",
        {
            "all_user": all_user,
            "todo_list": filtered_list,
            "penalty": total_penalty,
            "feedback": user_feedback,
        },
    )
