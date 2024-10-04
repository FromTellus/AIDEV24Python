class Krigare:
    def __init__(self, namn, hälsa=100):
        self.__namn = namn
        self.__hälsa = hälsa
        self.__vapen = None

    # Lägg till vapen till krigaren
    def lägg_till_vapen(self, vapen):
        self.__vapen = vapen

    # Använd vapen
    def använd_vapen(self):
        if self.__vapen:
            print(f"{self.__namn} använder {self.__vapen.get_namn()}.")
        else:
            print(f"{self.__namn} har inget vapen.")

    # Ta skada
    def ta_skada(self, skada):
        self.__hälsa -= skada
        print(f"{self.__namn} har tagit {skada} skada. Hälsa nu: {self.__hälsa}")

    # Kontrollera om krigaren är vid liv
    def är_vid_liv(self):
        return self.__hälsa > 0
    
    def get_namn(self):
        return self.__namn
