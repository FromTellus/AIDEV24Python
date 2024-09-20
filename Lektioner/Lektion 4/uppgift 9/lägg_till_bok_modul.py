# lägg_till_bok_modul.py
def lägg_till_bok(bibliotek):
    titel = input("Ange bokens titel: ")
    författare = input("Ange bokens författare: ")
    bok = {
        "titel": titel,
        "författare": författare,
        "utlånad": False
    }
    bibliotek.append(bok)
    print(f"Boken '{titel}' av {författare} har lagts till i biblioteket.")
