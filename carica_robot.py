import mysql.connector
import csv

# Mi collego a MariaDB
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123"
)
mycursor = mydb.cursor()

# Creo il nuovo database per i robot
mycursor.execute("CREATE DATABASE IF NOT EXISTS ROBOT_DB")
mycursor.execute("USE ROBOT_DB")

# Creo la tabella
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Robots (
  id INT PRIMARY KEY,
  nome VARCHAR(255),
  tipo VARCHAR(255),
  anno_creazione INT,
  autonomia_ore INT
)
""")

# Pulisco la tabella prima di inserire i nuovi dati
mycursor.execute("TRUNCATE TABLE Robots")

# Leggo il file CSV e inserisco i dati (salto la prima riga di intestazione)
with open('robot.csv', mode='r', encoding='utf-8') as file:
    lettore = csv.reader(file)
    next(lettore) # Salta la riga id,nome,tipo...
    
    for riga in lettore:
        sql = "INSERT INTO Robots (id, nome, tipo, anno_creazione, autonomia_ore) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sql, (int(riga[0]), riga[1], riga[2], int(riga[3]), int(riga[4])))

mydb.commit()
print("✅ File CSV dei robot caricato con successo nel database ROBOT_DB!")