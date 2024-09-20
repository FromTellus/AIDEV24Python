print("Du vaknar upp i en mörk skog. Det finns tre vägar framför dig.")
print("1. Gå åt höger.")
print("2. Gå åt vänster.")
print("3. Gå rakt fram.")

# Begär användarens val
val = input("Vad väljer du att göra? (1/2/3): ")

# Hantera användarens val med if-elif-else-satser
if val == "1":
    print("Du valde att gå åt höger. Du stöter på en stor björn!")
    print("Björnens vrål fyller luften, och du bestämmer dig för att långsamt backa undan.")
elif val == "2":
    print("Du valde att gå åt vänster. Du hittar en gammal skattkista!")
    print("Kistan är låst, men du känner att något värdefullt finns inuti.")
elif val == "3":
    print("Du valde att gå rakt fram. Efter en stund hittar du en väg ut ur skogen.")
    print("Grattis, du är säker nu!")
else:
    print("Det var inget giltigt val. Du står kvar på platsen och hör mystiska ljud omkring dig.")
