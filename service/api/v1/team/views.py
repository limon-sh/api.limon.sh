from rest_framework import viewsets
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
