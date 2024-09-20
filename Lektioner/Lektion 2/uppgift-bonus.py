# Begär input för den första lådan
längd1 = float(input("Mata in längden på den första lådan (meter): "))
bredd1 = float(input("Mata in bredden på den första lådan (meter): "))
höjd1 = float(input("Mata in höjden på den första lådan (meter): "))

# Beräkna volymen för den första lådan
volym1 = längd1 * bredd1 * höjd1

# Begär input för den andra lådan
längd2 = float(input("Mata in längden på den andra lådan (meter): "))
bredd2 = float(input("Mata in bredden på den andra lådan (meter): "))
höjd2 = float(input("Mata in höjden på den andra lådan (meter): "))

# Beräkna volymen för den andra lådan
volym2 = längd2 * bredd2 * höjd2

# Jämför volymerna och skriv ut resultatet
if volym1 > volym2:
    print("Den första lådan har störst volym.")
elif volym1 < volym2:
    print("Den andra lådan har störst volym.")
else:
    print("Båda lådorna har lika stor volym.")
