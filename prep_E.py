# Importo mysql.connector per connettermi a MariaDB
import mysql.connector

# Mi collego al database
mydb = mysql.connector.connect(
  host="localhost",  # Host del database
  user="pythonuser",  # Utente del database
  password="password123",  # Password dell'utente
  database="Animali"  # Nome del database
)
# Creo un cursore per eseguire le query
mycursor = mydb.cursor()

# Uso il comando SQL 'WHERE' per selezionare solo quelli con Peso maggiore di 2
mycursor.execute("SELECT * FROM Mammiferi WHERE Peso > 2")

# Prendo tutti i risultati trovati
risultati = mycursor.fetchall()

# Stampo a schermo solo gli animali che pesano più di 2 kg
print("--- ANIMALI CHE PESANO PIÙ DI 2 KG ---")
for animale in risultati:
    print(animale)