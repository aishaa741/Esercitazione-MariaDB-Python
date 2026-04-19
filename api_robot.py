# Importa Flask per creare il sito, jsonify per i dati JSON e render_template per le pagine HTML
from flask import Flask, jsonify, render_template
# Importa il connettore che permette a Python di parlare con il database MariaDB
import mysql.connector

# Crea l'applicazione Flask e la assegna alla variabile 'app'
app = Flask(__name__)

# Crea un dizionario con i dati di accesso (indirizzo, nome utente, password e nome database)
db_config = {
    'host': 'localhost',
    'user': 'pythonuser',
    'password': 'password123',
    'database': 'ROBOT_DB'
}

# Definizione di una funzione per aprire la connessione al database ogni volta che serve
def get_db_connection():
    # Restituisce la connessione attiva usando i dati configurati sopra
    return mysql.connector.connect(**db_config)

# --- ROTTE DEL SITO (Cosa succede quando visiti i vari indirizzi) ---

# Quando l'utente va all'indirizzo principale (la Home)
@app.route("/")
def home():
    # Prende il file 'home.html' dalla cartella templates e lo mostra all'utente
    return render_template("home.html")

# Quando l'utente clicca su "DIFESA STRATEGICA" (/combattimento)
@app.route("/combattimento")
def combattimento():
    conn = get_db_connection() # Apre la connessione al database
    cursor = conn.cursor() # Crea un "cursore" (uno strumento per scrivere i comandi SQL)
    # Esegue il comando SQL per cercare solo i robot di tipo 'Combattimento'
    cursor.execute("SELECT * FROM Robots WHERE tipo = 'Combattimento'")
    robots = cursor.fetchall() # Salva tutti i risultati trovati nella variabile 'robots'
    conn.close() # Chiude la connessione per non sprecare risorse
    # Invia i dati alla pagina 'table.html' insieme a titolo e sottotitolo personalizzati
    return render_template("table.html", 
                           titolo="DIFESA STRATEGICA", 
                           sottotitolo="Protocolli di ingaggio tattico e sicurezza perimetrale.", 
                           robots=robots, 
                           badge_text="ATTIVO", 
                           badge_class="")

# Quando l'utente clicca su "SISTEMI DEEP-SPACE" (/super_batteria)
@app.route("/super_batteria")
def super_batteria():
    conn = get_db_connection() # Apre la connessione
    cursor = conn.cursor() # Prepara il cursore
    # Cerca i robot che hanno più di 8000 ore di autonomia
    cursor.execute("SELECT * FROM Robots WHERE autonomia_ore > 8000")
    robots = cursor.fetchall() # Prende i dati
    conn.close() # Chiude la connessione
    # Mostra la tabella con i dati filtrati per la batteria
    return render_template("table.html", 
                           titolo="SISTEMI DEEP-SPACE", 
                           sottotitolo="Metriche reattori a fusione con operatività superiore alle 8000 ore.", 
                           robots=robots, 
                           badge_text="OTTIMALE", 
                           badge_class="status-ottimale")

# Quando l'utente clicca su "ARCHIVIO LEGACY" (/modelli_storici)
@app.route("/modelli_storici")
def modelli_storici():
    conn = get_db_connection() # Apre la connessione
    cursor = conn.cursor() # Prepara il cursore
    # Cerca i robot creati prima dell'anno 2000
    cursor.execute("SELECT * FROM Robots WHERE anno_creazione < 2000")
    robots = cursor.fetchall() # Prende i dati
    conn.close() # Chiude la connessione
    # Mostra la tabella con i modelli vecchi
    return render_template("table.html", 
                           titolo="ARCHIVIO LEGACY", 
                           sottotitolo="Vault di memoria a freddo. Consultazione modelli decommissionati.", 
                           robots=robots, 
                           badge_text="ARCHIVIATO", 
                           badge_class="status-archiviato")

# --- ROTTA API JSON (Restituisce i dati puri, senza grafica) ---

@app.route("/tutti_i_robot")
def api_robots():
    conn = get_db_connection() # Apre la connessione
    # dictionary=True trasforma i dati in un formato "etichetta: valore" (es. 'modello': 'NEX-V1')
    cursor = conn.cursor(dictionary=True) 
    cursor.execute("SELECT * FROM Robots") # Prende TUTTI i robot della tabella
    res = cursor.fetchall() # Salva tutto
    conn.close() # Chiude la connessione
    return jsonify(res) # Trasforma la lista di Python nel formato standard JSON per il web

# Avvio del server
if __name__ == "__main__":
    # Avvia l'app in modalità debug (si riavvia da sola se cambi il codice) sulla porta 5005
    app.run(debug=True, port=5005)