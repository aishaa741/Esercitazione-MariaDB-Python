import mysql.connector

# 1. Mi collego al database 'Animali'
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="Animali"
)

mycursor = mydb.cursor()

# 2. Uso il comando SQL 'SELECT *' che significa "Seleziona TUTTO" dalla tabella
mycursor.execute("SELECT * FROM Mammiferi")

# 3. Prendo tutti i risultati trovati e li salvo in una variabile
risultati = mycursor.fetchall()

# 4. Uso un ciclo per stampare ogni animale riga per riga
print("--- ELENCO DEGLI ANIMALI NEL DATABASE ---")
for animale in risultati:
  print(animale)