from rest_framework import routers

from api.v1.auth.token.views import TokenAuthenticationViewSet


router = routers.SimpleRouter()
router.register(
    'token', TokenAuthenticationViewSet, basename='TokenAuthentication'
)

urlpatterns = router.urls
