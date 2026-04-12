import mysql.connector

# 1. Ci colleghiamo senza specificare il database (perché dobbiamo ancora crearlo!)
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123"
)
mycursor = mydb.cursor()

# 2. Creiamo il database
mycursor.execute("CREATE DATABASE IF NOT EXISTS CLASH_ROYALE")
mycursor.execute("USE CLASH_ROYALE")

# 3. Creiamo la tabella
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Clash_Unit (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  transport VARCHAR(255),
  rarity VARCHAR(255),
  speed VARCHAR(255),
  damage INT
)
""")

# 4. Svuotiamo la tabella nel caso ci fossero vecchi dati e inseriamo 3 truppe di prova
mycursor.execute("TRUNCATE TABLE Clash_Unit")

sql = "INSERT INTO Clash_Unit (name, transport, rarity, speed, damage) VALUES (%s, %s, %s, %s, %s)"
valori = [
  ('Cucciolo di Drago', 'Air', 'Epic', 'Fast', 133),
  ('Cavaliere', 'Ground', 'Common', 'Medium', 167),
  ('Mongolfiera', 'Air', 'Epic', 'Medium', 798)
]

mycursor.executemany(sql, valori)
mydb.commit()

print("✅ Magia completata! Database CLASH_ROYALE e tabella creati con successo!")