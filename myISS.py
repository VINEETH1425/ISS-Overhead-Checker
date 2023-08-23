import requests
from datetime import datetime
import time

currlat = 13.6288
currlong = 79.4192

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    # print(response.raise_for_status())
    data = response.json()
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])
    print(data)
    if abs(currlat - iss_latitude) < 20  and abs(currlong - iss_longitude) < 20: # here 20 is the range.
        print("It is in the range")
        print(f"ISS Latitude: {iss_latitude}, ISS Longitude: {iss_longitude}")
        break
    else:
        print("It is not in the range")
        print(f"ISS Latitude: {iss_latitude}, ISS Longitude: {iss_longitude}")
        # here u have write f otherwise it will be included
        time.sleep(10)  # Check every 10 second