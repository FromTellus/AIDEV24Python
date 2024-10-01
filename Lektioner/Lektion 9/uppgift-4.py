try:
    tal = int(input("Ange ett heltal: "))
except ValueError:
    print("Ogiltig inmatning, du måste ange ett heltal.")
else:
    print("Dubbelt av talet är:", tal * 2)