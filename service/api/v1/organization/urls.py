from django.urls import path, include
from .views import OrganizationViewSet
from api.v1.project.views import ProjectViewSet
from api.v1.product.views import ProductViewSet
from api.v1.machine.views import MachineViewSet
from api.v1.cluster.views import ClusterViewSet
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('', OrganizationViewSet)

product_router = routers.NestedSimpleRouter(router, '', lookup='organization')
product_router.register('product', ProductViewSet)

project_router = routers.NestedSimpleRouter(product_router, 'product', lookup='product')
project_router.register('project', ProjectViewSet)

machine_router = routers.NestedSimpleRouter(project_router, 'project', lookup='project')
machine_router.register('machines', MachineViewSet)

cluster_router = routers.NestedSimpleRouter(project_router, 'project', lookup='project')
cluster_router.register('clusters', ClusterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(product_router.urls)),
    path('', include(machine_router.urls)),
    path('', include(cluster_router.urls)),
]
