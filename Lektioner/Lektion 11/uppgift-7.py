class Fordon:
    def __init__(self, hastighet):
        self.hastighet = hastighet

    def framfor(self):
        pass

class Bil(Fordon):
    def framfor(self):
        print(f"Bilen kör på vägen i {self.hastighet} km/h.")

class Cykel(Fordon):
    def framfor(self):
        print(f"Cykeln rullar på cykelbanan i {self.hastighet} km/h.")

class Tag(Fordon):
    def framfor(self):
        print(f"Tåget kör på rälsen i {self.hastighet} km/h.")

# Testa klasserna
fordon_lista = [Bil(100), Cykel(20), Tag(150)]

for fordon in fordon_lista:
    fordon.framfor()
