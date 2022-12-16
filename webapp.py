import requests


url = "https://data.buienradar.nl/2.0/feed/json"

response = requests.request("GET",url)
actueel = response.json()["actual"]
lokaal = actueel["stationmeasurements"]
exacteLocatie = lokaal[12]              #voor nu ff zo. Groningen is dit.


print(actueel["sunrise"])
print(actueel["sunset"])

print(exacteLocatie["stationname"])
print(exacteLocatie["timestamp"])
print(exacteLocatie["weatherdescription"])
print(exacteLocatie["airpressure"])
print(exacteLocatie["temperature"])
print(exacteLocatie["groundtemperature"])
print(exacteLocatie["windspeed"])