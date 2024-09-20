# Uppgift 9: Kombinera Tupler och Dictionaries – Personregister

# 1. Skapa en dictionary där varje nyckel är en persons namn och värdet är en tuple med ålder och stad
personregister = {}

# 2. Låt användaren mata in information om tre personer
for _ in range(3):
    namn = input("Ange personens namn: ")
    ålder = int(input(f"Ange {namn}s ålder: "))
    stad = input(f"Ange vilken stad {namn} bor i: ")
    personregister[namn] = (ålder, stad)

# 3. Skriv ut alla personer och deras information
for namn, info in personregister.items():
    ålder, stad = info
    print(f"{namn} är {ålder} år gammal och bor i {stad}.")

# 4. Använd en for-loop för att skriva ut namnen på personer som är äldre än 30 år
print("Personer äldre än 30 år:")
for namn, info in personregister.items():
    ålder = info[0]
    if ålder > 30:
        print(namn)
