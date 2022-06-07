from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenVerifyView

from .google.views import GoogleAuthenticationViewSet
from .basic.views import BasicAuthenticationViewSet


router = routers.SimpleRouter()
router.register('google', GoogleAuthenticationViewSet, basename='google')
router.register('basic', BasicAuthenticationViewSet, basename='basic')

urlpatterns = router.urls + [
    path('verify/', TokenVerifyView.as_view(), name='token_verify')
]
