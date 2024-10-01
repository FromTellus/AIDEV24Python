# Uppgift 3: Biluthyrning
class Bil:
    def __init__(self, modell):
        self.modell = modell
        self.tillgänglig = True
    
    def hyr(self):
        if self.tillgänglig:
            self.tillgänglig = False
            print(f"{self.modell} har hyrts ut.")
        else:
            print(f"{self.modell} är redan uthyrd.")
    
    def lämna_tillbaka(self):
        if not self.tillgänglig:
            self.tillgänglig = True
            print(f"{self.modell} har lämnats tillbaka och är nu tillgänglig igen.")
        else:
            print(f"{self.modell} är redan tillgänglig.")

# Skapa några bilar för uthyrning
bilar = [Bil("Volvo XC60"), Bil("Toyota Corolla"), Bil("BMW X5")]

# Interaktiv meny
while True:
    print("\nTillgängliga bilar:")
    for i, bil in enumerate(bilar):
        status = "Tillgänglig" if bil.tillgänglig else "Uthyrd"
        print(f"{i+1}. {bil.modell} - {status}")
    
    print("\nVad vill du göra?")
    print("1. Hyr en bil")
    print("2. Lämna tillbaka en bil")
    print("3. Avsluta")
    
    val = input("Välj ett alternativ (1-3): ")
    
    if val == "1":
        bilnummer = int(input("Vilken bil vill du hyra? Ange numret: ")) - 1
        if 0 <= bilnummer < len(bilar):
            bilar[bilnummer].hyr()
        else:
            print("Ogiltigt val. Försök igen.")
    elif val == "2":
        bilnummer = int(input("Vilken bil vill du lämna tillbaka? Ange numret: ")) - 1
        if 0 <= bilnummer < len(bilar):
            bilar[bilnummer].lämna_tillbaka()
        else:
            print("Ogiltigt val. Försök igen.")
    elif val == "3":
        print("Tack för att du använder vår biluthyrningstjänst!")
        break
    else:
        print("Ogiltigt val. Försök igen.")
