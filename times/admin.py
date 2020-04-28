from django.contrib import admin
from . import models


@admin.register(models.Times)
class TimesAdmin(admin.ModelAdmin):

    pass
