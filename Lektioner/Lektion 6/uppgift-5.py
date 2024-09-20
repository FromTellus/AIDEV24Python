# Samla fruktnamn från användaren och skriv till en fil
frukter = []
for _ in range(5):
    frukt = input("Mata in ett fruktnamn: ")
    frukter.append(frukt)

with open('frukter.txt', 'w') as fil:
    for frukt in frukter:
        fil.write(frukt + "\n")

# Läs och skriv ut frukterna från filen
with open('frukter.txt', 'r') as fil:
    for rad in fil:
        print(rad.strip())
