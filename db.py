import sqlite3

conn = sqlite3.connect("dataweerstations.db")


#We can verify we successfully created our connection object by running:
#print(conn.total_changes)

cursor = conn.cursor()
try: 
	cursor.execute('''CREATE TABLE "stations" (
		"id"	INTEGER,
		"stationID"	INTEGER UNIQUE,
		"stationname"	TEXT,
		"regio"	TEXT,
		PRIMARY KEY("id" AUTOINCREMENT)
	);''')

	cursor.execute(''' CREATE TABLE "stationdata" (
		"id"	INTEGER,
		"stationId"	INTEGER,
		"zonKracht"	REAL,
		"meetMoment"	TEXT,
		"luchtdruk"	NUMERIC,
		"weersOmschrijving"	BLOB,
		"temp"	NUMERIC,
		"tempGrond"	NUMERIC,
		"tempGevoel"	NUMERIC,
		"windsnelheid"	NUMERIC,
		"windrichting"	BLOB,
		"windrichtinggraad"	TEXT,
		"vocht"	NUMERIC,
		"neerslag"	NUMERIC,
		"regenUur"	NUMERIC,
		"regen24"	NUMERIC,
		"zicht"	NUMERIC,
		PRIMARY KEY("id" AUTOINCREMENT),
		FOREIGN KEY("stationId") REFERENCES "stations"("stationID")
	);''')
except:
	pass


rows = cursor.execute("SELECT * FROM stationdata").fetchall()
print(rows)

conn.close()

