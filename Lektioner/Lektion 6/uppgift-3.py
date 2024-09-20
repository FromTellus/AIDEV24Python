### Lösning Uppgift 3: Hantera filoperationer med undantag

try:
    # Be användaren om filnamn
    filnamn = input("Ange filnamnet du vill öppna: ")

    # Försök att öppna och läsa filen
    with open(filnamn, 'r') as fil:
        innehåll = fil.read()
        print("Filens innehåll:")
        print(innehåll)

except FileNotFoundError:
    # Hantera felet om filen inte hittas
    print(f"Fel: Filen '{filnamn}' hittades inte.")