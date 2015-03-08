"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
import math

# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    return response_data
#print get_json("https://maps.googleapis.com/maps/api/geocode/json?address=FenwayPark")
def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    newplace = ''
    for i in range(len(place_name)):

        if not place_name[i] == " ":
            newplace += place_name[i]
    
    latitude= ''
    longitude = ''
        
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+newplace
    response_data = get_json(url)
    latlong = response_data["results"][0]["geometry"]["location"]
    latitude = str(latlong.get("lat"))
    longitude = str(latlong.get("lng"))
    return (latitude, longitude)

#print get_lat_long("Fenway Park")
def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    #url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat=42.346961&lon=-71.076640&format=json"
    
    url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat="+latitude+"&lon="+longitude+"&format=json"
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    nearestStation = response_data["stop"][0]
    stationLat = nearestStation.get("stop_lat")
    stationLng = nearestStation.get("stop_lon")
    stationName = nearestStation.get("stop_name")
    dlat = abs(float(stationLat) - float(latitude))
    dlon = abs(float(stationLng) - float(longitude))
    Tdist = (math.sqrt(dlat**dlon**2))*(10./90) #gets distance in kilometers
    stationName = stationName.strip("u'")
    return (stationName, Tdist)


#print get_nearest_station("42.3466764", "-71.0972178")

def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    latlong = get_lat_long(place_name)
    return get_nearest_station(latlong[0], latlong[1])
#print find_stop_near("Fenway Park")

