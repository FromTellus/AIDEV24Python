import datetime

# Lägg till körningslogg i 'log.txt'
with open('log.txt', 'a+') as fil:
    aktuell_tid = datetime.datetime.now()
    fil.write(f"Programmet kördes {aktuell_tid}\n")
    
    # Flytta tillbaka pekaren till början av filen innan du läser
    fil.seek(0)
    
    # Läs och skriv ut hela filens innehåll
    innehåll = fil.read()
    print(innehåll)
