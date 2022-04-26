from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Member, Team


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_active',
        'last_login'
    )
    fieldsets = (
        ('General', {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'password'
            )
        }),
        ('Advanced options', {
            'fields': (
                'is_active',
                'is_superuser',
                'is_staff',
                'created_at',
                'groups'
            ),
        }),
    )
    readonly_fields = (
        'created_at',
    )
    ordering = (
        '-created_at',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email'
    )
    list_filter = (
        'is_active',
        'is_staff'
    )


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'user_name',
        'user_email',
        'role',
        'created_at'
    )
    readonly_fields = (
        'created_at',
    )
    ordering = (
        '-created_at',
    )
    list_filter = (
        'role',
    )

    @staticmethod
    def user_name(obj) -> str:
        return obj.user.name

    user_name.short_description = 'User name'

    @staticmethod
    def user_email(obj) -> str:
        return obj.user.email

    user_email.short_description = 'User email'


class TeamMemberInline(admin.StackedInline):
    extra = 0
    model = Team.members.through


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
        'members_count'
    )
    inlines = (
        TeamMemberInline,
    )

