from rest_framework import viewsets

from apps.organization.models import Organization
from .serializers import OrganizationSerializer
from rest_framework import status
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.decorators import api_view


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

@api_view(['GET'])
def view_cached_data(request):
    if 'data' in cache:
        result = cache.get('data')
        return Response(result, status=status.HTTP_201_CREATED)
    else:
        data = Organization.objects.all()
        serializer = OrganizationSerializer(data, many=True)
        cache.set('data', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)