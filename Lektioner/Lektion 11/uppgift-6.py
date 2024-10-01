class Bok:
    def __init__(self, titel, forfattare):
        self.titel = titel
        self.forfattare = forfattare

class Lanebok(Bok):
    def __init__(self, titel, forfattare):
        super().__init__(titel, forfattare)
        self.lantagare = None

    def lana_ut(self, lantagare):
        if self.lantagare is None:
            self.lantagare = lantagare
            print(f"Boken '{self.titel}' är nu utlånad till {lantagare}.")
        else:
            print(f"Boken '{self.titel}' är redan utlånad.")

    def aterlamna(self):
        if self.lantagare is not None:
            print(f"Boken '{self.titel}' har återlämnats.")
            self.lantagare = None
        else:
            print(f"Boken '{self.titel}' är inte utlånad.")

# Testa klassen
bok = Lanebok("1984", "George Orwell")
bok.lana_ut("Emma")
bok.aterlamna()
