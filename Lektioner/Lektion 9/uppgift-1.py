try:   
    tal = float(input("Ange ett tal: "))    
    resultat = 100 / tal    
    print("Resultat:", resultat)
except ZeroDivisionError:    print("Du kan inte dividera med noll!")
except ValueError:    print("Ogiltig inmatning, du måste ange ett tal!")