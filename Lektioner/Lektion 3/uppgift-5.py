# Lista med heltal
numbers = [23, 45, 67, 12, 98, 34, 56, 99, 5]

# Initialisera det största talet som första elementet i listan
largest_number = numbers[0]

# Iterera över listan och jämför varje tal med det största talet hittills
for number in numbers:
    if number > largest_number:
        largest_number = number

# Skriv ut det största talet
print("Det största talet i listan är:", largest_number)
