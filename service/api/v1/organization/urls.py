from django.urls import path, include
from .views import OrganizationViewSet
from api.v1.project.views import ProjectViewSet
from api.v1.team.views import TeamViewSet
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('', OrganizationViewSet)

project_router = routers.NestedSimpleRouter(router, '', lookup='organization')
project_router.register('project', ProjectViewSet)

team_router = routers.NestedSimpleRouter(router, '', lookup='organization')
team_router.register('team', TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(team_router.urls)),
]
