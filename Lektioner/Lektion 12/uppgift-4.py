class Vapen:
    def __init__(self, namn, skada):
        self.__namn = namn
        self.__skada = skada

    def get_namn(self):
        return self.__namn

    def get_skada(self):
        return self.__skada


class Krigare:
    def __init__(self, namn, hälsa=100):
        self.__namn = namn
        self.__hälsa = hälsa
        self.__vapen = None

    def lägg_till_vapen(self, vapen):
        self.__vapen = vapen

    def använd_vapen(self):
        if self.__vapen:
            print(f"{self.__namn} använder {self.__vapen.get_namn()}.")
            return self.__vapen.get_skada()
        else:
            print(f"{self.__namn} har inget vapen.")
            return 0

    def ta_skada(self, skada):
        self.__hälsa -= skada
        print(f"{self.__namn} har tagit {skada} skada. Hälsa nu: {self.__hälsa}")

    def är_vid_liv(self):
        return self.__hälsa > 0
    
    def get_namn(self):
        return self.__namn


class Fiende:
    def __init__(self, namn, hälsa=100):
        self.__namn = namn
        self.__hälsa = hälsa
        self.__vapen = None

    def lägg_till_vapen(self, vapen):
        self.__vapen = vapen

    def använd_vapen(self):
        if self.__vapen:
            print(f"{self.__namn} använder {self.__vapen.get_namn()}.")
            return self.__vapen.get_skada()
        else:
            print(f"{self.__namn} har inget vapen.")
            return 0

    def ta_skada(self, skada):
        self.__hälsa -= skada
        print(f"{self.__namn} har tagit {skada} skada. Hälsa nu: {self.__hälsa}")

    def är_vid_liv(self):
        return self.__hälsa > 0
    
        
    def get_namn(self):
        return self.__namn


class Kamp:
    def __init__(self, krigare, fiende):
        self.krigare = krigare
        self.fiende = fiende

    # Genomför kampen
    def starta(self):
        print(f"Kampen börjar mellan {self.krigare.get_namn()} och {self.fiende.get_namn()}")
        while self.krigare.är_vid_liv() and self.fiende.är_vid_liv():
            skada1 = self.krigare.använd_vapen()
            self.fiende.ta_skada(skada1)
            if self.fiende.är_vid_liv():
                skada2 = self.fiende.använd_vapen()
                self.krigare.ta_skada(skada2)

    # Visa slutresultatet
    def slutresultat(self):
        if self.krigare.är_vid_liv():
            print(f"{self.krigare.get_namn()} vann kampen!")
        else:
            print(f"{self.fiende.get_namn()} vann kampen!")

krigare = Krigare("Ulf")
fiende = Fiende("Jobb")
vapen1 = Vapen("Arbetskraft", 0)
vapen2 = Vapen("Slaveri", 25)
krigare.lägg_till_vapen(vapen1)
fiende.lägg_till_vapen(vapen2)

kamp = Kamp(krigare, fiende)
kamp.starta()
kamp.slutresultat()  # Output: Ulf vann kampen!
