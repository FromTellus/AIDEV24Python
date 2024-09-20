# Begär input från användaren
pris = float(input("Mata in priset på varan: "))

# Fråga om användaren vill ge dricks
ge_dricks = input("Vill du ge dricks? (ja/nej): ").lower()

# Hantera dricks
if ge_dricks == "ja":
    dricks = pris * 0.1
    pris += dricks
    print(f"Dricks på 10% har lagts till. Dricks: {dricks:.2f} SEK")

# Skriv ut slutpriset
print(f"Slutpriset inklusive dricks är: {pris:.2f} SEK")
