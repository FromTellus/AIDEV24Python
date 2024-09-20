# sök_kontakt_modul.py
def sök_kontakt(filnamn):
    söknamn = input("Ange namnet på kontakten du söker efter: ").lower()
    try:
        with open(filnamn, "r") as fil:
            for kontakt in fil:
                namn, telefonnummer = kontakt.strip().split(",")
                if namn.lower() == söknamn:
                    print(f"\nKontakt hittad: Namn: {namn}, Telefonnummer: {telefonnummer}")
                    return
            print(f"Ingen kontakt med namnet '{söknamn}' hittades.")
    except FileNotFoundError:
        print(f"Filen {filnamn} hittades inte.")
