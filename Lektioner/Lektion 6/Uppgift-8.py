# Skapa en exempeltextfil
with open('text.txt', 'w') as fil:
    fil.write("Python är kul.\n")
    fil.write("Vi lär oss filhantering.\n")
    fil.write("Programmering är kraftfullt.\n")

# Räkna antal rader och ord
antal_rader = 0
antal_ord = 0

with open('text.txt', 'r') as fil:
    for rad in fil:
        antal_rader += 1
        antal_ord += len(rad.split())  # Dela raden i ord och räkna antalet ord

print(f"Antal rader: {antal_rader}")
print(f"Antal ord: {antal_ord}")
