# huvudprogram.py
from lägg_till_kontakt_modul import lägg_till_kontakt
from visa_kontakter_modul import visa_kontakter
from sök_kontakt_modul import sök_kontakt

def huvudprogram():
    filnamn = "kontakter.txt"  # Filen där kontakterna sparas

    while True:
        print("\nVad vill du göra?")
        print("1: Lägg till en ny kontakt")
        print("2: Visa alla kontakter")
        print("3: Sök efter en kontakt")
        print("4: Avsluta")

        val = input("Gör ditt val (1, 2, 3 eller 4): ")

        if val == "1":
            lägg_till_kontakt(filnamn)
        elif val == "2":
            visa_kontakter(filnamn)
        elif val == "3":
            sök_kontakt(filnamn)
        elif val == "4":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    huvudprogram()
