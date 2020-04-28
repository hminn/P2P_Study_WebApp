from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Penalty)
class PenaltyAdmin(admin.ModelAdmin):
    pass
