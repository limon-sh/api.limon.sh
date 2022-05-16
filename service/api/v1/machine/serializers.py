from rest_framework import serializers
from apps.machine.models import Machine


class MachineSerializer(serializers.ModelSerializer):

    cluster = serializers.UUIDField(
        allow_null=True,
        required=False
    )

    class Meta:
        model = Machine
        fields = (
            'uuid',
            'name',
            'project',
            'cluster',
        )
        extra_kwargs = {
            'name': {'required': False}
        }
