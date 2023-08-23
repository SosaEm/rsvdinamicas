from geopy.geocoders import Nominatim 


geocode = lambda query: geolocator.geocode("%s, Buenos Aires" % query)
geolocator = Nominatim(user_agent="georef")
location = geolocator.geocode("11, 3380, Berazategui,Buenos Aires")
print((location.latitude, location.longitude))
print(location.raw)
print(location.address)
location = geolocator.geocode("gavilan,94,flores", country_codes="ar")
print((location.latitude, location.longitude))
print(location.raw)
print(location.address)