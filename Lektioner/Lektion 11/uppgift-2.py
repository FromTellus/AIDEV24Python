class Musikspelare:
    def __init__(self, märke):
        self.märke = märke

    def spela_musik(self):
        pass

class CDSpelare(Musikspelare):
    def __init__(self, märke, antal_skivor):
        super().__init__(märke)
        self.antal_skivor = antal_skivor

    def spela_musik(self):
        print(f"Spelar musik från {self.antal_skivor} CD-skivor på {self.märke}.")

class MP3Spelare(Musikspelare):
    def __init__(self, märke, minne):
        super().__init__(märke)
        self.minne = minne

    def spela_musik(self):
        print(f"Spelar musik från digitala filer ({self.minne} GB) på {self.märke}.")

class Radio(Musikspelare):
    def __init__(self, märke, frekvens):
        super().__init__(märke)
        self.frekvens = frekvens

    def spela_musik(self):
        print(f"Spelar musik från radiokanal {self.frekvens} på {self.märke}.")

# Testa klasserna
cdspelare = CDSpelare("Sony", 5)
mp3spelare = MP3Spelare("Apple", 64)
radio = Radio("Philips", 102.5)

cdspelare.spela_musik()
mp3spelare.spela_musik()
radio.spela_musik()
