# Uppgift 4: Dictionary med Kontrollstrukturer – Födelsedagsbok

# 1. Skapa en tom dictionary
födelsedagar = {}

# 2. Låt användaren mata in namn och födelsedatum för tre personer
for _ in range(3):
    namn = input("Ange personens namn: ")
    födelsedatum = input(f"Ange {namn}s födelsedatum (ÅÅÅÅ-MM-DD): ")
    födelsedagar[namn] = födelsedatum

# 3. Skriv ut alla personer och deras födelsedatum
for namn, datum in födelsedagar.items():
    print(f"{namn} fyller år den {datum}.")

# 4. Låt användaren kontrollera om en person finns i dictionaryn
sök_namn = input("Ange ett namn för att kontrollera födelsedatum: ")
if sök_namn in födelsedagar:
    print(f"{sök_namn} fyller år den {födelsedagar[sök_namn]}.")
else:
    print(f"{sök_namn} finns inte i födelsedagsboken.")
