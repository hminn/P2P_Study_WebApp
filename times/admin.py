from django.contrib import admin
from . import models


@admin.register(models.Times)
class TimesAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date",
        "to_do_submit",
        "arrive_submit",
        "feedback_submit",
    )
