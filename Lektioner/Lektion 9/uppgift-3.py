try:
    fil = open("testfil.txt", "r")
    innehåll = fil.read()
    print(innehåll)
except FileNotFoundError:
    print("Filen hittades inte!")
finally:
    try:
        fil.close()
        print("Filen är stängd.")
    except Exception:
        print("Filen öppnades aldrig.")