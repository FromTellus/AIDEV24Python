# huvudprogram.py
from valuta_modul import sek_till_usd, sek_till_eur, sek_till_gbp

def huvudprogram():
    sek_belopp = float(input("Ange belopp i SEK: "))
    print("Välj vilken valuta du vill omvandla till:")
    print("1: USD")
    print("2: EUR")
    print("3: GBP")

    val = input("Gör ditt val (1, 2 eller 3): ")

    if val == "1":
        resultat = sek_till_usd(sek_belopp)
        print(f"{sek_belopp} SEK motsvarar {resultat} USD")
    
    elif val == "2":
        resultat = sek_till_eur(sek_belopp)
        print(f"{sek_belopp} SEK motsvarar {resultat} EUR")
    
    elif val == "3":
        resultat = sek_till_gbp(sek_belopp)
        print(f"{sek_belopp} SEK motsvarar {resultat} GBP")
    
    else:
        print("Ogiltigt val")

if __name__ == "__main__":
    huvudprogram()
