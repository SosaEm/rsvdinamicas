from types import NoneType
from geopy.geocoders import Nominatim 
import csv
import json
import geopy
from geopy.exc import GeocoderTimedOut

def do_geocode(address, attempt=1, max_attempts=5):
    try:
        return geopy.geocode(address)
    except GeocoderTimedOut:
        if attempt <= max_attempts:
            return do_geocode(address, attempt=attempt+1)
        raise


#geolocator = Nominatim(user_agent="georef")
#location = geolocator.geocode("11, 3380, Berazategui,ar")
#print((location.latitude, location.longitude))
#print(location.raw)
#print(location.address)
#location = geolocator.geocode("gavilan,94,flores,ar")
#print((location.latitude, location.longitude))
#print(location.raw)
#print(location.address)

f = open(r'C:\Users\esosa\Desktop\Nominatim\rsvdinamicas\informes\personal.json')
data=json.load(f)
json_str = json.dumps(data)
resp = json.loads(json_str)

with open('informes/personal.json', 'r', encoding='utf-8') as json_file:
    for x in resp:
        try:
            geolocator = Nominatim(user_agent="georef")
            location = geolocator.geocode("calle " + x["direccion"] + "," + x["altura"] + "," + x["localidad"] + "," + "ar")
            id=(x['record_id'])
            dire=location.address
            lati=location.latitude
            lon=location.longitude
            with open('informes/longylat.csv', 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow(["{},{},{},{}" .format(id,lati,lon,"ARG")])
        except:
            NoneType    
