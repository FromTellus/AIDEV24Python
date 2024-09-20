# Uppgift 7: Dictionary med Flera Nyckel-Värde-Par – Bokhylla

# 1. Skapa en dictionary där nycklar är bokkategorier och värden är listor av böcker
bokhylla = {}

# 2. Låt användaren mata in böcker i olika kategorier
for _ in range(3):
    kategori = input("Ange bokkategori: ")
    bok = input(f"Ange en bok inom {kategori}: ")
    if kategori not in bokhylla:
        bokhylla[kategori] = []
    bokhylla[kategori].append(bok)

# 3. Skriv ut alla böcker i en specifik kategori
kategori_vald = input("Ange en kategori för att se alla böcker: ")
if kategori_vald in bokhylla:
    print(f"Böcker i kategorin {kategori_vald}: {bokhylla[kategori_vald]}")
else:
    print(f"Kategorin {kategori_vald} finns inte.")

# skapa en funktion som lägger ihop saker

def add(a, b):
    return a + b

#skapa en funktion som låter användaren spara namn och telefonnummer i en dict
def save_contact():
    contacts = {}
    while True:
        name = input("Ange namn: ")
        if name == "":
            break
        number = input("Ange telefonnummer: ")
        contacts[name] = number
    return contacts
