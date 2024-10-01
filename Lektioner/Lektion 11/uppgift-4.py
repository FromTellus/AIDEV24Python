class Kund:
    def __init__(self, namn):
        self.namn = namn
        self.prioritet = 3  # Standardprioritet för vanliga kunder

    def get_prioritet(self):
        return self.prioritet

class Medlem(Kund):
    def __init__(self, namn):
        super().__init__(namn)
        self.prioritet = 2  # Högre prioritet för medlemmar

class VIPKund(Kund):
    def __init__(self, namn):
        super().__init__(namn)
        self.prioritet = 1  # Högsta prioritet för VIP-kunder

# Testa och sortera kunder baserat på prioritet
kunder = [Kund("Anna"), Medlem("Bertil"), VIPKund("Cecilia"), Kund("David")]
sorterade_kunder = sorted(kunder, key=Kund.get_prioritet)

for kund in sorterade_kunder:
    print(kund.namn)
