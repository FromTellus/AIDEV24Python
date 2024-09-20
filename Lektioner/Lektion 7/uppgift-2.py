import sys

# Kolla om användaren angav ett filnamn som argument (felhantering)
if len(sys.argv) < 2:
    print("Ange ett filnamn som argument.")
    sys.exit()

# Hämta filnamnet från kommandoradsargumentet
filename = sys.argv[1]

# Försök att öppna filen och skriv ut dess innehåll
try:
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print(f"Filen {filename} hittades inte.")
