# Uppgift 2: Tupler – Koordinater för Städer

# 1. Skapa en tuple med stad, latitud och longitud
stad = ("Stockholm", 59.3293, 18.0686)

# 2. Skriv ut informationen om staden
print(f"Stad: {stad[0]}, Latitud: {stad[1]}, Longitud: {stad[2]}")

# 3. Be användaren skapa tre tupler för tre olika städer
städer = []
for _ in range(3):
    namn = input("Ange stadens namn: ")
    latitud = float(input(f"Ange latitud för {namn}: "))
    longitud = float(input(f"Ange longitud för {namn}: "))
    stad = (namn, latitud, longitud)
    städer.append(stad)

# Skriv ut informationen om alla städer
for stad in städer:
    print(f"Stad: {stad[0]}, Latitud: {stad[1]}, Longitud: {stad[2]}")
