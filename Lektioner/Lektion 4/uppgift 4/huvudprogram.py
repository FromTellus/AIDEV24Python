# huvudprogram.py
from lägg_till_modul import lägg_till_användare
from sök_modul import sök_användare
from visa_modul import visa_alla_användare

def huvudprogram():
    användare = []  # Lista för att lagra användare

    while True:
        print("\nVad vill du göra?")
        print("1: Lägg till en användare")
        print("2: Sök efter en användare")
        print("3: Visa alla användare")
        print("4: Avsluta")

        val = input("Gör ditt val (1, 2, 3 eller 4): ")

        if val == "1":
            lägg_till_användare(användare)
        elif val == "2":
            sök_användare(användare)
        elif val == "3":
            visa_alla_användare(användare)
        elif val == "4":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    huvudprogram()
