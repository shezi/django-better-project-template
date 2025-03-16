from django.contrib import admin

from . import models


@admin.register(models.User)
class Admin(admin.ModelAdmin):

    list_display = ("email", "is_active", "is_staff", "is_superuser")

    # if you want a password field, you'll have to do a bit of work: https://github.com/django/django/blob/main/django/contrib/auth/admin.py#L75
