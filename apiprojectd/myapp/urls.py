from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,CustomerViewset,OrderViewSet

router=DefaultRouter()
router.register(r'products',ProductViewSet)
router.register(r'customers',CustomerViewset)
router.register(r'orders',OrderViewSet)


urlpatterns=router.urls