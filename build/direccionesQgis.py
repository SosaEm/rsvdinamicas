from types import NoneType
from geopy.geocoders import Nominatim 
import csv
import json
from geopy.exc import GeocoderTimedOut
import time
start_time = time.time()



f = open(r'C:\Users\esosa\Desktop\Nominatim\rsvdinamicas\informes\personal.json')
data=json.load(f)
json_str = json.dumps(data)
resp = json.loads(json_str)


with open('informes\personal.json', 'r', encoding='utf-8') as json_file:
    for x in resp:
        try:
            geolocator = Nominatim(user_agent="georef")
            location = geolocator.geocode(x["direccion"] + "," + x["altura"] + "," + x["localidad"] + "," + "Buenos Aires")
            id=(x['record_id'])
            dire=location.address
            lati=location.latitude
            lon=location.longitude
            with open('informes/direcciones.csv', 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow(["{};{};{};{};{};{};{};{}" .format(id,x["hospital"],x["fecha_ingreso"],dire,lati,lon,x["uti"],x["dx_egreso"])])
        except:
            with open('informes/direcciones2.csv', 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow(["{};{};{};{};{}" .format(x["record_id"],x["hospital"],x["direccion"],x["altura"],x["localidad"])]) 

print("--- %s seconds ---" % (time.time() - start_time))
