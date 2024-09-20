# radera_fil_modul.py
def radera_innehåll(filnamn):
    with open(filnamn, "w") as fil:  # "w" skriver över hela filen
        print(f"Innehållet i filen {filnamn} har raderats.")
