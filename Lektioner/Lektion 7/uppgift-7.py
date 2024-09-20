import json

# Be användaren mata in sitt namn och ålder
name = input("Ange ditt namn: ")
age = int(input("Ange din ålder: "))

# Skapa en dictionary med användarens information
user_data = {"name": name, "age": age}

# Skriv data till en JSON-fil
with open('user_data.json', 'w') as file:
    json.dump(user_data, file)
    print("Användardata har sparats.")

# Läs tillbaka informationen från filen
with open('user_data.json', 'r') as file:
    loaded_data = json.load(file)
    print(f"Återläst data: {loaded_data}")
