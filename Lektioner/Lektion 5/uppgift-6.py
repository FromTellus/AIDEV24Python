# Uppgift 6: Sets – Fritidsintressen

# 1. Skapa två sets med fritidsintressen
ulf = set(input("Ange person 1s intressen, separerade med kommatecken: ").split(","))
magnus = set(input("Ange person 2s intressen, separerade med kommatecken: ").split(","))

# 2. Använd en for-loop för att skriva ut alla intressen för varje person

# 3. Använd union och intersection för att visa unika och gemensamma intressen
unika_intressen = ulf.union(magnus)
unika_intressen_2 = magnus.union(ulf)
gemensamma_intressen = ulf.intersection(magnus)

print(f"Unika intressen: {unika_intressen}")
print(f"Unika intressen: {unika_intressen_2}")

print(f"Gemensamma intressen: {gemensamma_intressen}")
