# Skapa en tom inköpslista
inkopslista = []

# Funktion för att visa menyn
def visa_meny():
    print("\nVälj ett alternativ:")
    print("1. Lägg till en vara")
    print("2. Ta bort en vara")
    print("3. Visa inköpslistan")
    print("4. Avsluta")

# Huvudprogrammet som körs i en while-loop
while True:
    visa_meny()
    val = input("Ange ditt val (1-4): ")

    if val == "1":
        # Lägg till en vara
        vara = input("Ange namnet på varan du vill lägga till: ")
        inkopslista.append(vara)
        print(f"{vara} har lagts till i inköpslistan.")

    elif val == "2":
        # Ta bort en vara
        vara = input("Ange namnet på varan du vill ta bort: ")
        if vara in inkopslista:
            inkopslista.remove(vara)
            print(f"{vara} har tagits bort från inköpslistan.")
        else:
            print(f"{vara} finns inte i inköpslistan.")

    elif val == "3":
        # Visa inköpslistan
        if len(inkopslista) == 0:
            print("Inköpslistan är tom.")
        else:
            print("Inköpslistan:")
            for item in inkopslista:
                print(f"- {item}")

    elif val == "4":
        # Avsluta programmet
        print("Avslutar programmet...")
        break

    else:
        print("Ogiltigt val. Försök igen.")
