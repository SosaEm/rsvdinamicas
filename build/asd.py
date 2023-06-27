from geopy.geocoders import Nominatim 



geolocator = Nominatim(user_agent="georef")
location = geolocator.geocode("11, 3380, Berazategui,ar")
print((location.latitude, location.longitude))
print(location.raw)
print(location.address)
location = geolocator.geocode("gavilan,94,flores,ar")
print((location.latitude, location.longitude))
print(location.raw)
print(location.address)