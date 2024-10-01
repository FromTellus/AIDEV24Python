class FilFel(Exception):
    pass

def öppna_fil(filnamn):
    try:
        fil = open(filnamn, "r")
        return fil.read()
    except FileNotFoundError as e:
        raise FilFel(f"Filen {filnamn} kunde inte öppnas.") from e

try:
    innehåll = öppna_fil("testfil.txt")
    print(innehåll)
except FilFel as e:
    print(e)