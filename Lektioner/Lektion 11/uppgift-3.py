class Anstalld:
    def __init__(self, namn, timlon):
        self.namn = namn
        self.timlon = timlon

    def berakna_lon(self, timmar):
        return self.timlon * timmar

class Heltid(Anstalld):
    def __init__(self, namn, manadslon):
        super().__init__(namn, timlon=0)
        self.manadslon = manadslon

    def berakna_lon(self):
        return self.manadslon

class Deltid(Anstalld):
    pass

# Testa klasserna
heltid_anstalld = Heltid("Sara", 30000)
deltid_anstalld = Deltid("Erik", 150)

print(f"Heltidsanställd lön: {heltid_anstalld.berakna_lon()}")
print(f"Deltidsanställd lön: {deltid_anstalld.berakna_lon(80)}")
