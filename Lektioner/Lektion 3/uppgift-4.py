# Definiera en fördefinierad lista med heltal
tal_lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

while True:
    # Be användaren mata in ett tal
    tal_input = int(input("Ange ett tal för att kontrollera om det finns i listan (eller ange -1 för att avsluta): "))

    # Kontrollera om användaren vill avsluta
    if tal_input == -1:
        print("Programmet avslutas.")
        break

    # Kontrollera om talet finns i listan
    if tal_input in tal_lista:
        print(f"Talet {tal_input} finns i listan.")
        print("Programmet avslutas.")
        break
    else:
        print(f"Talet {tal_input} finns inte i listan.")
