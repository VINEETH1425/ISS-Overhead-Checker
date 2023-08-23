import requests
from math import radians, sin, cos, sqrt, atan2
import time

def get_iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])
    return iss_latitude, iss_longitude

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

city_latitude = 13.6288  # Replace with the city's latitude
city_longitude = 79.4192  # Replace with the city's longitude
n_range = 50  # Replace with your desired range in kilometers

while True:
    iss_latitude, iss_longitude = get_iss_location()
    distance_to_city = calculate_distance(iss_latitude, iss_longitude, city_latitude, city_longitude)

    if distance_to_city <= n_range:
        print("ISS is within {} km range of the city.".format(n_range))
        print("ISS is directly overhead the city.")
    else:
        print("ISS is not within {} km range of the city.".format(n_range))
        print("Current ISS location: Latitude {}, Longitude {}".format(iss_latitude, iss_longitude))

    # Delay for a certain amount of time before checking again
    time.sleep(6)  # Delay for 60 seconds before checking again

