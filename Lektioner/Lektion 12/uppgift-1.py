class Vapen:
    def __init__(self, namn, skada):
        self.__namn = namn
        self.__skada = skada

    # Hämta vapnets namn
    def get_namn(self):
        return self.__namn

    # Hämta vapnets skada
    def get_skada(self):
        return self.__skada


class Krigare:
    def __init__(self, namn, hälsa=100):
        self.__namn = namn
        self.__hälsa = hälsa
        self.__vapen = None

    # Lägg till vapen till krigaren
    def lägg_till_vapen(self, vapen):
        self.__vapen = vapen
        print(f"{self.__namn} har fått vapnet {self.__vapen.get_namn()}.")

    # Använd vapen
    def använd_vapen(self):
        if self.__vapen:
            print(f"{self.__namn} använder {self.__vapen.get_namn()}.")
        else:
            print(f"{self.__namn} har inget vapen att använda.")

krigare = Krigare("Ulf")
vapen = Vapen("Svärd", 20)
krigare.lägg_till_vapen(vapen)
krigare.använd_vapen()  # Output: Thor använder Svärd
