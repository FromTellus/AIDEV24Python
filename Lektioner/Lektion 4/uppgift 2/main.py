from filter_letter import filter_letter
from filter_length import filter_length

def huvudprogram():
    # Användaren matar in en lista av strängar
    lista = input("Skriv in strängar separerade med kommatecken: ").split(',')

    print("Vad vill du göra?")
    print("1: Filtrera strängar som innehåller en viss bokstav")
    print("2: Filtrera strängar som är kortare än ett visst antal tecken")

    val = input("Gör ditt val (1 eller 2): ")

    if val == "1":
        bokstav = input("Vilken bokstav vill du filtrera efter? ")
        resultat = filter_letter(lista, bokstav)
        print("Filtrerad lista:", resultat)
    
    elif val == "2":
        max_längd = int(input("Vad är maxlängden på strängarna? "))
        resultat = filter_length(lista, max_längd)
        print("Filtrerad lista:", resultat)
    
    else:
        print("Ogiltigt val")


huvudprogram()
