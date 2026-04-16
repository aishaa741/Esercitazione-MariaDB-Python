from flask import Flask, jsonify, render_template
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

# --- LA PAGINA PRINCIPALE CON IL MENU ---
@app.route("/")
def home():
    return render_template('home.html')

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
    # fetchall() recupera tutti i risultati della query come lista di tuple
    risultati = mycursor.fetchall()
    return render_template('table.html', titolo="⚔️ Unità da Combattimento", dati=risultati)

# ROTTA 3: Robot storici (TABELLA BELLA)
@app.route("/modelli_storici")
def modelli_storici():
    mycursor.execute("SELECT * FROM Robots WHERE anno_creazione < 2000")
    risultati = mycursor.fetchall()
    return render_template('table.html', titolo="📜 Archivi Storici", dati=risultati)

# ROTTA 4: Robot con batteria infinita (TABELLA BELLA)
@app.route("/super_batteria")
def super_batteria():
    mycursor.execute("SELECT * FROM Robots WHERE autonomia_ore > 8000")
    risultati = mycursor.fetchall()
    return render_template('table.html', titolo="🔋 Modelli ad Alta Autonomia", dati=risultati)

if __name__ == "__main__":
    app.run(debug=True)