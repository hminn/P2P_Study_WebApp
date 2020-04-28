from django.db import models
from core.models import TimeStampedModel

# Create your models here.


class Penalty(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="penalties", on_delete=models.CASCADE
    )
    total = models.PositiveIntegerField(default=0)
    today = models.PositiveIntegerField(default=0)
