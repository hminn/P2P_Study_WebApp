from django.shortcuts import render
from django.urls import reverse_lazy
from datetime import date
from . import models
from django.views.generic import ListView

# Create your views here.


class ShowPenaltyView(ListView):
    template_name = "feedback.html"
    success_url = reverse_lazy("todos:feedback")

    def get(self, request):
        todo_list = models.TodoList.objects.all()
        filtered_list = todo_list.filter(user=request.user, created_date=date.today())
        nonchecked_count = len(filtered_list.filter(checked=False))
        unit_penalty = 1000
        total_penalty = int(nonchecked_count) * unit_penalty
        return render(
            request,
            "feedback.html",
            {"todo_list": filtered_list, "penalty": total_penalty},
        )
