# huvudprogram.py
from lägg_till_uppgift_modul import lägg_till_uppgift
from markera_klar_modul import markera_uppgift_som_klar
from ta_bort_uppgift_modul import ta_bort_uppgift

def huvudprogram():
    uppgifter = []  # Lista för att lagra uppgifter

    while True:
        print("\nVad vill du göra?")
        print("1: Lägg till en uppgift")
        print("2: Markera en uppgift som klar")
        print("3: Ta bort en uppgift")
        print("4: Avsluta")

        val = input("Gör ditt val (1, 2, 3 eller 4): ")

        if val == "1":
            lägg_till_uppgift(uppgifter)
        elif val == "2":
            markera_uppgift_som_klar(uppgifter)
        elif val == "3":
            ta_bort_uppgift(uppgifter)
        elif val == "4":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    huvudprogram()
