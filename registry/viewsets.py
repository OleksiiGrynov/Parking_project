import dateutil.parser

from rest_framework import viewsets

from registry.serializers import DriverSerializer, VehicleSerializer
from registry.models import Driver, Vehicle


class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer

    def get_queryset(self):
        queryset = Driver.objects.all()
        created_at_gte = self.request.query_params.get('created_at__gte')
        created_at_lte = self.request.query_params.get('created_at__lte')
        if created_at_gte:
            queryset = queryset.filter(created_at__gte=dateutil.parser.parse(created_at_gte))
        if created_at_lte:
            queryset = queryset.filter(created_at__lte=dateutil.parser.parse(created_at_lte))
        return queryset


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        with_drivers = self.request.query_params.get('with_drivers')
        if with_drivers == "yes":
            queryset = queryset.filter(driver__isnull=False)
        elif with_drivers == "no":
            queryset = queryset.filter(driver__isnull=True)
        return queryset
