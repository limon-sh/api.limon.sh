from django.urls import path

from .views import DocumentationView


urlpatterns = [
    path('', DocumentationView.with_ui('redoc', cache_timeout=0)),
]
