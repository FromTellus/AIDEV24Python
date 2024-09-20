import random

# Generera ett slumpmässigt tal mellan 1 och 100
random_number = random.randint(1, 100)

# Starta gissningsloopen
while True:
    guess = int(input("Gissa ett tal mellan 1 och 100: "))
    
    if guess < random_number:
        print("För lågt, försök igen!")
    elif guess > random_number:
        print("För högt, försök igen!")
    else:
        print("Grattis, du gissade rätt!")
        break
