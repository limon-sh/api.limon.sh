from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.organization.models import Organization
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
