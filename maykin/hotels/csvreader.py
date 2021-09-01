import os, sys, django
sys.path.append("C:/Users/frane/OneDrive/Desktop/maykin_media/maykin")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "maykin.settings")
django.setup()
from hotels.models import Hotel, City
import csv
import requests
import csv, requests
City.objects.all().delete()
def returner():
    user, password = ('python-demo', 'claw30_bumps')

    url_hotels = 'http://rachel.maykinmedia.nl/djangocase/hotel.csv'
    url_cities = 'http://rachel.maykinmedia.nl/djangocase/city.csv'
    with requests.Session() as s:
        download_h = s.get(url_hotels, auth=(user,password))
        download_c = s.get(url_cities, auth=(user,password))
        dec_cont=  download_h.content.decode('utf-8')
        cit_cont = download_c.content.decode('utf-8')
        cr_h = csv.reader(dec_cont.splitlines(), delimiter=',')
        cr_c = csv.reader(cit_cont.splitlines(), delimiter=',')
        hotel_list = list(cr_h)
        city_list = list(cr_c)
        hotel_dict=dict()
        c = []
        for row in city_list:
            city = City(CityName=str(row)[2:5], ticked=False)
            c.append(str(row)[2:5])
            city.save()
            for a in hotel_list:
                if str(a)[2:5] == city.CityName:
                    b = city.hotel_set.create(HotelName=str(a)[15:-3])
                    hotel_dict[b] = city
                    city.save()
                    
            city.save()
    print(c)
    return hotel_dict, c
returner()
    
#This file takes in the requested csv files, and writes them as the Hotel and 
#city objects defined in the methods section. These will be used to write