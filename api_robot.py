from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Connessione al database
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="ROBOT_DB"
)
mycursor = mydb.cursor()

# --- FUNZIONE MAGICA PER CREARE LE TABELLE LUMINOSE ---
def crea_pagina_bella(titolo, dati_robot):
    html_tabella = ""
    for r in dati_robot:
        html_tabella += f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}h</td></tr>"
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background-color: #121212; color: white; text-align: center; padding: 50px; }}
            h1 {{ color: #00e5ff; text-shadow: 0 0 10px #00e5ff; margin-bottom: 30px; }}
            table {{ margin: auto; border-collapse: collapse; width: 80%; background: #1e1e1e; border-radius: 10px; overflow: hidden; box-shadow: 0 8px 32px rgba(0,229,255,0.2); }}
            th, td {{ padding: 15px; border-bottom: 1px solid #333; text-align: center; }}
            th {{ background-color: #00e5ff; color: #121212; text-transform: uppercase; font-weight: bold; }}
            tr:hover {{ background-color: #282828; }}
            .back-btn {{ display: inline-block; margin-top: 30px; padding: 12px 25px; background: transparent; color: #00e5ff; border: 2px solid #00e5ff; text-decoration: none; border-radius: 8px; transition: 0.3s; font-weight: bold; }}
            .back-btn:hover {{ background: #00e5ff; color: #121212; box-shadow: 0 0 15px #00e5ff; }}
        </style>
    </head>
    <body>
        <h1>{titolo}</h1>
        <table>
            <tr>
                <th>ID</th><th>NOME</th><th>TIPO</th><th>ANNO</th><th>AUTONOMIA</th>
            </tr>
            {html_tabella}
        </table>
        <a href="/" class="back-btn">⬅ Torna alla Home</a>
    </body>
    </html>
    """

# --- LA PAGINA PRINCIPALE CON IL MENU ---
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <title>Database Robot di Aisha</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background-color: #121212; color: #ffffff; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .container { background-color: #1e1e1e; padding: 40px; border-radius: 15px; box-shadow: 0 8px 32px rgba(0, 229, 255, 0.2); text-align: center; border: 1px solid #333; }
            h1 { color: #00e5ff; margin-bottom: 10px; text-shadow: 0 0 10px #00e5ff; }
            .btn { display: block; background-color: #00e5ff; color: #121212; padding: 15px; margin: 15px auto; text-decoration: none; font-weight: bold; border-radius: 8px; transition: 0.3s; width: 250px; }
            .btn:hover { background-color: #ffffff; transform: scale(1.05); box-shadow: 0 0 15px #00e5ff; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🤖 ROBOT SYSTEM API</h1>
            <p>Seleziona un'opzione per accedere ai dati:</p>
            <a href="/tutti_i_robot" class="btn">🔌 DATI GREZZI (JSON)</a>
            <a href="/combattimento" class="btn">⚔️ COMBATTIMENTO</a>
            <a href="/modelli_storici" class="btn">📜 ARCHIVI STORICI</a>
            <a href="/super_batteria" class="btn">🔋 ALTA DURATA</a>
        </div>
    </body>
    </html>
    """

# ROTTA 1: Tutti i robot (QUESTA RIMANE IN FORMATO JSON)
@app.route("/tutti_i_robot")
def tutti_i_robot():
    mycursor.execute("SELECT * FROM Robots")
    row_headers = [x[0] for x in mycursor.description] 
    myresult = mycursor.fetchall()
    json_data = [dict(zip(row_headers, result)) for result in myresult]
    return jsonify(json_data)

# ROTTA 2: Solo i robot da combattimento (TABELLA BELLA)
@app.route("/combattimento")
def combattimento():
    mycursor.execute("SELECT * FROM Robots WHERE tipo = 'Combattimento'")
    risultati = mycursor.fetchall()
    return crea_pagina_bella("⚔️ Unità da Combattimento", risultati)

# ROTTA 3: Robot storici (TABELLA BELLA)
@app.route("/modelli_storici")
def modelli_storici():
    mycursor.execute("SELECT * FROM Robots WHERE anno_creazione < 2000")
    risultati = mycursor.fetchall()
    return crea_pagina_bella("📜 Archivi Storici", risultati)

# ROTTA 4: Robot con batteria infinita (TABELLA BELLA)
@app.route("/super_batteria")
def super_batteria():
    mycursor.execute("SELECT * FROM Robots WHERE autonomia_ore > 8000")
    risultati = mycursor.fetchall()
    return crea_pagina_bella("🔋 Modelli ad Alta Autonomia", risultati)

if __name__ == "__main__":
    app.run(debug=True)