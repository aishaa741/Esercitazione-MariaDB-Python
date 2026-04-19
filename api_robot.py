from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Configurazione Database - Verifica che i dati siano corretti per il tuo ambiente
db_config = {
    'host': 'localhost',
    'user': 'pythonuser',
    'password': 'password123',
    'database': 'ROBOT_DB'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# --- ROTTE DEL SITO (Pagine HTML) ---

@app.route("/")
def home():
    # Carica il file templates/home.html
    return render_template("home.html")

@app.route("/combattimento")
def combattimento():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Robots WHERE tipo = 'Combattimento'")
    robots = cursor.fetchall()
    conn.close()
    return render_template("table.html", 
                           titolo="DIFESA STRATEGICA", 
                           sottotitolo="Protocolli di ingaggio tattico e sicurezza perimetrale.", 
                           robots=robots, 
                           badge_text="ATTIVO", 
                           badge_class="")

@app.route("/super_batteria")
def super_batteria():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Robots WHERE autonomia_ore > 8000")
    robots = cursor.fetchall()
    conn.close()
    return render_template("table.html", 
                           titolo="SISTEMI DEEP-SPACE", 
                           sottotitolo="Metriche reattori a fusione con operatività superiore alle 8000 ore.", 
                           robots=robots, 
                           badge_text="OTTIMALE", 
                           badge_class="status-ottimale")

@app.route("/modelli_storici")
def modelli_storici():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Robots WHERE anno_creazione < 2000")
    robots = cursor.fetchall()
    conn.close()
    return render_template("table.html", 
                           titolo="ARCHIVIO LEGACY", 
                           sottotitolo="Vault di memoria a freddo. Consultazione modelli decommissionati.", 
                           robots=robots, 
                           badge_text="ARCHIVIATO", 
                           badge_class="status-archiviato")

# --- ROTTA API JSON (Quella che cercavi!) ---

@app.route("/tutti_i_robot")
def api_robots():
    conn = get_db_connection()
    # dictionary=True è fondamentale per avere il formato JSON {chiave: valore}
    cursor = conn.cursor(dictionary=True) 
    cursor.execute("SELECT * FROM Robots")
    res = cursor.fetchall()
    conn.close()
    return jsonify(res)

if __name__ == "__main__":
    # Uso la porta 5005 per evitare l'errore "Address already in use"
    app.run(debug=True, port=5005)