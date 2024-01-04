import requests             # to work with API's
from datetime import datetime
MY_LAT = 54.687157
MY_LONG = 25.279652
response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response1.raise_for_status()
data = response1.json()

longitude = float(response1.json()['iss_position']['longitude'])
latitude = float(response1.json()['iss_position']['latitude'])
iss_position = (longitude, latitude)
print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data2 = response.json()
sunrise = int(data2["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data2["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)

LAT_distance = abs(MY_LAT - latitude)
LON_distance = abs(MY_LONG - longitude)
if LAT_distance <= 5 or LON_distance <= 5 and time_now.hour < sunrise or time_now.hour > sunset:
    print("look up")
else:
    print("ISS is not there yet")
