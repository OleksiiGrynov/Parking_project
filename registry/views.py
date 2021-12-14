from registry.models import Vehicle
from registry.serializers import UpdateSerializer, VehicleSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


class UpdateDriverView(CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = UpdateSerializer

    def create(self, request, pk):
        vehicle = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vehicle.driver_id = serializer.data["driver"]
        vehicle.save()

        return Response(VehicleSerializer(instance=vehicle).data)
