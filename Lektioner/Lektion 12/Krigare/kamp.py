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
