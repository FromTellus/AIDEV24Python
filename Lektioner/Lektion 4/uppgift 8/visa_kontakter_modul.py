# visa_kontakter_modul.py
def visa_kontakter(filnamn):
    try:
        # Öppna filen i läsläge ("r")
        with open(filnamn, "r") as fil:
            kontakter = fil.readlines()
            if kontakter:
                print("\nLista över alla kontakter:")
                for kontakt in kontakter:
                    namn, telefonnummer = kontakt.strip().split(",")
                    print(f"Namn: {namn}, Telefonnummer: {telefonnummer}")
            else:
                print("Inga kontakter hittades.")
    except FileNotFoundError:
        print(f"Filen {filnamn} hittades inte.")
