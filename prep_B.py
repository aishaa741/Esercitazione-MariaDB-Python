import mysql.connector

# 1. Mi collego direttamente al database 'Animali'
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="Animali"  # Nota: ora specifico in quale DB voglio entrare
)

mycursor = mydb.cursor()

# 2. Preparo il comando SQL per inserire i dati nelle colonne giuste
sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"

# 3. Creo una lista con i 5 animali (Nome, Razza, Peso in kg, Età)
valori = [
  ("Fuffi", "Cane", 15, 5),
  ("Silvestro", "Gatto", 4, 3),
  ("Bugs", "Coniglio", 2, 1),
  ("Hamtaro", "Criceto", 1, 2),
  ("Spirit", "Cavallo", 400, 8)
]

# 4. Eseguo l'inserimento multiplo di tutta la lista
mycursor.executemany(sql, valori)

# 5. SALVO LE MODIFICHE (Se dimentichi questa riga, il database non salva nulla!)
mydb.commit()

print("Fantastico! Ho inserito", mycursor.rowcount, "animali nel database.")