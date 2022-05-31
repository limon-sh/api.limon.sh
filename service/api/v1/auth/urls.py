from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenVerifyView

from .google.views import GoogleAuthenticationViewSet


router = routers.SimpleRouter()
router.register('google', GoogleAuthenticationViewSet, basename='google')

urlpatterns = router.urls + [
    path('verify/', TokenVerifyView.as_view(), name='token_verify')
]
