import requests
from datetime import datetime

MY_LAT = 40.789143
MY_LONG = -73.134964

parameters = {
  "lat": MY_LAT,
  "lon": MY_LONG,
  "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# 2021-10-23T17:09:35+00:00
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunset)
time_now  = datetime.now()