from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app) # Abilita l'accesso per Angular come richiesto dal prof

# Connessione al database con le credenziali trovate in prep_A.py
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="CLASH_ROYALE" 
)
mycursor = mydb.cursor()

# --- PARTE 1: Route base ---
@app.route("/")
def hello():
    return "<h1>Hello, World!</h1><p>Il server Flask di Aisha e' attivo e collegato correttamente!</p>"

@app.route("/getAllDataInHtml")
def getAllData():
    # Seleziona tutto dalla tabella Clash_Unit
    mycursor.execute("SELECT * FROM Clash_Unit")
    myresult = mycursor.fetchall()
    return str(myresult)

# --- PARTE 2: Nuove route filtrate ---
@app.route("/air_transport")
def airTransport():
    mycursor.execute("SELECT * FROM Clash_Unit WHERE transport = 'Air'")
    return str(mycursor.fetchall())

@app.route("/epic_units")
def epicUnits():
    mycursor.execute("SELECT * FROM Clash_Unit WHERE rarity = 'Epic'")
    return str(mycursor.fetchall())

@app.route("/fast_units")
def fastUnits():
    mycursor.execute("SELECT * FROM Clash_Unit WHERE speed = 'Fast'")
    return str(mycursor.fetchall())

@app.route("/high_damage")
def highDamage():
    mycursor.execute("SELECT * FROM Clash_Unit WHERE damage > 200")
    return str(mycursor.fetchall())

# --- PARTE 3: Formato JSON per Angular ---
@app.route("/getAllDataJSON")
def getAllDataJSON():
    mycursor.execute("SELECT * FROM Clash_Unit")
    # Questo serve per dare un nome a ogni colonna (marca, costo, ecc.)
    row_headers = [x[0] for x in mycursor.description] 
    myresult = mycursor.fetchall()
    
    json_data = []
    for result in myresult:
        json_data.append(dict(zip(row_headers, result)))
        
    return jsonify(json_data)

if __name__ == "__main__":
    app.run(debug=True)