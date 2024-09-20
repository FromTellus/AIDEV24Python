# huvudprogram.py
from lägg_till_bok_modul import lägg_till_bok
from låna_bok_modul import låna_bok
from returnera_bok_modul import returnera_bok

def huvudprogram():
    bibliotek = []  # Lista för att lagra böcker i biblioteket

    while True:
        print("\nVad vill du göra?")
        print("1: Lägg till en ny bok")
        print("2: Låna en bok")
        print("3: Returnera en bok")
        print("4: Avsluta")

        val = input("Gör ditt val (1, 2, 3 eller 4): ")

        if val == "1":
            lägg_till_bok(bibliotek)
        elif val == "2":
            låna_bok(bibliotek)
        elif val == "3":
            returnera_bok(bibliotek)
        elif val == "4":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    huvudprogram()
