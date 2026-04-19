# Importo mysql.connector per connettermi a MariaDB
import mysql.connector

# Mi collego a MariaDB senza specificare il database perché devo crearlo
mydb = mysql.connector.connect(
  host="localhost",  # Host del database
  user="pythonuser",  # Utente del database
  password="password123"  # Password dell'utente
)
# Creo un cursore per eseguire le query
mycursor = mydb.cursor()

# Creo il database CLASH_ROYALE se non esiste
mycursor.execute("CREATE DATABASE IF NOT EXISTS CLASH_ROYALE")
# Seleziono il database CLASH_ROYALE
mycursor.execute("USE CLASH_ROYALE")

# Creo la tabella Clash_Unit se non esiste con le colonne specificate
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Clash_Unit (
  id INT AUTO_INCREMENT PRIMARY KEY,  # Colonna id auto-incrementante e chiave primaria
  name VARCHAR(255),  # Colonna name di tipo stringa
  transport VARCHAR(255),  # Colonna transport di tipo stringa
  rarity VARCHAR(255),  # Colonna rarity di tipo stringa
  speed VARCHAR(255),  # Colonna speed di tipo stringa
  damage INT  # Colonna damage di tipo intero
)
""")

# Svuoto la tabella Clash_Unit per rimuovere eventuali vecchi dati
mycursor.execute("TRUNCATE TABLE Clash_Unit")

# Definisco la query SQL per inserire i dati
sql = "INSERT INTO Clash_Unit (name, transport, rarity, speed, damage) VALUES (%s, %s, %s, %s, %s)"
# Definisco i valori da inserire
valori = [
  ('Cucciolo di Drago', 'Air', 'Epic', 'Fast', 133),  # Primo record
  ('Cavaliere', 'Ground', 'Common', 'Medium', 167),  # Secondo record
  ('Mongolfiera', 'Air', 'Epic', 'Medium', 798)  # Terzo record
]

# Eseguo l'inserimento di più record
mycursor.executemany(sql, valori)
# Confermo le modifiche al database
mydb.commit()

# Stampo un messaggio di successo
print("✅ Magia completata! Database CLASH_ROYALE e tabella creati con successo!")