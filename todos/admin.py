from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.TodoList)
class TodoListAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Custom Inform",
            {"fields": ("contents", "user", "checked", "submit_check",)},
        ),
    )

    list_display = (
        "user",
        "checked",
        "submit_check",
        "created_date",
    )


@admin.register(models.TimeTask)
class TimeTaskAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Custom Inform", {"fields": ("contents", "user", "checked", "part",)},),
    )

    list_display = (
        "user",
        "checked",
        "created_date",
        "part",
    )
    pass


@admin.register(models.WeekTask)
class WeekTaskAdmin(admin.ModelAdmin):
    pass


@admin.register(models.WeekPlan)
class WeekPlanAdmin(admin.ModelAdmin):
    pass
