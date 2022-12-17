import requests


url = "https://data.buienradar.nl/2.0/feed/json"

response = requests.request("GET",url)
actueel = response.json()["actual"]
lokaal = actueel["stationmeasurements"]
exacteLocatie = lokaal[12]                          #voor nu ff zo. Groningen is dit.


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

out = f"Meetmoment: {meetMoment}:\nStation: {stationNaam},  regio: {regio}  \nZon op: {zonOp}, zon onder: {zonOnder}, zonkracht: {zonKracht}\n" 
out = out + f"{weersOmschrijving} \nLuchtdruk: {luchtdruk}, windsnelheid {windsnelheid}, windrichting: {windrichting}, graad: {windrichtinggraad}\n"
out =  out + f"Vochtpercentage: {vocht}, neerslag: {neerslag}, regen laatste uur: {regenUur}, regen laatste 24 uur: {regen24}, zicht: {zicht}\n"
out =  out + f"Temperatuur: {temp}, grondtemperatuur: {tempGrond}, gevoelstemperatuur {tempGevoel}" 
print(out)