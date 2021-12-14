from django.db import models


class DatetimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Driver(DatetimeMixin, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Vehicle(DatetimeMixin, models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    plate_number = models.CharField(max_length=15)

    driver = models.ForeignKey(Driver, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.model} {self.make} {self.plate_number}"
