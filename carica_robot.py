# Importo il modulo mysql.connector per connettermi a MariaDB
import mysql.connector
# Importo il modulo csv per leggere i file CSV
import csv

# Mi collego a MariaDB usando i parametri di connessione
mydb = mysql.connector.connect(
  host="localhost",  # Specifico l'host del database
  user="pythonuser",  # Specifico l'utente del database
  password="password123"  # Specifico la password dell'utente
)
# Creo un cursore per eseguire le query SQL
mycursor = mydb.cursor()

# Creo il nuovo database per i robot se non esiste già
mycursor.execute("CREATE DATABASE IF NOT EXISTS ROBOT_DB")
# Seleziono il database ROBOT_DB per le operazioni successive
mycursor.execute("USE ROBOT_DB")

# Droppo la tabella se esiste per ricrearla con la struttura corretta
mycursor.execute("DROP TABLE IF EXISTS Robots")

# Creo la tabella Robots con le colonne specificate
mycursor.execute("""
CREATE TABLE Robots (
  id INT AUTO_INCREMENT PRIMARY KEY,  # Colonna id auto-incrementante e chiave primaria di tipo intero
  nome VARCHAR(255),  # Colonna nome di tipo stringa con lunghezza massima 255
  tipo VARCHAR(255),  # Colonna tipo di tipo stringa con lunghezza massima 255
  anno_creazione INT,  # Colonna anno_creazione di tipo intero
  autonomia_ore INT  # Colonna autonomia_ore di tipo intero
)
""")

# Apro il file CSV 'robot.csv' in modalità lettura con encoding UTF-8
with open('robot.csv', mode='r', encoding='utf-8') as file:
    # Creo un lettore CSV per il file
    lettore = csv.reader(file)
    # Salto la prima riga che contiene le intestazioni
    next(lettore) # Salta la riga id,nome,tipo...
    
    # Itero su ogni riga del file CSV
    for riga in lettore:
        # Definisco la query SQL per inserire i dati nella tabella Robots
        sql = "INSERT INTO Robots (nome, tipo, anno_creazione, autonomia_ore) VALUES (%s, %s, %s, %s)"
        # Eseguo la query SQL con i valori della riga corrente
        mycursor.execute(sql, (riga[0], riga[1], int(riga[2]), int(riga[3])))

# Confermo le modifiche al database
mydb.commit()
# Stampo un messaggio di successo
print("✅ File CSV dei robot caricato con successo nel database ROBOT_DB!")