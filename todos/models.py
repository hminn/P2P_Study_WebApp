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


class TimeTask(TimeStampedModel):
    """ TimeTask Model Definition """

    PART_ONE = "one"
    PART_TWO = "two"
    PART_KAKAO = "three"

    PART_CHOICES = (
        (PART_ONE, "One"),
        (PART_TWO, "Two"),
        (PART_KAKAO, "Three"),
    )
    contents = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        "users.User", related_name="timetasks", on_delete=models.CASCADE
    )
    checked = models.BooleanField(default=False)
    part = models.CharField(choices=PART_CHOICES, max_length=10, blank=True)
    created_date = models.DateField(auto_now_add=True)


class WeekTask(TimeStampedModel):
    week_index = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(
        "users.User", related_name="weektasks", on_delete=models.CASCADE, default=""
    )
    contents = models.TextField(null=True, blank=True)


class WeekPlan(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="weekplans", on_delete=models.CASCADE,
    )
    week_index = models.PositiveIntegerField(default=0)
    contents = models.TextField(null=True, blank=True)
