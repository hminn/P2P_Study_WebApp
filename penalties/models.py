from django.db import models
from core import TimeStampedModel

# Create your models here.


class Penalty(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="users", on_delete=models.CASCADE
    )
    total = models.PositiveIntegerField(default=0)
    today = models.PositiveIntegerField(default=0)
