# läs_från_fil_modul.py
def läs_innehåll(filnamn):
    try:
        with open(filnamn, "r") as fil:
            innehåll = fil.read()
            if innehåll:
                print("Filens innehåll:")
                print(innehåll)
            else:
                print("Filen är tom.")
    except FileNotFoundError:
        print(f"Filen {filnamn} finns inte.")
