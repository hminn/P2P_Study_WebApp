from django.db import models
from django.urls import reverse
from core.models import TimeStampedModel


class TodoList(TimeStampedModel):
    """ TodoList Model Definition """

    contents = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        "users.User", related_name="todolists", on_delete=models.CASCADE,
    )
    checked = models.BooleanField(default=False)
    submit_check = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)


class TimeTask(TimeStampedModel):
    """ TimeTask Model Definition """

    PART_ONE = "one"
    PART_TWO = "two"
    PART_THREE = "three"
    PART_FOUR = "four"
    PART_FIVE = "five"
    PART_SIX = "six"

    PART_CHOICES = (
        (PART_ONE, "One"),
        (PART_TWO, "Two"),
        (PART_THREE, "Three"),
        (PART_FOUR, "four"),
        (PART_FIVE, "five"),
        (PART_SIX, "six"),
    )
    contents = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        "users.User", related_name="timetasks", on_delete=models.CASCADE,
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


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse("edit", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
