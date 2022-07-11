from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenVerifyView

from .basic.views import BasicAuthenticationViewSet
from .github.views import GithubAuthenticationViewSet
from .google.views import GoogleAuthenticationViewSet


router = routers.SimpleRouter()
router.register('basic', BasicAuthenticationViewSet, basename='basic')
router.register('github', GithubAuthenticationViewSet, basename='github')
router.register('google', GoogleAuthenticationViewSet, basename='google')

urlpatterns = router.urls + [
    path('verify/', TokenVerifyView.as_view(), name='token_verify')
]
