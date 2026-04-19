# Importo mysql.connector per connettermi a MariaDB
import mysql.connector

# Mi collego al database
mydb = mysql.connector.connect(
  host="localhost",  # Host del database
  user="pythonuser",  # Utente del database
  password="password123",  # Password dell'utente
  database="Animali"  # Nome del database
)
# Creo un cursore per eseguire le query
mycursor = mydb.cursor()
# Definisco la query SQL per inserire i dati
sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"

# Stampo un messaggio di inizio
print("--- INSERIMENTO NUOVI ANIMALI ---")
print("Dovrai inserire 5 nuovi animali. Cominciamo!\n")

# Uso un ciclo "for" che si ripete esattamente 5 volte
for i in range(5):
    print(f"Inserimento animale numero {i+1}:")
    
    # Chiedo i dati all'utente tramite input
    nome = input("Come si chiama l'animale? ")
    razza = input("Che razza è? ")
    peso = input("Quanto pesa (in kg)? ")
    eta = input("Quanti anni ha? ")
    
    # Metto i dati digitati in una tupla
    valori = (nome, razza, peso, eta)
    
    # Inserisco questo singolo animale nel database
    mycursor.execute(sql, valori)
    print("Animale aggiunto!\n")

# Salvo le modifiche nel database alla fine del ciclo
mydb.commit()

# Stampo un messaggio di completamento
print("Finito! Hai inserito con successo 5 nuovi animali nel database.")