class Djur:
    def __init__(self, namn, ålder):
        self.ålder = ålder
        self.namn = namn

    def ljud(self):
        pass
    
    def info (self):
        return f"{self.namn} är {self.ålder} år gammal"

class Lejon(Djur):
    def __init__(self, namn, ålder, manens_storlek):
        super().__init__(namn, ålder)
        self.manens_storlek = manens_storlek
    
    def ljud(self):
        return "ROOOAAAR"
    
class Elefant(Djur):
    def __init__(self, namn, ålder, betarnas_längd):
        super().__init__(namn, ålder)
        self.betarnas_längd = betarnas_längd
    
    def ljud(self):
        return "TÖÖÖÖÖÖÖT"
    
class Apa(Djur):
    def __init__(self, namn, ålder, art):
        super().__init__(namn, ålder)
        self.art = art
    
    def ljud(self):
        return "OOH OOH AHH AHH"
    
elefant = Elefant("Dumbo", 22, 1.5)
lejon = Lejon("Simba", 10, 0.3)
apa = Apa("Abu", 5, "Gibbon")

print(elefant.info())
print(lejon.info())
print(apa.info())
print(elefant.ljud())
print(lejon.ljud())
print(apa.ljud())
