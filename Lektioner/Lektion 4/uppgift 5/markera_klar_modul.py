from visa_uppgifter_modul import visa_uppgifter


def markera_uppgift_som_klar(lista_av_uppgifter):
    # Kontrollera om det finns några uppgifter i listan
    if len(lista_av_uppgifter) == 0:
        print("Det finns inga uppgifter att markera som klara.")
        return  # Avsluta funktionen om listan är tom
    
    # Visa uppgifterna så att användaren kan välja en uppgift att markera som klar
    visa_uppgifter(lista_av_uppgifter)
    
    # Be användaren att ange indexet för den uppgift som ska markeras som klar
    try:
        index = int(input("Ange numret på uppgiften du vill markera som klar: "))
    except ValueError:
        print("Du måste ange ett giltigt nummer.")
        return  # Avsluta funktionen om användaren anger något annat än ett heltal
    
    # Kontrollera om indexet är inom giltigt intervall
    if 0 <= index < len(lista_av_uppgifter):
        # Markera den valda uppgiften som klar
        lista_av_uppgifter[index]["klar"] = True
        print(f"Uppgiften '{lista_av_uppgifter[index]['uppgift']}' är nu markerad som klar.")
    else:
        print("Ogiltigt val. Vänligen ange ett nummer från listan.")

