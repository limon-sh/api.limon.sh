from rest_framework import serializers
from apps.cluster.models import Cluster


class ClusterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cluster
        fields = (
            'name',
            'project',
        )
