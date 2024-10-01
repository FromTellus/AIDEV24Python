# Uppgift 6: Filmkatalog
class Film:
    def __init__(self, titel, år, regissör):
        self.titel = titel
        self.år = år
        self.regissör = regissör

class Filmkatalog:
    def __init__(self):
        self.filmer = []
    
    def lägg_till_film(self, titel, år, regissör):
        ny_film = Film(titel, år, regissör)
        self.filmer.append(ny_film)
    
    def sök_film(self, titel):
        for film in self.filmer:
            if film.titel == titel:
                print (film.titel, film.år, film.regissör)
                # print(f"{film.titel} ({film.år}), regisserad av {film.regissör}")
                return
        print("Filmen hittades inte.")

# Exempel på användning:
katalog = Filmkatalog()
katalog.lägg_till_film("Inception", 2010, "Christopher Nolan")
katalog.sök_film("Inception")
