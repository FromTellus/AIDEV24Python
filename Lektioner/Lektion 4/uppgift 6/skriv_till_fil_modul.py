# skriv_till_fil_modul.py
def skriv_anteckning(filnamn):
    with open(filnamn, "a") as fil:  # "a" står för append, lägg till i filen
        anteckning = input("Skriv din anteckning: ")
        fil.write(anteckning + "\n")
        print("Anteckningen har sparats.")
