# 1. Be användaren mata in strängar, separerade med kommatecken
strang_input = input("Ange minst fem strängar, separerade med kommatecken: ")

# 2. Dela upp strängarna i en lista genom att använda `split()`-metoden
strang_lista_med_mellanrum = strang_input.split(",")

# 3. Skapa en ny lista där vi kommer att lagra strängarna utan mellanrum
strang_lista = []

# 4. Iterera över varje sträng i `strang_lista_med_mellanrum`
for strang in strang_lista_med_mellanrum:
    # 5. Ta bort eventuella extra mellanrum runt strängen med `strip()`-metoden
    strang_utan_mellanrum = strang.strip()
    
    # 6. Lägg till den "rena" strängen i `strang_lista`
    strang_lista.append(strang_utan_mellanrum)

# 7. Skapa en ny lista för att lagra strängar som konverterats till versaler
versaler_lista = []

# 8. Iterera över `strang_lista` och konvertera till versaler om strängen inte redan är i versaler
for strang in strang_lista:
    if strang.isupper():
        # Om strängen redan är i versaler, hoppa över den
        continue
    else:
        # Om strängen inte är i versaler, konvertera och lägg till i `versaler_lista`
        versaler_lista.append(strang.upper())

# 9. Skriv ut den nya listan med strängar i versaler
print(f"Den nya listan med strängar i versaler är: {versaler_lista}")
