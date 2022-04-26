from django.urls import include, path

from .auth.urls import urlpatterns as auth_urls
from .docs.urls import urlpatterns as docs_urls
from .organization.urls import urlpatterns as organization_urls


urlpatterns = [
    path('docs/', include(docs_urls)),
    path('auth/', include(auth_urls), name='auth'),
    path('organizations/', include(organization_urls), name='organization'),
]
