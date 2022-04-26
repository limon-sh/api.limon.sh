from django.contrib import admin

from apps.project.models import Project


class ProjectTeamInline(admin.StackedInline):
    extra = 0
    model = Project.teams.through


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at'
    )
    inlines = (
        ProjectTeamInline,
    )
