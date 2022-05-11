from rest_framework import serializers

from apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'name',
            'slug',
            'organization'
        )
        extra_kwargs = {
            'name': {'required': False},
            'slug': {'required': False, 'read_only': True}
        }
