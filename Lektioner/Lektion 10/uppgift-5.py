# Uppgift 5: Bokbibliotek
class Bibliotek:
    def __init__(self):
        self.böcker = []
    
    def lägg_till_bok(self, titel, författare):
        self.böcker.append({"titel": titel, "författare": författare})
    
    def visa_böcker(self):
        if not self.böcker:
            print("Inga böcker har lagts till i biblioteket ännu.")
        else:
            print("\nBöcker i biblioteket:")
            for bok in self.böcker:
                print(f"{bok['titel']} av {bok['författare']}")

# Interaktiv meny
bibliotek = Bibliotek()

while True:
    print("\nVad vill du göra?")
    print("1. Lägg till en bok")
    print("2. Visa böcker")
    print("3. Avsluta")
    
    val = input("Välj ett alternativ (1-3): ")
    
    if val == "1":
        titel = input("Ange bokens titel: ")
        författare = input("Ange författaren: ")
        bibliotek.lägg_till_bok(titel, författare)
        print(f"Boken '{titel}' av {författare} har lagts till i biblioteket.")
    elif val == "2":
        bibliotek.visa_böcker()
    elif val == "3":
        print("Avslutar programmet.")
        break
    else:
        print("Ogiltigt val. Försök igen.")
