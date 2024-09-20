# Begär input från användaren
tal1 = float(input("Mata in det första talet: "))
tal2 = float(input("Mata in det andra talet: "))

# Visa alternativ för användaren
print("Välj en operation:")
print("1. Addition (+)")
print("2. Subtraktion (-)")
print("3. Multiplikation (*)")
print("4. Division (/)")
print("5. Exponentiering (**)")
print("6. Modulus (%)")

# Begär användarens val
val = input("Ange ditt val (1/2/3/4/5/6): ")

# Utför operationen baserat på användarens val
if val == '1':
    resultat = tal1 + tal2
    operation = "Addition"
elif val == '2':
    resultat = tal1 - tal2
    operation = "Subtraktion"
elif val == '3':
    resultat = tal1 * tal2
    operation = "Multiplikation"
elif val == '4':
    if tal2 != 0:
        resultat = tal1 / tal2
        operation = "Division"
    else:
        resultat = "ogiltig (division med noll)"
        operation = "Division"
elif val == '5':
    resultat = tal1 ** tal2
    operation = "Exponentiering"
elif val == '6':
    if tal2 != 0:
        resultat = tal1 % tal2
        operation = "Modulus"
    else:
        resultat = "ogiltig (modulus med noll)"
        operation = "Modulus"
else:
    resultat = "ogiltigt val"
    operation = "ingen giltig operation"

# Skriv ut resultatet
print(f"Resultatet av {operation} är: {resultat}")
