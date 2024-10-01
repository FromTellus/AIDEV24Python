class Produkt:
    def __init__(self, namn, pris):
        self.namn = namn
        self.pris = pris

class Mat(Produkt):
    def __init__(self, namn, pris, utgangsdatum):
        super().__init__(namn, pris)
        self.utgangsdatum = utgangsdatum

class Dryck(Produkt):
    def __init__(self, namn, pris, volym):
        super().__init__(namn, pris)
        self.volym = volym

# Testa klasserna
brod = Mat("Bröd", 25, "2023-12-31")
mjolk = Dryck("Mjölk", 15, "1 liter")

print(f"{brod.namn}: {brod.pris} kr, Utgångsdatum: {brod.utgangsdatum}")
print(f"{mjolk.namn}: {mjolk.pris} kr, Volym: {mjolk.volym}")
