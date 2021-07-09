from django.contrib import admin as dj_admin
from django_neomodel import admin as neo_admin
from .models import Person


class PersonAdmin(dj_admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )

dj_admin.site.register(Person, PersonAdmin)
