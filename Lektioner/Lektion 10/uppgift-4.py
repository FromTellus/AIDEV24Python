# Uppgift 4: Studentens studier
class Student:
    def __init__(self, namn):
        self.namn = namn
        self.ämnen = []
    
    def lägg_till_ämne(self, ämne):
        self.ämnen.append(ämne)
    
    def visa_ämnen(self):
        ämneslista = ', '.join(self.ämnen)
        print(f"{self.namn} läser: {ämneslista}")

# Exempel på användning:
student = Student("Bob")
student.lägg_till_ämne("Matematik")
student.lägg_till_ämne("Fysik")
student.visa_ämnen()  # Output: Bob läser: Matematik, Fysik
