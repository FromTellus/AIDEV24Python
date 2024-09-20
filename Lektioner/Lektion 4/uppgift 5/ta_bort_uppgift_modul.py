# ta_bort_uppgift_modul.py

from visa_uppgifter_modul import visa_uppgifter

def ta_bort_uppgift(uppgifter):
    if len(uppgifter) == 0:
        print("Det finns inga uppgifter att ta bort.")
        return
    visa_uppgifter(uppgifter)
    index = int(input("Ange numret på uppgiften du vill ta bort: "))
    if 0 <= index < len(uppgifter):
        borttagen_uppgift = uppgifter.pop(index)
        print(f"Uppgiften '{borttagen_uppgift['uppgift']}' har tagits bort.")
    else:
        print("Ogiltigt val.")
    
