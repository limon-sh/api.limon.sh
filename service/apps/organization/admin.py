from django.contrib import admin

from apps.organization.models import Organization


class OrganizationMemberInline(admin.StackedInline):
    extra = 0
    model = Organization.members.through


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'members_count',
        'created_at'
    )
    ordering = (
        'name',
    )
    search_fields = (
        'name',
    )
    readonly_fields = (
        'created_at',
    )
    inlines = (
        OrganizationMemberInline,
    )

    def get_exclude(self, request, obj=None):
        exclude_fields = super().get_exclude(request, obj) or []

        if not obj:
            return list(exclude_fields) + ['slug', 'created_at']

        return list(exclude_fields)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj) or []

        if not obj:
            return []

        return list(readonly_fields)
