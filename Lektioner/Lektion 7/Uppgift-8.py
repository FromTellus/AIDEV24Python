from collections import Counter

# Skapa en sträng med text
text = "Detta är en text med flera ord. Vissa ord förekommer flera gånger, som ordet 'ord'."

# Dela upp texten i en lista av ord
words = text.split()

# Använd Counter för att räkna förekomsten av varje ord
word_count = Counter(words)

# Skriv ut hur många gånger varje ord förekommer
print("Förekomst av ord:")
for word, count in word_count.items():
    print(f"{word}: {count}")
