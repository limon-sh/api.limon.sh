from rest_framework import routers

from .views import AuthenticationViewSet


router = routers.SimpleRouter()
router.register('', AuthenticationViewSet, basename='Authentication')

urlpatterns = router.urls
