# Source: https://www.geeksforgeeks.org/create-a-gui-to-get-sunset-and-sunrise-time-using-python/

from suntime import Sun
from geopy.geocoders import Nominatim

'''
Return the local sunrise and sunset for the given date and location
as 24-hour time. 

Ex: 07:00 or 16:00
'''
def getSunrise(now, place):
    # Nominatim API to get latitude and longitude
    geolocator = Nominatim(user_agent="geoapiExercises")

    location = geolocator.geocode(place)

    # latitude and longitude fetch
    latitude = location.latitude
    longitude = location.longitude
    sun = Sun(latitude, longitude)

    # Return the formated string as 24 hour time.
    return (sun.get_local_sunrise_time(now)).strftime('%H:%M'), (sun.get_local_sunset_time(now)).strftime('%H:%M')

