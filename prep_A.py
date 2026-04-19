# Importo mysql.connector per connettermi a MariaDB
import mysql.connector

# Mi collego a MariaDB usando l'utente creato prima
mydb = mysql.connector.connect(
  host="localhost",  # Host del database
  user="pythonuser",  # Utente del database
  password="password123"  # Password dell'utente
)

# Creo un cursore per eseguire le query
mycursor = mydb.cursor()

# Creo il database 'Animali' se non esiste già
mycursor.execute("CREATE DATABASE IF NOT EXISTS Animali")

# Dico al sistema di usare il database 'Animali'
mycursor.execute("USE Animali")

# Definisco la query SQL per creare la tabella 'Mammiferi'
sql_tabella = """
CREATE TABLE IF NOT EXISTS Mammiferi (
  Id INT AUTO_INCREMENT PRIMARY KEY,  # Colonna Id auto-incrementante e chiave primaria
  Nome_Proprio VARCHAR(255),  # Colonna Nome_Proprio di tipo stringa
  Razza VARCHAR(255),  # Colonna Razza di tipo stringa
  Peso INT,  # Colonna Peso di tipo intero
  Eta INT  # Colonna Eta di tipo intero
)
"""
# Eseguo la creazione della tabella
mycursor.execute(sql_tabella)

# Stampo un messaggio di successo
print("Perfetto! Database 'Animali' e tabella 'Mammiferi' creati con successo!")