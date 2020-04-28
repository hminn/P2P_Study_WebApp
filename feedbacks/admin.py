from django.contrib import admin
from . import models


@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    pass
