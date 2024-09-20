# lägg_till_uppgift_modul.py
def lägg_till_uppgift(uppgifter):
    uppgift = input("Ange en ny uppgift: ")
    uppgifter.append({"uppgift": uppgift, "klar": False})
    print(f"Uppgiften '{uppgift}' har lagts till.")
