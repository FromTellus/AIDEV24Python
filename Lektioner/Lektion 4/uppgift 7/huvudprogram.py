# huvudprogram.py
from lägg_till_recept_modul import lägg_till_recept
from sök_recept_modul import sök_recept
from lista_recept_modul import lista_recept

def huvudprogram():
    receptlista = []  # Lista för att lagra recept

    while True:
        print("\nVad vill du göra?")
        print("1: Lägg till ett nytt recept")
        print("2: Sök efter ett recept")
        print("3: Lista alla recept")
        print("4: Avsluta")

        val = input("Gör ditt val (1, 2, 3 eller 4): ")

        if val == "1":
            lägg_till_recept(receptlista)
        elif val == "2":
            sök_recept(receptlista)
        elif val == "3":
            lista_recept(receptlista)
        elif val == "4":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    huvudprogram()
