# Be användaren mata in heltal, separerade med mellanslag
tal_input = input("Ange heltal, separerade med mellanslag: ")

# Konvertera inmatningen till en lista av heltal
tal_lista = [int(tal) for tal in tal_input.split()]

# Kontrollera att listan inte är tom
if len(tal_lista) == 0:
    print("Du angav inga tal.")
else:
    # Beräkna summan av alla tal i listan
    summa = sum(tal_lista)

    # Beräkna medelvärdet genom att dividera summan med antalet tal
    medelvarde = summa / len(tal_lista)

    # Skriv ut medelvärdet
    print(f"Medelvärdet av de angivna talen är: {medelvarde:.2f}")
