from rest_framework import serializers

from apps.user.models import User


class UserCacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'first_name',
            'last_name',
            'email',
            'is_active'
        )
