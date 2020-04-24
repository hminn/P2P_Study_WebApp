from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    Custom_UserAdmin = (UserAdmin.fieldsets[0], UserAdmin.fieldsets[1])
    fieldsets = Custom_UserAdmin + (
        (
            "Custom profile",
            {"fields": ("avatar", "gender", "bio", "homepage", "birthdate",)},
        ),
    )
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )
