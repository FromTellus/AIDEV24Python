# sök_recept_modul.py
def sök_recept(receptlista):
    titel = input("Ange receptets titel som du söker efter: ")
    for recept in receptlista:
        if recept["titel"].lower() == titel.lower():
            print(f"\nRecept hittat: {recept['titel']}")
            print(f"Ingredienser: {', '.join(recept['ingredienser'])}")
            print(f"Instruktioner: {recept['instruktioner']}")
            return
    print(f"Inget recept med titeln '{titel}' hittades.")
