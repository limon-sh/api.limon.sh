from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.organization.models import Organization
from apps.user.models import Team
from .serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    list:
        team list

        List of teams.

    retrieve:
        team detail

        Details of team.

    create:
        team create

        Create a new team.

    update:
        team update

        Update a team.

    partial_update:
        team partial update

        Update and team partially.

    destroy:
        team destroy

        Destroy a team.
    """

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    serializer_class = TeamSerializer
    queryset = Team.objects.prefetch_related(
        'organization'
    )

    def create(self, request, *args, **kwargs):
        organization = Organization.objects.get(slug=kwargs['organization_slug'])

        serializer = self.get_serializer(data={
            'name': request.data['name'],
            'organization': organization.uuid
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        organization = Organization.objects.get(slug=kwargs['organization_slug'])

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data={
            'name': request.data['name'],
            'organization': organization.uuid}, partial=partial)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)