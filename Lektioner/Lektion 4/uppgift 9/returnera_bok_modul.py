# returnera_bok_modul.py
def returnera_bok(bibliotek):
    if len(bibliotek) == 0:
        print("Inga böcker finns i biblioteket.")
        return

    visa_utlånade_böcker(bibliotek)
    titel = input("Ange titeln på boken du vill returnera: ")

    for bok in bibliotek:
        if bok["titel"].lower() == titel.lower() and bok["utlånad"]:
            bok["utlånad"] = False
            print(f"Boken '{bok['titel']}' har returnerats.")
            return
    print(f"Boken '{titel}' hittades inte som utlånad.")

def visa_utlånade_böcker(bibliotek):
    print("\nUtlånade böcker:")
    utlånade = [bok for bok in bibliotek if bok["utlånad"]]
    if utlånade:
        for bok in utlånade:
            print(f"- {bok['titel']} av {bok['författare']}")
    else:
        print("Inga böcker är utlånade.")
