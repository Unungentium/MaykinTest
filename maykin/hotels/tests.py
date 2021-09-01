from django.test import TestCase
from hotels.models import Hotel, City
# Create your tests here.

class HotelTestCase(TestCase):
    def SetUp(self):
        city=City.objects.create(CityName="Amsterdam", ticked=True)
        city.create(HotelName="Travelodge")
        city.save()
    def test_city_creation(self):
        get_city = City.objects.get(CityName="Amsterdam")
        self.assertEqual(get_city.CityName(), "Amsterdam")