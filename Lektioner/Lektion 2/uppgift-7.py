# Begär input från användaren
pris1 = float(input("Mata in priset på den första varan: "))
pris2 = float(input("Mata in priset på den andra varan: "))
pris3 = float(input("Mata in priset på den tredje varan: "))

# Beräkna totalkostnaden exklusive moms
totalkostnad = pris1 + pris2 + pris3

# Lägg till moms (25%)
totalkostnad_moms = totalkostnad * 1.25

# Kolla om rabatt ska appliceras
if totalkostnad_moms > 500:
    slutpris = totalkostnad_moms * 0.9  # 10% rabatt
    print(f"Du får 10% rabatt eftersom totalbeloppet överstiger 500 SEK.")
else:
    slutpris = totalkostnad_moms

# Skriv ut slutpriset
print(f"Slutpriset inklusive moms är: {slutpris:.2f} SEK")