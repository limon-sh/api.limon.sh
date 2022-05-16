from rest_framework import serializers
from settings import base as settings
from apps.product.models import Product
from libs.validators import ValidateFileSize, ValidateFileExtension


class ProductSerializer(serializers.ModelSerializer):

    logo = serializers.ImageField(
        required=False,
        allow_null=True,
        validators=[ValidateFileSize(settings.IMAGE_UPLOAD_MAX_SIZE),
                    ValidateFileExtension(settings.ALLOWED_IMAGE_EXTENSIONS)])

    class Meta:
        model = Product
        fields = (
            'name',
            'slug',
            'organization',
            'logo'
        )
        extra_kwargs = {
            'name': {'required': False},
            'slug': {'required': False, 'read_only': True},
        }
