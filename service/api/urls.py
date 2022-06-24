from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .v1 import urls as v1_urls
from settings import Environment

app_name = 'api'


urlpatterns = [
    path('v1/', include(v1_urls), name='v1'),
    path('admin/', admin.site.urls),
    path('healthcheck/', lambda request: HttpResponse(status=200))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if Environment.is_develop():
    urlpatterns += [
        path('silk/', include('silk.urls', namespace='silk'))
    ]
