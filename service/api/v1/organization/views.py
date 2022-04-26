from rest_framework import viewsets
from apps.organization.models import Organization
from .serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    list:
        organization list

        List of organizations.

    retrieve:
        organization detail

        Details of organization.

    create:
        organization create

        Create a new organization.

    update:
        organization update

        Update an organization.

    partial_update:
        organization partial update

        Update and organization partially.

    destroy:
        organization destroy

        Destroy an organization.
    """

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.prefetch_related(
        'members'
    ).prefetch_related(
        'members__user'
    )
