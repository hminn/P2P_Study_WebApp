from django.db import models
from core.models import TimeStampedModel


class TodoList(TimeStampedModel):
    """ TodoList Model Definition """

    contents = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        "users.User", related_name="todolists", on_delete=models.CASCADE
    )
    checked = models.BooleanField(default=False)
    submit_check = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)


class WeekTask(TimeStampedModel):
    week_index = models.PositiveIntegerField()
    contents = models.TextField(null=True, blank=True)


class WeekPlan(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="weekplans", on_delete=models.CASCADE
    )
    week_index = models.PositiveIntegerField()
    contents = models.TextField(null=True, blank=True)
