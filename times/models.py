from django.db import models
from core import models as core_models
from users import models as user_models


class Times(core_models.TimeStampedModel):

    """ Times Model Definition """

    user = models.ForeignKey(
        user_models.User, related_name="times", on_delete=models.CASCADE
    )
    date = models.DateField(auto_now=True, null=True)
    to_do_submit = models.TimeField(blank=True, null=True)
    arrive_submit = models.TimeField(blank=True, null=True)
    feedback_submit = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = "Time"
