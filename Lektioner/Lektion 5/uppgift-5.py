# Uppgift 5: Tupler – Koordinater för Platser

# 1. Skapa en tuple som representerar latitud och longitud för en plats
plats1 = (59.3293, 18.0686)  # Stockholm

# 2. Skriv ut informationen om platsen
print(f"Plats 1 - Latitud: {plats1[0]}, Longitud: {plats1[1]}")

# 3. Skapa en lista med tre tupler som representerar koordinater för tre olika platser
platser = [
    (59.3293, 18.0686),  # Stockholm
    (40.7128, -74.0060), # New York
    (35.6895, 139.6917)  # Tokyo
]

# 4. Iterera över listan och skriv ut informationen om varje plats
index = 1
for plats in platser:
    print(f"Plats {index} - Latitud: {plats[0]}, Longitud: {plats[1]}")
    index += 1
