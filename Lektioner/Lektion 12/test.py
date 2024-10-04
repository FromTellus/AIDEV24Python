class Bankkonto:
    def __init__(self, innehavare, saldo):
        self.__innehavare = innehavare  # Privat attribut
        self.__saldo = saldo # Privat attribut

    def insättning(self, belopp):
        if belopp > 0:
            self.__saldo += belopp
            print(f"{belopp} kr har satts in på kontot.")
            print(f"Ditt saldo är: {self.__saldo} kr")
        else:
            print("Beloppet måste vara positivt.")

konto = Bankkonto("Anna", 1000)
konto.insättning(500)  # Output: 500 kr har satts in på kontot.
konto.__saldo += 599  # Fungerar inte för attributet är inte tillgängligt
print(konto.__saldo)  # Output: AttributeError: 'Bankkonto' object has no attribute '__saldo'
konto.insättning(500)  # Output: 500 kr har satts in på kontot.
