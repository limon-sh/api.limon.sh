from rest_framework import serializers
from apps.project.models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = (
            'name',
            'slug',
            'product'
        )
        extra_kwargs = {
            'name': {'required': False},
            'slug': {'required': False, 'read_only': True}
        }
