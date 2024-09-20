# Be användaren om ett ord att söka efter
sökord = input("Ange ett ord att söka efter i filen: ").lower()

# Öppna och söka i filen
antal_förekomster = 0
with open('text.txt', 'r') as fil:
    for rad in fil:
        # Dela upp raden i ord och räkna förekomster
        ord_i_raden = rad.lower().split()  # Gör ordlistan case-insensitive
        antal_förekomster += ord_i_raden.count(sökord)

print(f"Ordet '{sökord}' förekommer {antal_förekomster} gånger i filen.")
