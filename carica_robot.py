# Importa la libreria per permettere a Python di comandare MariaDB
import mysql.connector
# Importa la libreria per leggere i file in formato CSV (quelli con i dati separati da virgole)
import csv

# Crea il collegamento con il server MariaDB che gira sul computer (localhost)
mydb = mysql.connector.connect(
  host="localhost",    # L'indirizzo del server (il computer stesso)
  user="pythonuser",   # Il nome dell'utente che abbiamo creato prima
  password="password123"  # La chiave di accesso per l'utente
)

# Crea il 'cursore', ovvero l'oggetto che invia fisicamente i comandi SQL al database
mycursor = mydb.cursor()

# Invia il comando per creare il database 'ROBOT_DB' se non è già presente
mycursor.execute("CREATE DATABASE IF NOT EXISTS ROBOT_DB")

# Dice al sistema di entrare nel database 'ROBOT_DB' per iniziare a lavorarci dentro
mycursor.execute("USE ROBOT_DB")

# Cancella la tabella 'Robots' se esiste già (serve per ricominciare da zero e non avere errori)
mycursor.execute("DROP TABLE IF EXISTS Robots")

# Crea la tabella 'Robots' definendo quali tipi di dati può contenere ogni colonna
mycursor.execute("""
CREATE TABLE Robots (
  id INT AUTO_INCREMENT PRIMARY KEY,  # Un numero unico che cresce da solo per ogni robot
  nome VARCHAR(255),                  # Testo per il nome (massimo 255 lettere)
  tipo VARCHAR(255),                  # Testo per la categoria (es. Combattimento)
  anno_creazione INT,                 # Numero intero per l'anno
  autonomia_ore INT                   # Numero intero per la durata della batteria
)
""")

# Apre il file 'robot.csv' per leggerlo, assicurandosi di leggere bene accenti e simboli (utf-8)
with open('robot.csv', mode='r', encoding='utf-8') as file:
    # Crea uno strumento ('lettore') che sa come dividere le righe del CSV
    lettore = csv.reader(file)
    
    # Salta la prima riga del file CSV (perché contiene i titoli delle colonne, non i dati)
    next(lettore) 
    
    # Inizia un ciclo che legge i robot uno per uno, riga dopo riga
    for riga in lettore:
        # Prepara lo schema del comando per inserire i dati (i %s sono dei segnaposto)
        sql = "INSERT INTO Robots (nome, tipo, anno_creazione, autonomia_ore) VALUES (%s, %s, %s, %s)"
        
        # Inserisce i dati della riga corrente al posto dei segnaposto (%s)
        # riga[0] è il nome, riga[1] il tipo, ecc. (int() trasforma il testo in numero)
        mycursor.execute(sql, (riga[0], riga[1], int(riga[2]), int(riga[3])))

# Salva definitivamente tutte le modifiche nel database (senza questo, i dati andrebbero persi)
mydb.commit()

# Stampa a video un messaggio per confermare che tutto è andato bene
print("✅ File CSV dei robot caricato con successo nel database ROBOT_DB!")