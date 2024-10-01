class Djur:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder

    def ljud(self):
        pass

    def info(self):
        print(f"Namn: {self.namn}, Ålder: {self.ålder}")

class Lejon(Djur):
    def __init__(self, namn, ålder, manens_storlek):
        super().__init__(namn, ålder)
        self.manens_storlek = manens_storlek
        
    def info(self):
        print(f"Namn: {self.namn}, Ålder: {self.ålder}, Manens storlek: {self.manens_storlek}")
        

    def ljud(self):
        print("Lejonet ryter!")

class Elefant(Djur):
    def __init__(self, namn, ålder, betarnas_längd):
        super().__init__(namn, ålder)
        self.betarnas_längd = betarnas_längd

    def ljud(self):
        print("Elefanten trumpetar!")

class Apa(Djur):
    def __init__(self, namn, ålder, art):
        super().__init__(namn, ålder)
        self.art = art

    def ljud(self):
        print("Apan skriker!")

# Testa klasserna
lejon = Lejon("Simba", 5, "Stor")
elefant = Elefant("Dumbo", 10, 2.5)
apa = Apa("George", 3, "Schimpans")

print(lejon.manens_storlek, "här är manen")

lejon.info()
lejon.ljud()

elefant.info()
elefant.ljud()

apa.info()
apa.ljud()
