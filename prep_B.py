# Importo mysql.connector per connettermi a MariaDB
import mysql.connector

# Mi collego direttamente al database 'Animali'
mydb = mysql.connector.connect(
  host="localhost",  # Host del database
  user="pythonuser",  # Utente del database
  password="password123",  # Password dell'utente
  database="Animali"  # Specifico il database a cui connettermi
)

# Creo un cursore per eseguire le query
mycursor = mydb.cursor()

# Preparo il comando SQL per inserire i dati nelle colonne giuste
sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"

# Creo una lista con i 5 animali (Nome, Razza, Peso in kg, Età)
valori = [
  ("Fuffi", "Cane", 15, 5),  # Primo animale
  ("Silvestro", "Gatto", 4, 3),  # Secondo animale
  ("Bugs", "Coniglio", 2, 1),  # Terzo animale
  ("Hamtaro", "Criceto", 1, 2),  # Quarto animale
  ("Spirit", "Cavallo", 400, 8)  # Quinto animale
]

# Eseguo l'inserimento multiplo di tutta la lista
mycursor.executemany(sql, valori)

# Salvo le modifiche al database
mydb.commit()

# Stampo un messaggio con il numero di animali inseriti
print("Fantastico! Ho inserito", mycursor.rowcount, "animali nel database.")