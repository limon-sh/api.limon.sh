from django.urls import path, include
from .views import OrganizationViewSet
from api.v1.project.views import ProjectViewSet
from api.v1.team.views import TeamViewSet
from api.v1.product.views import ProductViewSet
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('', OrganizationViewSet)

team_router = routers.NestedSimpleRouter(router, '', lookup='organization')
team_router.register('team', TeamViewSet)

product_router = routers.NestedSimpleRouter(router, '', lookup='organization')
product_router.register('product', ProductViewSet)

project_router = routers.NestedSimpleRouter(product_router, 'product', lookup='product')
project_router.register('project', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(team_router.urls)),
    path('', include(product_router.urls)),
]
