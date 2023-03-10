import requests
import sqlite3
from datetime import datetime




def fetchdata():

    # datetime object containing current date and time
    now = datetime.now()
    url = "https://data.buienradar.nl/2.0/feed/json"

    response = requests.request("GET",url)
    actueel = response.json()["actual"]
    lokaal = actueel["stationmeasurements"]

    zonOp = actueel["sunrise"]
    zonOnder = actueel["sunset"]

    i = 0
    while i < len(lokaal): 
        exacteLocatie = lokaal[i]   
        
        zonKracht = exacteLocatie.get("sunpower")
        stationId = exacteLocatie.get("stationid")
        stationNaam = exacteLocatie.get("stationname")
        regio = exacteLocatie.get("regio")
        meetMoment = exacteLocatie.get("timestamp")
        weersOmschrijving = exacteLocatie.get("weatherdescription")
        luchtdruk = exacteLocatie.get("airpressure")
        temp = exacteLocatie.get("temperature")
        tempGrond = exacteLocatie.get("groundtemperature")
        tempGevoel = exacteLocatie.get("feeltemperature")
        windsnelheid = exacteLocatie.get("windspeed")
        windrichting = exacteLocatie.get("winddirection")
        windrichtinggraad = exacteLocatie.get("winddirectiondegrees")
        vocht = exacteLocatie.get("humidity")
        neerslag = exacteLocatie.get("precipitation")
        regenUur = exacteLocatie.get("rainFallLastHour")
        regen24 = exacteLocatie.get("rainFallLast24Hour")
        zicht = exacteLocatie.get("visibility")

        print(i + 1)
        print(now)
        out = f"Meetmoment: {meetMoment}:\nStation: {stationNaam},  regio: {regio}  \nZon op: {zonOp}, zon onder: {zonOnder}, zonkracht: {zonKracht}\n" 
        out = out + f"{weersOmschrijving} \nLuchtdruk: {luchtdruk}, windsnelheid {windsnelheid}, windrichting: {windrichting}, graad: {windrichtinggraad}\n"
        out =  out + f"Vochtpercentage: {vocht}, neerslag: {neerslag}, regen laatste uur: {regenUur}, regen laatste 24 uur: {regen24}, zicht: {zicht}\n"
        out =  out + f"Temperatuur: {temp}, grondtemperatuur: {tempGrond}, gevoelstemperatuur {tempGevoel}\n\n" 
        print(out)


        conn = sqlite3.connect("dataweerstations.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO stationdata ('stationId' , 'zonKracht' , 'meetMoment' , 'luchtdruk' , 'weersOmschrijving' , 'temp' , 'tempGrond' , 'tempGevoel' , 'windsnelheid' , 'windrichting' , 'windrichtinggraad' , 'vocht' , 'neerslag' , 'regenUur' , 'regen24' , 'zicht') VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (stationId, zonKracht,meetMoment,luchtdruk,weersOmschrijving,temp,tempGrond,tempGevoel,windsnelheid,windrichting,windrichtinggraad,vocht,neerslag,regenUur,regen24,zicht))
        
        try: 
            #vul de stationstabel bij als er nieuwe stations zijn bijgekomen
            cursor.execute('''INSERT INTO stations ('stationId', 'stationname','regio') VALUES (?,?,?)''', (stationId, stationNaam, regio))
        except:
            pass
        finally:
            conn.commit()
            conn.close()

        i += 1

