### Lösning Uppgift 1: Läsa från en fil

# Skapa en textfil manuellt, sedan läs filen rad för rad och skriv ut varje rad
with open('uppgift-1.txt', 'r') as fil:
    for rad in fil:
        print(rad.strip())  # strip() tar bort eventuella radbrytningar
