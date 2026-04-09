import mysql.connector

# 1. Mi collego a MariaDB usando l'utente creato prima
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123"
)

mycursor = mydb.cursor()

# 2. Creo il database 'Animali' (se non esiste già)
mycursor.execute("CREATE DATABASE IF NOT EXISTS Animali")

# 3. Dico al sistema di usare proprio il database 'Animali'
mycursor.execute("USE Animali")

# 4. Creo la tabella 'Mammiferi' con le colonne richieste dal prof
sql_tabella = """
CREATE TABLE IF NOT EXISTS Mammiferi (
  Id INT AUTO_INCREMENT PRIMARY KEY,
  Nome_Proprio VARCHAR(255),
  Razza VARCHAR(255),
  Peso INT,
  Eta INT
)
"""
mycursor.execute(sql_tabella)

print("Perfetto! Database 'Animali' e tabella 'Mammiferi' creati con successo!")