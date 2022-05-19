from django.contrib import admin

from apps.cluster.models import Cluster


@admin.register(Cluster)
class MachineAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at'
    )
