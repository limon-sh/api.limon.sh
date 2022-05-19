from rest_framework import viewsets
from apps.cluster.models import Cluster
from .serializers import ClusterSerializer


class ClusterViewSet(viewsets.ModelViewSet):
    """
    list:
        cluster list

        List of clusters.

    retrieve:
        cluster detail

        Details of cluster.

    create:
        cluster create

        Create a new cluster.

    update:
        cluster update

        Update a cluster.

    partial_update:
        cluster partial update

        Update a cluster partially.

    destroy:
        cluster destroy

        Destroy a cluster.
    """

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    serializer_class = ClusterSerializer
    queryset = Cluster.objects.all()
