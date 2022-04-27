from rest_framework import viewsets
from apps.project.models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    list:
        project list

        List of projects.

    retrieve:
        project detail

        Details of project.

    create:
        project create

        Create a new project.

    update:
        project update

        Update a project.

    partial_update:
        project partial update

        Update and project partially.

    destroy:
        project destroy

        Destroy a project.
    """

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    serializer_class = ProjectSerializer
    queryset = Project.objects.prefetch_related(
        'teams'
    )
