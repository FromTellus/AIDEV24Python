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

