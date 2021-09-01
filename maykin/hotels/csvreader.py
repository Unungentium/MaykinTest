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
    """This function takes in the urls provided in the email, as well as the passwords and re-writes them in a usable format for django. This method can
    be improved, and with more time I would look at simplifying this code."""
    user, password = ('python-demo', 'claw30_bumps')

    url_hotels = 'http://rachel.maykinmedia.nl/djangocase/hotel.csv'
    url_cities = 'http://rachel.maykinmedia.nl/djangocase/city.csv' #quick note to myself and future contributors - there appears to be a doubling of hotels in the csv file. For future versions, please fix that.
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
        h = []
        for row in city_list:
            city = City(CityName=str(row)[2:5], ticked=False)
            c.append(str(row)[2:5])
            city.save()
            for a in hotel_list:
                if str(a)[2:5] == city.CityName: #this is my attempt at fixing the doubling issue in the hotels in bangkok. I am unsure why the code isn't doing what its supposed to do - F.P. 
                    if h not in hotel_list:
                        b = city.hotel_set.create(HotelName=str(a)[15:-3])
                        hotel_dict[b] = city
                        h.append(a)
                        city.save()
                    
            city.save()
    return hotel_dict, c
returner()
    
#This file takes in the requested csv files, and writes them as the Hotel and 
#city objects defined in the methods section. These will be used to write the final website structure