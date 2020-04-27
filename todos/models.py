from django.db import models
from django.contrib.postgres.fields import ArrayField
from core import TimeStampedModel

# Create your models here.


class TodoList(TimeStampedModel):
    """ TodoList Model Definition """

    todo_array = ArrayField(models.CharField(max_length=40, black=True,), size=10,)
    user = models.ForeignKey(
        "users.User", related_name="users", on_delete=models.CASCADE
    )
    checked = models.BooleanField(default=False)
    submit_check = models.BooleanField(default=False)


class WeekTask(TimeStampedModel):
    week_index = models.PositiveIntegerField()
    task_array = ArrayField(models.CharField(max_length=40, black=True,), blank=True,)


class WeekPlan(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="users", on_delete=models.CASCADE
    )
    week_index = models.PositiveIntegerField()
    weekplan_array = ArrayField(
        models.CharField(max_length=40, black=True,), blank=True,
    )
