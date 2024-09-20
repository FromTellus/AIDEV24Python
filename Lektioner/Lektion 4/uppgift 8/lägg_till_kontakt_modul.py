# lägg_till_kontakt_modul.py
def lägg_till_kontakt(filnamn):
    namn = input("Ange kontaktens namn: ")
    telefonnummer = input("Ange kontaktens telefonnummer: ")
    
    # Öppna filen i tilläggsläge ("a")
    with open(filnamn, "a") as fil:
        fil.write(f"{namn},{telefonnummer}\n")
        print(f"Kontakten {namn} har sparats.")
