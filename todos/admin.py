from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.TodoList)
class TodoListAdmin(admin.ModelAdmin):
    pass


@admin.register(models.WeekTask)
class WeekTaskAdmin(admin.ModelAdmin):
    pass


@admin.register(models.WeekPlan)
class WeekPlanAdmin(admin.ModelAdmin):
    pass
