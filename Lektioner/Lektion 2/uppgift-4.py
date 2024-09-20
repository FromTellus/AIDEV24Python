# Begär input från användaren
tal1 = float(input("Mata in det första talet: "))
tal2 = float(input("Mata in det andra talet: "))
tal3 = float(input("Mata in det tredje talet: "))

# Kontrollera om något tal är negativt
if tal1 < 0 or tal2 < 0 or tal3 < 0:
    print("Varning: Negativa tal är inte tillåtna.")
else:
    # Beräkna medelvärdet
    medelvärde = (tal1 + tal2 + tal3) / 3
    # Skriv ut resultatet med två decimaler
    print(f"Medelvärdet av de tre talen är: {medelvärde:.2f}")
