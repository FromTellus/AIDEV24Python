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

fiende = Fiende("Jätte")
vapen = Vapen("Yxa", 25)
fiende.lägg_till_vapen(vapen)
fiende.ta_skada(40)  # Output: Jätte har tagit 40 skada. Hälsa nu: 60
