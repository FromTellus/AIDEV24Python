# lägg_till_modul.py
def lägg_till_användare(användare):
    namn = input("Ange användarens namn: ")
    ålder = input("Ange användarens ålder: ")
    användare.append({"namn": namn, "ålder": ålder})
    print(f"Användaren {namn} har lagts till.")
