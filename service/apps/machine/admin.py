from django.contrib import admin

from apps.machine.models import Machine


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at'
    )
