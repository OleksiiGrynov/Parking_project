from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from registry.models import Driver, Vehicle


class TestDriver(APITestCase):
    def test_all(self):
        driver = Driver.objects.create(first_name="First", last_name="Last")
        response = self.client.get("/drivers/driver/")
        data = response.json()
        self.assertEqual(driver.id, data[0]["id"])
        self.assertEqual(driver.first_name, data[0]["first_name"])
        self.assertEqual(driver.last_name, data[0]["last_name"])

    def test_create(self):
        params = {"first_name": "test", "last_name": "new"}
        response = self.client.post("/drivers/driver/", data=params)
        data = response.json()
        self.assertEqual(params["first_name"], data["first_name"])
        self.assertEqual(params["last_name"], data["last_name"])

    def test_delete(self):
        driver = Driver.objects.create(first_name="First", last_name="Last")
        response = self.client.delete(f"/drivers/driver/{driver.id}/")
        self.assertEqual(response.status_code, 204)


class TestVehicle(APITestCase):
    def test_all(self):
        vehicle = Vehicle.objects.create(make="First", model="model", plate_number="Last")
        response = self.client.get("/vehicles/vehicle/")
        data = response.json()
        self.assertEqual(vehicle.id, data[0]["id"])
        self.assertEqual(vehicle.make, data[0]["make"])
        self.assertEqual(vehicle.model, data[0]["model"])
        self.assertEqual(vehicle.plate_number, data[0]["plate_number"])

    def test_create(self):
        params = {"make": "First", "model": "model", "plate_number": "Last"}
        response = self.client.post("/vehicles/vehicle/", data=params)
        data = response.json()
        self.assertEqual(params["make"], data["make"])
        self.assertEqual(params["model"], data["model"])
        self.assertEqual(params["plate_number"], data["plate_number"])

    def test_delete(self):
        vehicle = Vehicle.objects.create(make="First", model="model", plate_number="Last")
        response = self.client.delete(f"/vehicles/vehicle/{vehicle.id}/")
        self.assertEqual(response.status_code, 204)

    def test_set_driver(self):
        driver = Driver.objects.create(first_name="First", last_name="Last")
        vehicle = Vehicle.objects.create(make="First", model="model", plate_number="Last")
        response = self.client.post(f"/vehicles/vehicle/set_driver/{vehicle.id}", data={"driver": driver.id})
        data = response.json()
        self.assertEqual(data["driver"], driver.id)

        response = self.client.post(f"/vehicles/vehicle/set_driver/{vehicle.id}", data={"driver": ""})
        data = response.json()
        self.assertFalse(data["driver"])
