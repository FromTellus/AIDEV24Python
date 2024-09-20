# visa_modul.py
def visa_alla_användare(användare):
    if len(användare) == 0:
        print("Det finns inga användare i listan.")
    else:
        print("Lista över alla användare:")
        for person in användare:
            print(f"Namn: {person['namn']}, Ålder: {person['ålder']}")
