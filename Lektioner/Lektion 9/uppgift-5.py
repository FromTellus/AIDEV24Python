try:
    tal = int(input("Ange ett tal: "))
    resultat = 100 / tal
except:
    print("Ett fel inträffade.")

# Diskussion: Att fånga alla undantag utan att specificera vilket gör att
# man inte vet vad som gick fel. Det är bättre att vara specifik med undantagen
# för att kunna hantera dem på ett korrekt sätt.