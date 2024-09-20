# Startvärden
i = 1
summa = 0

# While-loop som körs så länge i är mindre än eller lika med 100
while i <= 100:
    summa += i  # Lägg till det nuvarande värdet av i till summan
    i += 1  # Öka i med 1 för varje iteration

# Skriv ut den totala summan
print(f"Summan av alla heltal från 1 till 100 är: {summa}")
