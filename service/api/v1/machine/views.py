from rest_framework import viewsets
from apps.machine.models import Machine
from .serializers import MachineSerializer


class MachineViewSet(viewsets.ModelViewSet):
    """
    list:
        machine list

        List of machines.

    retrieve:
        machine detail

        Details of machine.

    create:
        machine create

        Create a new machine.

    update:
        machine update

        Update a machine.

    partial_update:
        machine partial update

        Update a machine partially.

    destroy:
        machine destroy

        Destroy a machine.
    """

    lookup_field = 'uuid'
    lookup_url_kwarg = 'uuid'
    serializer_class = MachineSerializer
    queryset = Machine.objects.all()
