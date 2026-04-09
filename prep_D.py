import mysql.connector

# 1. Mi collego al database
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="Animali"
)
mycursor = mydb.cursor()
sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"

print("--- INSERIMENTO NUOVI ANIMALI ---")
print("Dovrai inserire 5 nuovi animali. Cominciamo!\n")

# 2. Uso un ciclo "for" che si ripete esattamente 5 volte
for i in range(5):
    print(f"Inserimento animale numero {i+1}:")
    
    # 3. Chiedo i dati all'utente (la funzione input serve per scrivere da tastiera)
    nome = input("Come si chiama l'animale? ")
    razza = input("Che razza è? ")
    peso = input("Quanto pesa (in kg)? ")
    eta = input("Quanti anni ha? ")
    
    # 4. Metto i dati digitati in una tupla (un pacchetto)
    valori = (nome, razza, peso, eta)
    
    # 5. Inserisco questo singolo animale nel database
    mycursor.execute(sql, valori)
    print("Animale aggiunto!\n")

# 6. Salvo le modifiche nel database alla fine del ciclo
mydb.commit()

print("Finito! Hai inserito con successo 5 nuovi animali nel database.")