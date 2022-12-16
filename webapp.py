import requests


url = "https://data.buienradar.nl/2.0/feed/json"

response = requests.request("GET",url)
actueel = response.json()["actual"]
lokaal = actueel["stationmeasurements"]
exacteLocatie = lokaal[12]              #voor nu ff zo. Groningen is dit.


zonOp = actueel["sunrise"]
zonOnder = actueel["sunset"]

zonKracht = exacteLocatie["sunpower"]
stationId = exacteLocatie["stationid"]
stationNaam = exacteLocatie["stationname"]
regio = exacteLocatie["regio"]
meetMoment = exacteLocatie["timestamp"]
weersOmschrijving = exacteLocatie["weatherdescription"]
luchtdruk = exacteLocatie["airpressure"]
temp = exacteLocatie["temperature"]
tempGrond = exacteLocatie["groundtemperature"]
tempGevoel = exacteLocatie["feeltemperature"]
windsnelheid = exacteLocatie["windspeed"]
windrichting = exacteLocatie["winddirection"]
windrichtinggraad = exacteLocatie["winddirectiondegrees"]
vocht = exacteLocatie["humidity"]
neerslag = exacteLocatie["precipitation"]
regenUur = exacteLocatie["rainFallLastHour"]
regen24 = exacteLocatie["rainFallLast24Hour"]
zicht = exacteLocatie["visibility"]


print(exacteLocatie)