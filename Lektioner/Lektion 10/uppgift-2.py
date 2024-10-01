# Uppgift 2: Bankkonto
class Bankkonto:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def insättning(self, belopp):
        self.saldo += belopp
    
    def uttag(self, belopp):
        if belopp <= self.saldo:
            self.saldo -= belopp
        else:
            print("Otillräckligt saldo.")
    
    def visa_saldo(self):
        print(f"Ditt saldo är: {self.saldo} kr")

# Interaktiv användning
konto = Bankkonto(float(input("Ange ditt startsaldo: ")))

while True:
    print("\nVad vill du göra?")
    print("1. Sätt in pengar")
    print("2. Ta ut pengar")
    print("3. Visa saldo")
    print("4. Avsluta")
    
    val = input("Välj ett alternativ (1-4): ")
    
    if val == "1":
        belopp = float(input("Hur mycket vill du sätta in? "))
        konto.insättning(belopp)
        print(f"{belopp} kr har satts in.")
    elif val == "2":
        belopp = float(input("Hur mycket vill du ta ut? "))
        if (konto.saldo - belopp) < 0:
            print("Otillräckligt saldo.")
        else:
            konto.uttag(belopp)
    elif val == "3":
        konto.visa_saldo()
    elif val == "4":
        print("Tack för att du använder vår tjänst!")
        break
    else:
        print("Ogiltigt val. Försök igen.")
