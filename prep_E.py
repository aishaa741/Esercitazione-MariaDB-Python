import mysql.connector

# 1. Mi collego al database
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="Animali"
)
mycursor = mydb.cursor()

# 2. Uso il comando SQL 'WHERE' per dire "prendi solo quelli con Peso maggiore di 2"
mycursor.execute("SELECT * FROM Mammiferi WHERE Peso > 2")

# 3. Prendo tutti i risultati trovati
risultati = mycursor.fetchall()

# 4. Stampo a schermo solo gli animali belli pesanti!
print("--- ANIMALI CHE PESANO PIÙ DI 2 KG ---")
for animale in risultati:
    print(animale)