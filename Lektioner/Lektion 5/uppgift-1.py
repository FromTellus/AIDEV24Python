# Uppgift 1: Grundläggande Dictionaries – Hantera Elevers Information

# 1. Skapa en tom dictionary
elever = {}

# 2. Låt användaren mata in namn och ålder för tre elever
for _ in range(3):
    namn = input("Ange elevens namn: ")
    ålder = int(input(f"Ange {namn}s ålder: "))
    # 3. Lägg till varje elev och deras ålder i dictionaryn.'
    # Namnet blir nyckel och ålder blir värdet
    elever[namn] = ålder

# 4. Skriv ut alla elever och deras åldrar
for namn, ålder in elever.items():
    print(f"{namn} är {ålder} år gammal.")
