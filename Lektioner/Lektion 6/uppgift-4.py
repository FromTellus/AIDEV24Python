### Lösning Uppgift 4: Läsa och summera tal från en fil

# Skapa en fil med heltal
with open('tal.txt', 'w') as fil:
    fil.write("10\n")
    fil.write("20\n")
    fil.write("30\n")

# Öppna filen och summera talen
summa = 0
with open('tal.txt', 'r') as fil:
    for rad in fil:
        summa += int(rad.strip())  # Konvertera varje rad till ett heltal och lägg till i summan

print(f"Summan av talen är: {summa}")
