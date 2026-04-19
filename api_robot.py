from flask import Flask, jsonify, render_template  # importa le classi Flask per gestire l'app, le risposte JSON e il rendering dei template
import mysql.connector  # importa il connettore MySQL per gestire la connessione al database

app = Flask(__name__)  # crea l'istanza dell'app Flask usando il nome del modulo corrente

# Configurazione del database, salvata in un dizionario per facilità di riuso
db_config = {
    'host': 'localhost',  # hostname del server MariaDB/MySQL
    'user': 'pythonuser',  # nome utente usato per connettersi al database
    'password': 'password123',  # password dell'utente database
    'database': 'ROBOT_DB'  # nome del database da utilizzare
}

# Funzione utility per aprire una nuova connessione al database quando serve
def get_db_connection():
    return mysql.connector.connect(**db_config)  # passa l'intero dizionario di configurazione a mysql.connector.connect

@app.route("/")  # definisce la route principale dell'applicazione
def home():
    return render_template("home.html")  # restituisce il template home.html per la homepage

@app.route("/tutti_i_robot")  # definisce l'endpoint che restituisce i dati JSON di tutti i robot
def tutti_i_robot():
    conn = get_db_connection()  # apre una nuova connessione al database
    cursor = conn.cursor(dictionary=True)  # crea un cursore che restituisce righe come dizionari
    cursor.execute("SELECT * FROM Robots")  # esegue la query per leggere tutte le righe della tabella Robots
    res = cursor.fetchall()  # legge tutti i risultati della query
    conn.close()  # chiude la connessione al database
    return jsonify(res)  # converte i risultati in JSON e li restituisce al client

# Funzione helper che costruisce una pagina reparto renderizzando il template table.html
def render_reparto_page(titolo, sottotitolo, query, badge_class, badge_text):
    conn = get_db_connection()  # apre connessione al database
    cursor = conn.cursor()  # crea un cursore standard
    cursor.execute(query)  # esegue la query specificata per il reparto
    robots = cursor.fetchall()  # legge tutti i robot risultati dalla query
    conn.close()  # chiude la connessione dopo l'uso
    return render_template(
        "table.html",  # template Jinja2 che serve la pagina reparto
        titolo=titolo,  # titolo della pagina visualizzato nell'intestazione
        sottotitolo=sottotitolo,  # sottotitolo che descrive il reparto
        robots=robots,  # dati robot da mostrare nella tabella
        badge_class=badge_class,  # classe CSS personalizzata per lo stato del badge
        badge_text=badge_text,  # testo visualizzato nel badge di stato
    )

@app.route("/combattimento")  # route per la pagina del reparto combattimento
def combattimento():
    return render_reparto_page(
        "DIFESA STRATEGICA",  # titolo della pagina reparto
        "Terminale di controllo per le unità d'assalto e mantenimento della pace.",  # descrizione del reparto
        "SELECT * FROM Robots WHERE tipo = 'Combattimento'",  # query per selezionare robot di tipo Combattimento
        "status-attivo",  # classe CSS per il badge di stato
        "ATTIVO",  # testo del badge di stato
    )

@app.route("/super_batteria")  # route per la pagina dei robot ad alta autonomia
def super_batteria():
    return render_reparto_page(
        "SISTEMI DEEP-SPACE",  # titolo della pagina reparto
        "Monitoraggio decadimento reattori e stato di conservazione energetica.",  # descrizione del reparto
        "SELECT * FROM Robots WHERE autonomia_ore > 8000",  # query per selezionare robot con autonomia oltre 8000 ore
        "status-ottimale",  # classe CSS per badge ottimale
        "OTTIMALE",  # testo del badge di stato
    )

@app.route("/modelli_storici")  # route per la pagina dell'archivio storico
def modelli_storici():
    return render_reparto_page(
        "ARCHIVIO LEGACY",  # titolo della pagina reparto
        "Accesso in sola lettura ai modelli storici decommissionati.",  # descrizione del reparto
        "SELECT * FROM Robots WHERE anno_creazione < 2000",  # query per selezionare robot creati prima del 2000
        "status-archiviato",  # classe CSS per badge archiviato
        "ARCHIVIATO",  # testo del badge di stato
    )

if __name__ == "__main__":  # controlla che lo script sia eseguito direttamente e non importato
    app.run(debug=True)  # avvia il server Flask in modalità debug
