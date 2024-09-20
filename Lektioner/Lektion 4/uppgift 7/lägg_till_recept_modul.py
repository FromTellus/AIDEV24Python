# lägg_till_recept_modul.py
def lägg_till_recept(receptlista):
    titel = input("Ange receptets titel: ")
    ingredienser = input("Ange ingredienser (separerade med kommatecken): ")
    instruktioner = input("Ange instruktionerna för receptet: ")
    recept = {
        "titel": titel,
        "ingredienser": ingredienser.split(","),
        "instruktioner": instruktioner
    }
    receptlista.append(recept)
    print(f"Receptet '{titel}' har lagts till.")
