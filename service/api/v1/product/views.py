from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.organization.models import Organization
from apps.product.models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    list:
        product list

        List of products.

    retrieve:
        product detail

        Details of product.

    create:
        product create

        Create a new product.

    update:
        product update

        Update a product.

    partial_update:
        product partial update

        Update a product partially.

    destroy:
        product destroy

        Destroy a product.
    """

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    serializer_class = ProductSerializer
    queryset = Product.objects.prefetch_related(
        'organization'
    ).order_by('name')

    def create(self, request, *args, **kwargs):
        organization = Organization.objects.get(slug=kwargs['organization_slug'])

        serializer = self.get_serializer(data={
            'name': request.data['name'],
            'organization': organization.uuid,
            'logo': request.data['logo']
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
            'organization': organization.uuid,
            'logo': request.data['logo']
        }, partial=partial)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
