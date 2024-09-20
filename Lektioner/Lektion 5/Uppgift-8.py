# Uppgift 8: Kontrollstrukturer och Dictionaries – Produktfiltrering

# 1. Skapa en dictionary där nycklar är produktnamn och värden är priser
produkter = {}

# 2. Låt användaren mata in produkter och deras priser
for _ in range(3):
    produkt = input("Ange produktens namn: ")
    pris = float(input(f"Ange priset för {produkt}: "))
    produkter[produkt] = pris

# 3. Be användaren mata in ett maxpris och använd en for-loop för att visa produkter inom budget
maxpris = float(input("Ange ett maxpris: "))
print(f"Produkter inom budgeten på {maxpris} kr:")
for produkt, pris in produkter.items():
    if pris <= maxpris:
        print(f"{produkt}: {pris} kr")
