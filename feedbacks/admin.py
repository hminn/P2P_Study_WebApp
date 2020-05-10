from django.contrib import admin
from . import models


@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    fieldsets = (("Custom Inform", {"fields": ("contents", "user",)},),)

    list_display = (
        "user",
        "created_date",
    )
