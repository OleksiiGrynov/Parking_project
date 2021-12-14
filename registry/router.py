from rest_framework import routers

from registry.viewsets import DriverViewSet, VehicleViewSet


router = routers.SimpleRouter()
router.register('drivers/driver', DriverViewSet, basename='Driver')
router.register('vehicles/vehicle', VehicleViewSet, basename='Vehicle')

urlpatterns = router.urls
