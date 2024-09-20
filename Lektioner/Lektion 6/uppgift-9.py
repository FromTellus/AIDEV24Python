# Skapa en dictionary från användarinmatning
personer = {}
for _ in range(5):
    namn = input("Ange ett namn: ")
    ålder = input("Ange ålder: ")
    personer[namn] = ålder

# Skriv dictionaryn till en fil
with open('personer.txt', 'w') as fil:
    for namn, ålder in personer.items():
        fil.write(f"{namn}: {ålder}\n")

# Läs dictionaryn från filen
personer_från_fil = {}
with open('personer.txt', 'r') as fil:
    for rad in fil:
        namn, ålder = rad.strip().split(': ')
        personer_från_fil[namn] = ålder

print("Personer från fil:")
print(personer_från_fil)
