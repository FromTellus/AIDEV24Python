# Begär input från användaren

tal = int(input("Mata in ett heltal: "))

# Kontrollera om talet är jämnt eller udda
if tal % 2 == 0:
    resultat = "jämnt"
else:
    resultat = "udda"

# Skriv ut resultatet
print(f"Talet {tal} är {resultat}.")
