# Importo il "traduttore" per far parlare Python con il database (MariaDB)
import mysql.connector
# Importo lo strumento per leggere i file Excel/CSV
import csv

# Apro la connessione: dico a Python di bussare alla porta del database
mydb = mysql.connector.connect(
  host="localhost",    # Il database è su questo computer
  user="pythonuser",   # Il nome dell'utente autorizzato
  password="password123" # La chiave segreta per entrare
)

# Creo un "cursore": è come una penna che useremo per scrivere i comandi SQL
mycursor = mydb.cursor()

# Dico al database: "Se non esiste già, crea uno scaffale chiamato ROBOT_DB"
mycursor.execute("CREATE DATABASE IF NOT EXISTS ROBOT_DB")

# Dico al database di entrare dentro quello scaffale per lavorare lì
mycursor.execute("USE ROBOT_DB")

# Creo la tabella 'robots' (una griglia tipo Excel) se non c'è già
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS robots (
        id INT AUTO_INCREMENT PRIMARY KEY, # Un numero che cresce da solo per ogni robot
        nome VARCHAR(255),                 # Uno spazio per il nome (testo)
        modello VARCHAR(255),              # Uno spazio per la categoria (testo)
        anno_produzione INT,               # Uno spazio per l'anno (numero intero)
        prezzo DECIMAL(10, 2)              # Uno spazio per il prezzo (numero con la virgola)
    )
""")

# Svuoto la tabella: cancello i vecchi robot per non fare doppioni ogni volta che avvio il file
mycursor.execute("TRUNCATE TABLE robots")

# Creo un contatore che parte da zero per contare quanti robot aggiungiamo
count = 0

# Apro il file 'robot.csv' per leggerlo (modalità 'r' sta per read/leggere)
with open('robot.csv', mode='r', encoding='utf-8') as file:
    # Uso lo strumento reader per dividere le righe del file dove ci sono le virgole
    reader = csv.reader(file)
    
    # Per ogni riga che trovo dentro il file CSV...
    for row in reader:
        # Controllo che la riga non sia vuota e abbia almeno 4 pezzi di informazione
        if len(row) >= 4: 
            # Preparo il comando SQL per "infilare" i dati nella tabella
            sql = "INSERT INTO robots (nome, modello, anno_produzione, prezzo) VALUES (%s, %s, %s, %s)"
            
            # Prendo i 4 pezzi della riga e pulisco eventuali spazi inutili (strip)
            val = (row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip())
            
            # Uso la "penna" (cursore) per scrivere i dati nel database
            mycursor.execute(sql, val)
            
            # Aumento il contatore di 1 ogni volta che inserisco un robot
            count += 1

# Confermo ufficialmente le modifiche: senza questo i dati non vengono salvati davvero!
mydb.commit()

# Stampo un messaggio nel terminale per dirmi che tutto è andato bene e quanti robot ho caricato
print(f"✅ FINALMENTE! Caricati {count} robot nel database.")