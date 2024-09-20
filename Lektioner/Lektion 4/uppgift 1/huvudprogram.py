# huvudprogram.py
from uppercase_modul import text_till_versaler
from remove_spaces_modul import ta_bort_mellanslag

def huvudprogram():
    text = input("Skriv in text: ")
    print("Vad vill du göra?")
    print("1: Konvertera till versaler")
    print("2: Ta bort alla mellanslag")

    val = input("Gör ditt val (1 eller 2): ")

    if val == "1":
        print(text_till_versaler(text))
    elif val == "2":
        print(ta_bort_mellanslag(text))
    else:
        print("Ogiltigt val")
        
    


huvudprogram()
