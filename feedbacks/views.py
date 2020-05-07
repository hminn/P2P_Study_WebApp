from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from . import models, forms
from todos import models as todo_models
from users import models as user_models
from django.views.generic import FormView
from datetime import datetime, time, date


class FeedbackView(FormView):
    template_name = "feedback.html"
    form_class = forms.FeedbackForm
    success_url = reverse_lazy("feedbacks:feedback")

    def get(self, request):
        form = forms.FeedbackForm()
        todo_list = todo_models.TodoList.objects.all()
        filtered_list = todo_list.filter(
            user=request.user, created_date=date.today(), submit_check=True
        )
        nonchecked_count = len(filtered_list.filter(checked=False))
        user_times = request.user.times.filter(date=datetime.today())
        time_rule = time(9)
        if user_times:
            late_submit = user_times[0].to_do_submit > time_rule
        else:
            late_submit = False
        unit_penalty = 1000
        total_penalty = (nonchecked_count + late_submit) * (unit_penalty)
        return render(
            request,
            "feedback.html",
            {"todo_list": filtered_list, "penalty": total_penalty, "form": form},
        )

    def post(self, request, *args, **kwargs):
        if "penalty_check" in request.POST:
            user = user_models.User.objects.filter(username=request.user)
            if not user[0].penalty_checked:
                user.update(today_penalty=request.POST.get("penalty_check"))
                user[0].reset_penalty()
                user.update(penalty_checked=True)
        if "submit" in request.POST:
            form = forms.FeedbackForm(request.POST, request.FILES)
            if form.is_valid():
                post = models.Feedback()
                post.contents = form.cleaned_data.get("feedback")
                post.user = request.user
                post.save()
            else:
                form = forms.FeedbackForm()

        return HttpResponseRedirect(self.get_success_url())
