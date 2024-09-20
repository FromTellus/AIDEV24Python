# Begär input från användaren
tal1 = float(input("Mata in det första talet: "))
tal2 = float(input("Mata in det andra talet: "))

# Utför de aritmetiska operationerna
summa = tal1 + tal2
skillnad = tal1 - tal2
produkt = tal1 * tal2

# Hantera division och undvik division med noll
if tal2 != 0:
    kvot = tal1 / tal2
else:
    kvot = "Ogiltig (division med noll är inte tillåten)"

# Skriv ut resultaten
print(f"Summan av talen är: {summa}")
print(f"Skillnaden mellan talen är: {skillnad}")
print(f"Produkten av talen är: {produkt}")
print(f"Kvoten av talen är: {kvot}")

