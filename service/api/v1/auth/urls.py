from rest_framework import routers

from .token.views import TokenAuthenticationViewSet
from .google.views import GoogleAuthenticationViewSet


router = routers.SimpleRouter()
router.register('token', TokenAuthenticationViewSet, basename='token')
router.register('google', GoogleAuthenticationViewSet, basename='google')

urlpatterns = router.urls
