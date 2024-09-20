# Be användaren mata in ett tal
tal = int(input("Ange ett tal: "))

# Kontrollera om talet är jämnt eller udda
if tal % 2 == 0:
    print(f"{tal} är ett jämnt tal.")
else:
    print(f"{tal} är ett udda tal.")
