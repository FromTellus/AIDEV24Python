class UnderÅlderError(Exception):
    pass

def kontrollera_ålder(ålder):
    if ålder < 18:
        raise UnderÅlderError("Du måste vara över 18 år.")
    else:
        print("Du är tillräckligt gammal.")

try:
    ålder = int(input("Ange din ålder: "))
    kontrollera_ålder(ålder)
except UnderÅlderError as e:
    print(e)
