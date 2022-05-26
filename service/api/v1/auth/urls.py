from rest_framework import routers

from .google.views import GoogleAuthenticationViewSet


router = routers.SimpleRouter()
router.register('google', GoogleAuthenticationViewSet, basename='google')

urlpatterns = router.urls
