# låna_bok_modul.py
def låna_bok(bibliotek):
    if len(bibliotek) == 0:
        print("Inga böcker finns i biblioteket.")
        return

    visa_tillgängliga_böcker(bibliotek)
    titel = input("Ange titeln på boken du vill låna: ")
    
    for bok in bibliotek:
        if bok["titel"].lower() == titel.lower() and not bok["utlånad"]:
            bok["utlånad"] = True
            print(f"Boken '{bok['titel']}' har lånats ut.")
            return
    print(f"Boken '{titel}' finns inte tillgänglig för utlåning.")

def visa_tillgängliga_böcker(bibliotek):
    print("\nTillgängliga böcker:")
    tillgängliga = [bok for bok in bibliotek if not bok["utlånad"]]
    if tillgängliga:
        for bok in tillgängliga:
            print(f"- {bok['titel']} av {bok['författare']}")
    else:
        print("Inga böcker tillgängliga för utlåning.")
