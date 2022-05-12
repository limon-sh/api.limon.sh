from rest_framework import serializers
from settings import base as settings
from apps.user.models import Member
from apps.organization.models import Organization
from libs.validators import ValidateFileSize, ValidateFileExtension


class OrganizationMemberSerializer(serializers.ModelSerializer):
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


class OrganizationSerializer(serializers.ModelSerializer):
    members = OrganizationMemberSerializer(
        many=True,
        read_only=True
    )

    logo = serializers.ImageField(required=False,
                                  allow_null=True,
                                  validators=[ValidateFileSize(settings.IMAGE_UPLOAD_MAX_SIZE),
                                              ValidateFileExtension(settings.ALLOWED_IMAGE_EXTENSIONS)])

    class Meta:
        model = Organization
        fields = (
            'name',
            'slug',
            'members',
            'logo'
        )
        extra_kwargs = {
            'name': {'required': False},
            'slug': {'required': False, 'read_only': True}
        }
