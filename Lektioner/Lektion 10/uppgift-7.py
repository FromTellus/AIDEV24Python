# Uppgift 7: Köhantering
class Kö:
    def __init__(self):
        self.kölista = []
    
    def lägg_till_person(self, namn):
        self.kölista.append(namn)
        print(f"{namn} har lagts till i kön.")
    
    def betjäna_person(self):
        if self.kölista:
            betjänad_person = self.kölista.pop(0)
            print(f"{betjänad_person} betjänas.")
        else:
            print("Ingen finns i kön.")

    def visa_kö(self):
        if self.kölista:
            print(f"Personer i kön: {', '.join(self.kölista)}")
        else:
            print("Kön är tom.")

# Interaktiv meny
kö = Kö()

while True:
    print("\nVad vill du göra?")
    print("1. Lägg till en person i kön")
    print("2. Betjäna första personen i kön")
    print("3. Visa personer i kön")
    print("4. Avsluta")
    
    val = input("Välj ett alternativ (1-4): ")
    
    if val == "1":
        namn = input("Ange personens namn: ")
        kö.lägg_till_person(namn)
    elif val == "2":
        kö.betjäna_person()
    elif val == "3":
        kö.visa_kö()
    elif val == "4":
        print("Avslutar programmet.")
        break
    else:
        print("Ogiltigt val. Försök igen.")
