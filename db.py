import sqlite3

conn = sqlite3.connect("../databases/weerstations.db")


#We can verify we successfully created our connection object by running:
#print(conn.total_changes)

cursor = conn.cursor()
#cursor.execute("CREATE TABLE stationdata (stationId INTEGER, stationname TEXT, regio TEXT, zonKracht REAL, meetMoment TEXT, luchtdruk REAL, weersOmschrijving TEXT, temp REAL, tempGrond REAL, tempGevoel REAL, windsnelheid REAL, windrichting TEXT, windrichtinggraad INTEGER, vocht REAL, neerslag REAL, regenUur REAL, regen24 REAL, zicht REAL  )")

#cursor.execute("INSERT INTO stationdata VALUES (316333, 'Station Groenkampen', 'PEELOO', 500, '2022-12-18T20:00', 1022.2, 'Lichtbewolkt', -4.5 , -4.8 , -9.4 , 55.3 , 'ZO' , 288.7 , 89.9 , 3.2 , 0.0 , 3.2 , 5200 )")
#cursor.execute("INSERT INTO stationdata VALUES (316333, 'Station Groenkampen', 'PEELOO', 500, '2022-12-18T20:00', 1022.2, 'Lichtbewolkt', -4.5 , -4.8 , -9.4 , 55.3 , 'ZO' , 288.7 , 89.9 , 3.2 , 0.0 , 3.2 , 5200 )")
#conn.commit()

rows = cursor.execute("SELECT * FROM stationdata").fetchall()
print(rows)

