# sök_modul.py
def sök_användare(användare):
    namn = input("Ange namnet på användaren du vill söka efter: ")
    for person in användare:
        if person["namn"].lower() == namn.lower():
            print(f"Användare hittad: {person['namn']}, Ålder: {person['ålder']}")
            return
    print(f"Användaren {namn} hittades inte.")
