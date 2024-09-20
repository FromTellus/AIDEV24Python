# Be användaren om namn och ålder
namn = input("Vad heter du? ")
ålder = input("Hur gammal är du? ")

# Skriv namn och ålder till info.txt
with open('info.txt', 'w') as fil:
    fil.write(f"Namn: {namn}\n")
    fil.write(f"Ålder: {ålder}\n")
