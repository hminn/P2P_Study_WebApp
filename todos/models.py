from django.db import models
from core.models import TimeStampedModel
from typing import Iterable


class ListField(models.TextField):
    """
    A custom Django field to represent lists as comma separated strings
    """

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop("token", ",")
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["token"] = self.token
        return name, path, args, kwargs

    def to_python(self, value):
        class SubList(list):
            def __init__(self, token, *args):
                self.token = token
                super().__init__(*args)

            def __str__(self):
                return self.token.join(self)

        if isinstance(value, list):
            return value
        if value is None:
            return SubList(self.token)
        return SubList(self.token, value.split(self.token))

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        if not value:
            return
        assert isinstance(value, Iterable)
        return self.token.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class TodoList(TimeStampedModel):
    """ TodoList Model Definition """

    todo_array = ListField()
    user = models.ForeignKey(
        "users.User", related_name="todolists", on_delete=models.CASCADE
    )
    checked = models.BooleanField(default=False)
    submit_check = models.BooleanField(default=False)


class WeekTask(TimeStampedModel):
    week_index = models.PositiveIntegerField()
    task_array = ListField()


class WeekPlan(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="weekplans", on_delete=models.CASCADE
    )
    week_index = models.PositiveIntegerField()
    weekplan_array = ListField()
