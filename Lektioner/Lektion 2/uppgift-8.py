# Variabel för att hålla reda på poängen
poäng = 0

# Fråga 1
print("Fråga 1: Vad är huvudstaden i Sverige?")
print("1) Göteborg")
print("2) Stockholm")
print("3) Malmö")
svar = input("Ange ditt svar (1/2/3): ")

if svar == "2":
    print("Rätt!")
    poäng += 1
else:
    print("Fel, rätt svar är Stockholm.")

# Fråga 2
print("\nFråga 2: Vad är 5 + 7?")
print("1) 10")
print("2) 12")
print("3) 14")
svar = input("Ange ditt svar (1/2/3): ")

if svar == "2":
    print("Rätt!")
    poäng += 1
else:
    print("Fel, rätt svar är 12.")

# Fråga 3
print("\nFråga 3: Vilken planet är den tredje från solen?")
print("1) Mars")
print("2) Venus")
print("3) Jorden")
svar = input("Ange ditt svar (1/2/3): ")

if svar == "3":
    print("Rätt!")
    poäng += 1
else:
    print("Fel, rätt svar är Jorden.")

# Skriv ut resultatet
print(f"\nDu fick {poäng} av 3 rätt!")
