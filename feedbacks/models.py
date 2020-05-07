from django.db import models
from core import models as core_models
from users import models as user_models


class Feedback(core_models.TimeStampedModel):

    """ Feedback Model Definition """

    user = models.ForeignKey(
        user_models.User, related_name="feedbacks", on_delete=models.CASCADE
    )
    contents = models.TextField(default="", blank=True)
    submit_check = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.created}"
