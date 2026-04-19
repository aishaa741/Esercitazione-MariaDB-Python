# Importo Flask e jsonify per creare l'API
from flask import Flask, jsonify
# Importo CORS per abilitare le richieste cross-origin
from flask_cors import CORS
# Importo mysql.connector per connettermi a MariaDB
import mysql.connector

# Creo l'applicazione Flask
app = Flask(__name__)
# Abilito CORS per l'accesso da Angular
CORS(app) # Abilita l'accesso per Angular come richiesto dal prof

# Connessione al database con le credenziali specificate
mydb = mysql.connector.connect(
  host="localhost",  # Host del database
  user="pythonuser",  # Utente del database
  password="password123",  # Password dell'utente
  database="CLASH_ROYALE"  # Nome del database
)
# Creo un cursore per eseguire le query
mycursor = mydb.cursor()

# Definisco la rotta base che restituisce un messaggio di benvenuto
@app.route("/")
def hello():
    # Restituisco un HTML semplice
    return "<h1>Hello, World!</h1><p>Il server Flask di Aisha e' attivo e collegato correttamente!</p>"

# Definisco la rotta per ottenere tutti i dati in formato HTML
@app.route("/getAllDataInHtml")
def getAllData():
    # Eseguo la query per selezionare tutto dalla tabella Clash_Unit
    mycursor.execute("SELECT * FROM Clash_Unit")
    # Ottengo tutti i risultati
    myresult = mycursor.fetchall()
    # Restituisco i risultati come stringa
    return str(myresult)

# Definisco la rotta per le unità di trasporto aereo
@app.route("/air_transport")
def airTransport():
    # Eseguo la query per selezionare le unità con transport = 'Air'
    mycursor.execute("SELECT * FROM Clash_Unit WHERE transport = 'Air'")
    # Restituisco i risultati come stringa
    return str(mycursor.fetchall())

# Definisco la rotta per le unità epiche
@app.route("/epic_units")
def epicUnits():
    # Eseguo la query per selezionare le unità con rarity = 'Epic'
    mycursor.execute("SELECT * FROM Clash_Unit WHERE rarity = 'Epic'")
    # Restituisco i risultati come stringa
    return str(mycursor.fetchall())

# Definisco la rotta per le unità veloci
@app.route("/fast_units")
def fastUnits():
    # Eseguo la query per selezionare le unità con speed = 'Fast'
    mycursor.execute("SELECT * FROM Clash_Unit WHERE speed = 'Fast'")
    # Restituisco i risultati come stringa
    return str(mycursor.fetchall())

# Definisco la rotta per le unità con alto danno
@app.route("/high_damage")
def highDamage():
    # Eseguo la query per selezionare le unità con damage > 200
    mycursor.execute("SELECT * FROM Clash_Unit WHERE damage > 200")
    # Restituisco i risultati come stringa
    return str(mycursor.fetchall())

# Definisco la rotta per ottenere tutti i dati in formato JSON
@app.route("/getAllDataJSON")
def getAllDataJSON():
    # Eseguo la query per selezionare tutto dalla tabella Clash_Unit
    mycursor.execute("SELECT * FROM Clash_Unit")
    # Ottengo i nomi delle colonne
    row_headers = [x[0] for x in mycursor.description] 
    # Ottengo tutti i risultati
    myresult = mycursor.fetchall()
    
    # Inizializzo la lista per i dati JSON
    json_data = []
    # Itero sui risultati per creare dizionari
    for result in myresult:
        json_data.append(dict(zip(row_headers, result)))
        
    # Restituisco i dati in formato JSON
    return jsonify(json_data)

# Se il file è eseguito direttamente, avvio l'app Flask in modalità debug
if __name__ == "__main__":
    app.run(debug=True)