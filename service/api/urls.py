from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .v1 import urls as v1_urls

urlpatterns = [
    path('v1/', include(v1_urls)),
    path('admin/', admin.site.urls),
    path('healthcheck/', lambda request: HttpResponse(status=200))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
