# Lista med minst fem heltal
numbers = [2, 3, 5, 7, 11]

# Initialisera produkten som 1 (multiplikativt neutralt element)
product = 1

# Iterera över listan och multiplicera varje tal med produkten
for number in numbers:
    product *= number

# Skriv ut produkten av alla tal i listan
print("Produkten av talen i listan är:", product)
