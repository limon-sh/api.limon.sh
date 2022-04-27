from rest_framework import serializers
from apps.user.models import Member, Team


class TeamMemberSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        source='user.name',
        read_only=True
    )
    email = serializers.EmailField(
        source='user.email',
        read_only=True
    )

    class Meta:
        model = Member
        fields = (
            'role',
            'name',
            'email'
        )
        extra_kwargs = {
            'role': {'required': False}
        }


class TeamSerializer(serializers.ModelSerializer):
    members = TeamMemberSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Team
        fields = (
            'name',
            'slug',
            'members'
        )
        extra_kwargs = {
            'name': {'required': False},
            'slug': {'required': False, 'read_only': True}
        }
