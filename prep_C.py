# Importo mysql.connector per connettermi a MariaDB
import mysql.connector

# Mi collego al database 'Animali'
mydb = mysql.connector.connect(
  host="localhost",  # Host del database
  user="pythonuser",  # Utente del database
  password="password123",  # Password dell'utente
  database="Animali"  # Nome del database
)

# Creo un cursore per eseguire le query
mycursor = mydb.cursor()

# Uso il comando SQL 'SELECT *' per selezionare tutto dalla tabella Mammiferi
mycursor.execute("SELECT * FROM Mammiferi")

# Prendo tutti i risultati trovati e li salvo in una variabile
risultati = mycursor.fetchall()

# Uso un ciclo per stampare ogni animale riga per riga
print("--- ELENCO DEGLI ANIMALI NEL DATABASE ---")
for animale in risultati:
  print(animale)