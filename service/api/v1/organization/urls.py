from rest_framework import routers
from .views import OrganizationViewSet, view_cached_data
from django.urls import include, path


#router = routers.SimpleRouter()
#router.register('', OrganizationViewSet)

#urlpatterns = router.urls
urlpatterns = [
    path('testing/', view_cached_data),
]