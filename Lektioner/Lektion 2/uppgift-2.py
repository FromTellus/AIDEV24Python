# Begär input från användaren
tal1 = float(input("Mata in det första talet: "))
tal2 = float(input("Mata in det andra talet: "))

# Utför jämförelserna
är_större = tal1 > tal2
är_mindre = tal1 < tal2
är_lika = tal1 == tal2
är_olika = tal1 != tal2


# Skriv ut resultaten av jämförelserna
print(f"Är tal1 större än tal2? {är_större}")
print(f"Är tal1 mindre än tal2? {är_mindre}")
print(f"Är tal1 lika med tal2? {är_lika}")
print(f"Är tal1 olika tal2? {är_olika}")

# Bestäm vilket tal som är störst eller om de är lika
if tal1 > tal2:
    print("Det första talet är större än det andra.")
elif tal1 < tal2:
    print("Det andra talet är större än det första.")
else:
    print("De två talen är lika stora.")
