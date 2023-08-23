# import requests module
import requests
from datetime import datetime
import time
currlat = 13.6288
currlong = 79.4192
# Making a get request
response = requests.get(url="http://api.open-notify.org/iss-now.json")

#check if an error has occurred,returns an HTTPError object if an error has occurred during the process.
response.raise_for_status()

#used to fetch data from APIs
data = response.json()
iss_latitude = float(data['iss_position']['latitude'])
iss_longitude = float(data['iss_position']['longitude'])
print(data)
# it is used to check any data with the a certain frequency of time mentioned.
# time.sleep(60)

## now we will be creating a dictionary 
parameters = {
    "lat" : currlat,
    "lng" : currlong,
    "formatted" : 0
}
# the use of dictionary is If you intend to use these parameters in a specific API request or function call, you would pass this parameters dictionary as an argument

# now the x and parameters will be refering to the same variable.
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()

# this gives the time in hours
print((datetime.now()).hour)

# this gives the date and time
print(datetime.now())

while True:
    time.sleep(10) ## check for every 10s 
    if((datetime.now()).hour>sunset or (datetime.now()).hour<sunrise) :
        if(abs(currlat-iss_latitude)<1 and abs(currlong-iss_longitude)<1) :
            break
        
    
