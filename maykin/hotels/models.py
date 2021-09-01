from django.db import models


# Create your models here.

class City(models.Model):
    """Creates the City class which has the attributes name and ticked. 
    Name is a string that contains the name of the city. Ticked is a bool which says whether or not the user has selected this city."""
    CityName = models.CharField(max_length=300)
    ticked = models.BooleanField()

    def __str__(self):
        return self.CityName

class Hotel(models.Model):
    """Creates the Hotel class which has the attribute HotelName, its name. ForeignKey tells Django that Hotel is a part of City and will be deleted in case its City is deleted"""
    hotellist = models.ForeignKey(City, on_delete=models.CASCADE)
    HotelName = models.CharField(max_length = 300)
    def __str__(self):
        return self.HotelName