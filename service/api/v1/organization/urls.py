from rest_framework import routers

from .views import OrganizationViewSet


router = routers.SimpleRouter()
router.register('', OrganizationViewSet)

urlpatterns = router.urls
