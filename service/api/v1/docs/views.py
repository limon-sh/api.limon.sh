from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


DocumentationView = get_schema_view(
    openapi.Info(
        title='Limon',
        default_version='v1',
        description='Server performance monitoring project API.',
        contact=openapi.Contact(
            name='Andrey Doroschenko'
        )
    ),
    public=True,
    permission_classes=(
        permissions.AllowAny,
    )
)
