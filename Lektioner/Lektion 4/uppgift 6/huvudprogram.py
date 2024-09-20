# huvudprogram.py
from skriv_till_fil_modul import skriv_anteckning
from läs_från_fil_modul import läs_innehåll
from radera_fil_modul import radera_innehåll

def huvudprogram():
    filnamn = "anteckningar.txt"  # Filen som ska användas för att spara anteckningar

    while True:
        print("\nVad vill du göra?")
        print("1: Skriv en ny anteckning")
        print("2: Läs anteckningar")
        print("3: Radera alla anteckningar")
        print("4: Avsluta")

        val = input("Gör ditt val (1, 2, 3 eller 4): ")

        if val == "1":
            skriv_anteckning(filnamn)
        elif val == "2":
            läs_innehåll(filnamn)
        elif val == "3":
            radera_innehåll(filnamn)
        elif val == "4":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    huvudprogram()
