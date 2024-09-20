# lista_recept_modul.py
def lista_recept(receptlista):
    if len(receptlista) == 0:
        print("Inga recept är tillgängliga.")
    else:
        print("\nLista över alla sparade recept:")
        for recept in receptlista:
            print(f"- {recept['titel']}")
