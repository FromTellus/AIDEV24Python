# Skapa ett fördefinierat set med färger
predefinierade_färger = {"röd", "grön", "blå"}

# Be användaren om att mata in sina färger (avgränsade med kommatecken)
användarfärger = input("Ange några färger separerade med kommatecken: ").strip().split(',')

# Omvandla användarfärger till ett set för att få unika värden
användarfärger_set = set(användarfärger)


# Visa alla unika färger genom att kombinera båda setsen (union)
unika_färger = användarfärger_set.union(predefinierade_färger)
print(f"Alla unika färger: {unika_färger}")

# Visa de färger som finns i båda setsen (intersection)
gemensamma_färger = användarfärger_set.intersection(predefinierade_färger)
print(f"Färger som finns i båda setsen: {gemensamma_färger}")
