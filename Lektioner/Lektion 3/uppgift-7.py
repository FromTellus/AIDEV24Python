import random

# Generera ett slumpmässigt tal mellan 1 och 50
slumptal = random.randint(1, 50)

# Initialisera variabel för att lagra användarens gissning
gissning = None

# While-loop som körs tills användaren gissar rätt
while gissning != slumptal:
    # Be användaren mata in en gissning
    gissning = int(input("Gissa ett tal mellan 1 och 50: "))
    
    # Kontrollera om gissningen är för låg, för hög eller korrekt
    if gissning < slumptal:
        print("För lågt! Försök igen.")
    elif gissning > slumptal:
        print("För högt! Försök igen.")
    else:
        print(f"Grattis! Du gissade rätt. Talet var {slumptal}.")
