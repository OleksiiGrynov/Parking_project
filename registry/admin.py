from django.contrib import admin

from registry.models import Driver, Vehicle


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created_at', 'updated_at')


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'plate_number', 'driver', 'created_at', 'updated_at')
