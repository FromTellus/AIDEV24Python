# visa_uppgifter_modul.py

def visa_uppgifter(uppgifter):
    print("\nAktuella uppgifter:")
    for i, uppgift in enumerate(uppgifter):
        status = "Klar" if uppgift["klar"] else "Inte klar"
        print(f"{i}: {uppgift['uppgift']} - {status}")
