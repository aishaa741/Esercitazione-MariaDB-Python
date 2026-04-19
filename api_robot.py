# Importo Flask (per creare il sito), render_template (per aprire le pagine HTML) 
# e jsonify (per creare la pagina con i dati tecnici JSON)
from flask import Flask, render_template, jsonify
import mysql.connector

# Creo l'applicazione web e la chiamo "app"
app = Flask(__name__)

# Questa funzione serve per collegarsi al database ogni volta che ne abbiamo bisogno
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="pythonuser",
        password="password123",
        database="ROBOT_DB" # Dico di usare proprio il database dei robot
    )

# --- PAGINA INIZIALE ---
@app.route('/') # Quando l'utente apre l'indirizzo base (es. localhost:5005/)
def home():
    # Apri il file home.html che sta nella cartella templates
    return render_template('home.html')

# --- ROTTA 1: UNITÀ DA COMBATTIMENTO ---
@app.route('/combattimento') # Quando l'utente clicca sul primo pulsante
def combattimento():
    db = get_db_connection() # Mi collego al database
    cursor = db.cursor()     # Prendo la "penna" per scrivere il comando
    # Chiedo al database solo i robot che hanno come modello 'Combattimento'
    cursor.execute("SELECT id, nome, modello, anno_produzione, prezzo FROM robots WHERE modello = 'Combattimento'")
    robots = cursor.fetchall() # Metto i risultati in una lista chiamata 'robots'
    cursor.close() # Chiudo la penna
    db.close()     # Chiudo il database
    # Mando i dati alla pagina 'table.html' e decido i titoli da mostrare
    return render_template('table.html', 
                           robots=robots, 
                           titolo="DIFESA STRATEGICA", 
                           sottotitolo="Protocolli tattici unità d'assalto",
                           badge_text="ATTIVO",
                           badge_class="neon-blue")

# --- ROTTA 2: UNITÀ AD ALTA ENERGIA ---
@app.route('/super_batteria') # Quando l'utente clicca sul secondo pulsante
def super_batteria():
    db = get_db_connection()
    cursor = db.cursor()
    # Chiedo i robot che hanno il prezzo (energia) maggiore di 8000
    cursor.execute("SELECT id, nome, modello, anno_produzione, prezzo FROM robots WHERE prezzo > 8000")
    robots = cursor.fetchall()
    cursor.close()
    db.close()
    # Mando i dati alla pagina 'table.html' con i titoli per lo spazio
    return render_template('table.html', 
                           robots=robots, 
                           titolo="SISTEMI DEEP-SPACE", 
                           sottotitolo="Unità a lunga durata operativa",
                           badge_text="STABILE",
                           badge_class="neon-blue")

# --- ROTTA 3: ROBOT VECCHI (ARCHIVIO) ---
@app.route('/modelli_storici') # Quando l'utente clicca sul terzo pulsante
def modelli_storici():
    db = get_db_connection()
    cursor = db.cursor()
    # Chiedo i robot costruiti prima dell'anno 2000
    cursor.execute("SELECT id, nome, modello, anno_produzione, prezzo FROM robots WHERE anno_produzione < 2000")
    robots = cursor.fetchall()
    cursor.close()
    db.close()
    # Mando i dati alla pagina 'table.html' con i titoli "Legacy"
    return render_template('table.html', 
                           robots=robots, 
                           titolo="ARCHIVIO LEGACY", 
                           sottotitolo="Modelli di prima generazione (Pre-2000)",
                           badge_text="ARCHIVIATO",
                           badge_class="neon-purple")

# --- ROTTA API JSON (I DATI GREZZI) ---
@app.route('/tutti_i_robot') # Quando l'utente clicca su "System API" nella barra in alto
def tutti_i_robot():
    db = get_db_connection()
    # dictionary=True serve per far uscire i dati con i nomi (es. "nome": "Ares")
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT nome, modello, anno_produzione, prezzo FROM robots")
    robots = cursor.fetchall()
    cursor.close()
    db.close()
    # Non mando una pagina HTML, ma mando il testo grezzo in formato JSON
    return jsonify(robots)

# Se questo file viene eseguito, fai partire il server
if __name__ == '__main__':
    # host='0.0.0.0' serve per renderlo visibile nel Codespace
    # port=5005 è la porta che abbiamo scelto
    # debug=True serve per vedere gli errori se qualcosa si rompe
    app.run(host='0.0.0.0', port=5005, debug=True)