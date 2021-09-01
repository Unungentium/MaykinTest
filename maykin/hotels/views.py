from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel, City
from .csvreader import returner
import csv
import requests
# Create your views here.
City.objects.all().delete()
hotel_dict, city_list = returner()
#Hotel_dict and city_list are a relic of a bygone era of this test -  I have effectively scrapped them but kept them in in case I needed them later.
def index(response, name):
    ls = City.objects.get(CityName=name)
    return render(response, "hotels/list.html", {"ls":ls})

def home(response):
    return render(response, "hotels/home.html",{})

