# Uppgift 1: Skapa en Person-klass
class Person:
    def __init__(self, namn, ålder, stad):
        self.namn = namn
        self.ålder = ålder
        self.stad = stad
    
    def hälsa(self):
        print(f"Hej! Jag heter {self.namn} och bor i {self.stad}.")

# Interaktivt användarinput
namn = input("Ange ditt namn: ")
ålder = int(input("Ange din ålder: "))
stad = input("Ange din stad: ")

# Skapa ett person-objekt baserat på användarens input
person1 = Person(namn, ålder, stad)
person1.hälsa()
