---
marp: true
paginate: true
theme: distansakademin
class: lead gaia
---


# Föreläsning: Operatorer och Kodstruktur i Python


---
## Inledning
I denna föreläsning kommer vi att fördjupa oss i användningen av operatorer i Python samt diskutera grundläggande kodstruktur. Dessa koncept är grundläggande för att kunna skriva effektiva och läsbara program.

---

## Operatorer i Python
### Aritmetiska Operatorer
Python har en mängd aritmetiska operatorer som används för att utföra matematiska operationer på tal.

- **Addition (+):** Lägger till två tal.
- **Subtraktion (-):** Subtraherar ett tal från ett annat.
- **Multiplikation (*):** Multiplicerar två tal.
- **Division (/):** Dividerar ett tal med ett annat, resultatet blir ett flyttal.
- **Heltalsdivision (//):** Dividerar och returnerar endast heltalsdelen av resultatet.
- **Modulus (%):** Returnerar resten efter division.
- **Exponentiation (**):** Upphöjer ett tal till en viss potens.

---
###### Exempel:
```
a = 3
b = 2

a + b  # Ger 5
a - b  # Ger 1
a * b  # Ger 6
a / b  # Ger 1.5
a // b # Ger 1
a % b  # Ger 1
a ** b # Ger 9


```
---

### Jämförelseoperatorer
Jämförelseoperatorer används för att jämföra värden. De returnerar alltid ett Boolean-värde, antingen `True` eller `False`.

- **Lika med (==):** Kontrollerar om två värden är lika.
- **Inte lika med (!=):** Kontrollerar om två värden inte är lika.
- **Större än (>):** Kontrollerar om det första värdet är större än det andra.
- **Mindre än (<):** Kontrollerar om det första värdet är mindre än det andra.
- **Större än eller lika med (>=):** Kontrollerar om det första värdet är större än eller lika med det andra.
- **Mindre än eller lika med (<=):** Kontrollerar om det första värdet är mindre än eller lika med det andra.
---

###### Exempel:
```
x = 10
y = 20
x == y  # Ger False
x != y  # Ger True
x > y   # Ger False
x < y   # Ger True
x >= y  # Ger False
x <= y  # Ger True
```
---
### Logiska Operatorer
Logiska operatorer används för att kombinera flera jämförelser eller uttryck.

- **and:** Returnerar `True` om båda villkoren är sanna.
- **or:** Returnerar `True` om minst ett av villkoren är sant.
- **not:** Returnerar `True` om villkoret är falskt.

###### Exempel:
```
x = 10
y = 20
z = 30
x > 5 and y < 25  # Ger True
x > 15 or z == 30  # Ger True
not(x > y)  # Ger True
```
---

## If- och Elif-satser

### Vad är If-satser?
En `if`-sats används i Python för att fatta beslut baserat på ett villkor. Om villkoret är sant (`True`), körs den efterföljande koden. Om villkoret är falskt (`False`), hoppar programmet över koden inuti `if`-satsen.

---

### Grundläggande If-sats
Den enklaste formen av en `if`-sats ser ut så här:

```
if villkor:  
    # kör denna kod om villkoret är sant
```

```
ålder = 18  
if ålder >= 18:  
    print("Du är myndig.")
```
I detta exempel kontrollerar programmet om värdet på variabeln `ålder` är 18 eller större. Om det är sant, skriver programmet ut "Du är myndig."

---

### Vad är Elif-satser?
En `elif`-sats står för "else if" och används för att kontrollera ytterligare villkor om det första `if`-villkoret är falskt. Du kan lägga till så många `elif`-satser som du behöver.

### If-Elif-Struktur
Strukturen för `if`- och `elif`-satser ser ut så här:

```
if villkor1:  
    # kör denna kod om villkor1 är sant  
elif villkor2:  
    # kör denna kod om villkor1 är falskt och villkor2 är sant  
elif villkor3:  
    # kör denna kod om villkor2 är falskt och villkor3 är sant  
```
---

### Vad är Else-satsen?
En `else`-sats används för att hantera alla situationer där inga av de tidigare `if`- eller `elif`-villkoren är sanna. Det är en "fångst-allt"-lösning som säkerställer att någon kod körs, även om inga specifika villkor uppfylls.

### If-Elif-Else-Struktur
```
if villkor1:  
    # kör denna kod om villkor1 är sant  
elif villkor2:  
    # kör denna kod om villkor1 är falskt och villkor2 är sant  
elif villkor3:  
    # kör denna kod om villkor2 är falskt och villkor3 är sant  
else:  
    # kör denna kod om ingen av ovanstående villkor är sanna
```
----

#### Exempel med If-Elif-Else:
```
poäng = 75  

if poäng >= 90:  
    betyg = "A"  
elif poäng >= 80:  
    betyg = "B"  
elif poäng >= 70:  
    betyg = "C"  
elif poäng >= 60:  
    betyg = "D"  
else:  
    betyg = "F"

print(f"Ditt betyg är {betyg}.")
```

---

### När ska man använda If-Elif-Else?
Använd `if`, `elif` och `else` när du har flera möjliga tillstånd eller scenarier att kontrollera. Dessa strukturer gör det möjligt för ditt program att fatta beslut baserat på olika villkor och köra olika kod beroende på vad som är sant.

### Viktiga punkter att komma ihåg:
- **Indragning:** Indragningar (4 mellanslag eller en tab) är viktiga i Python och används för att indikera vilken kod som hör till vilken `if`, `elif` eller `else`.
- **Else:** `else` är användbart för att hantera fall där ingen av de specifika villkoren är sanna. Det är dock valfritt och behövs bara om du vill att en viss kod ska köras när inga andra villkor uppfylls.

---


## Grundläggande Kodstruktur
### Kommentarer
Kommentarer används för att dokumentera koden och gör den lättare att förstå. I Python använder vi `#` för att skriva en kommentar.

###### Exempel:
````
a = 10  # Variabel a sätts till 10
````

---
### Variabler och Namngivning

Variabler används för att lagra data i ett program. Ett bra variabelnamn ska vara beskrivande och hjälpa till att göra koden lättare att förstå. För att uppnå detta finns det vissa konventioner och regler som bör följas.

---

#### Regler för Variabelnamn
- **Starta med en bokstav eller ett understreck (`_`):** Variabelnamn måste börja med en bokstav (a-z, A-Z) eller ett understreck (`_`). De kan följas av bokstäver, siffror (0-9), eller ytterligare understreck.
- **Reserverade ord:** Python har ett antal reserverade ord som inte kan användas som variabelnamn. Dessa är ord som `if`, `else`, `while`, `True`, `False`, `None`, och många fler. Dessa ord har speciell betydelse i språket och används för att definiera strukturer och logik i koden.
---
#### Understreck (`_`) i Variabelnamn
Att börja ett variabelnamn med ett understreck (`_`) har specifika syften:

---

- **Skyddade medlemsvariabler:** I objektorienterad programmering används ett inledande understreck (t.ex. `_my_var`) för att indikera att en variabel är "skyddad". Detta är en konvention som signalerar att variabeln inte bör användas utanför klassen eller modulen där den definierades. Det innebär att variabeln kan användas av klassen och dess subklasser, men att den inte är avsedd för extern åtkomst. Detta hjälper till att förhindra oavsiktliga ändringar av variabeln från kod utanför klassen.

---

- **Privata medlemsvariabler:** Två understreck i början av ett variabelnamn (t.ex. `__my_var`) används för att skapa namnförvrängning (name mangling), vilket innebär att variabeln blir "privat" och inte kan lätt nås eller ändras utanför klassen. Detta är användbart när du vill säkerställa att en variabel endast kan manipuleras inom den klass där den är definierad, och inte av subklasser eller extern kod. Namnförvrängning gör att variabelns namn ändras internt i Python, vilket ytterligare försvårar oavsiktlig åtkomst.


---
### Case-stilar för Namngivning

Det finns flera olika case-stilar som används för att namnge variabler och funktioner beroende på kontext och språkstandard.

---

1. **snake_case**
   - **Beskrivning:** Ord separeras med understreck, och alla bokstäver är små.
   - **Användning:** Detta är standarden i Python för variabler och funktionsnamn.
###### Exempel: `total_sum`, `average_score`, `max_value`

---

2. **camelCase**
   - **Beskrivning:** Det första ordet börjar med en liten bokstav, och varje efterföljande ord börjar med en stor bokstav, utan några understreck eller mellanslag.
   - **Användning:** Vanligt i många andra programmeringsspråk, som JavaScript.
###### Exempel: `totalSum`, `averageScore`, `maxValue`

---

3. **PascalCase**
   - **Beskrivning:** Liknar camelCase, men det första ordet börjar också med en stor bokstav.
   - **Användning:** Ofta används för klassnamn i många programmeringsspråk inklusive Python.
###### Exempel: `TotalSum`, `AverageScore`, `MaxValue`

---

4. **kebab-case**
   - **Beskrivning:** Ord separeras med bindestreck, och alla bokstäver är små.
   - **Användning:** Används ofta i URL:er och vissa konfigurationer, men är inte tillåtet som variabelnamn i Python.
###### Exempel: `total-sum`, `average-score`, `max-value`

---

5. **UPPER_CASE**
   - **Beskrivning:** Alla bokstäver är stora, och ord separeras med understreck.
   - **Användning:** Används vanligtvis för konstanter, alltså värden som inte ska ändras.
###### Exempel: `MAX_SIZE`, `DEFAULT_COLOR`, `PI`

---

### Sammanfattning
- **Använd `snake_case`** för variabler och funktioner i Python.
- **Använd `PascalCase`** för klassnamn.
- **Undvik reserverade ord** som variabelnamn.
- **Använd ett inledande understreck (`_`)** för skyddade variabler och dubbla understreck (`__`) för privata variabler i objektorienterad programmering.

Att följa dessa konventioner bidrar till att göra din kod mer läsbar och underhållbar.

---
### Bra Praxis för Kodstruktur
- **Använd indragningar:** För att tydligt visa block av kod som hör samman, som i loopar och funktioner.
- **Håll koden läsbar:** Skriv korta och tydliga rader. Om en rad blir för lång, överväg att bryta upp den.
- **Använd tomma rader:** För att separera logiska sektioner i koden och göra den mer lättläst.

###### Exempel:

```
total = 0
antal = 10

for i in range(antal):
    * total += i

 print(total)
```
---

## Sammanfattning
Dagens föreläsning har introducerat viktiga koncept som operatorer i Python och grundläggande kodstruktur. Genom att förstå och använda dessa på rätt sätt kan du skriva mer effektiv och läsbar kod. Nästa lektion kommer vi att fördjupa oss i kontrollstrukturer och hur de används för att styra flödet i dina program.

---

## Uppgifter för Vecka 35 - Fredag

1. **Grundläggande aritmetiska operationer**
   - Skriv ett program som ber användaren mata in två tal. Programmet ska sedan använda `+`, `-`, `*`, och `/` operatorerna för att beräkna och skriva ut summan, skillnaden, produkten och kvoten av dessa tal.
   - **Tidsåtgång:** 30-45 minuter.

2. **Jämförelse av två tal**
   - Skriv ett program som frågar användaren efter två tal. Programmet ska sedan använda jämförelseoperatorer (`>`, `<`, `==`, `!=`) för att jämföra dessa tal och skriva ut resultaten av dessa jämförelser. Programmet ska också avgöra vilket tal som är störst, eller om de är lika.
   - **Tidsåtgång:** 30-45 minuter.

---

3. **Beräkna kostnad med dricks**
   - Skriv ett program som frågar användaren efter priset på en vara. Programmet ska sedan fråga om användaren vill ge dricks. Om användaren svarar "ja", ska programmet lägga till en dricks på 10% av priset. Programmet ska sedan skriva ut slutpriset inklusive dricks.
   - **Tidsåtgång:** 30-45 minuter.

4. **Beräkna medelvärde av tre tal**
   - Skriv ett program som ber användaren mata in tre tal. Programmet ska beräkna medelvärdet av dessa tre tal och skriva ut resultatet med två decimaler. Om något av talen är negativt, skriv ut en varning om att negativa tal inte är tillåtna.
   - **Tidsåtgång:** 30-45 minuter.

---

5. **Skapa ett enkelt interaktivt äventyr**
   - Skriv ett program som simulerar ett enkelt textbaserat äventyrsspel. Programmet ska presentera användaren med en situation och flera val. Baserat på användarens val ska olika resultat visas. Använd if-elif-else-satser för att hantera användarens val och skapa olika scenarier. Använd `if`- och `else`-satser.
   - **Tidsåtgång:** 45-60 minuter.

6. **Kontrollera om ett tal är jämnt eller udda**
   - Skriv ett program som ber användaren mata in ett tal. Programmet ska använda modulus-operatorn (`%`) för att avgöra om talet är jämnt eller udda och skriva ut ett meddelande som informerar användaren om resultatet.
   - **Tidsåtgång:** 60-75 minuter.

---


7. **Beräkna totalkostnaden för flera varor**
   - Skriv ett program som ber användaren mata in priserna på tre olika varor. Programmet ska sedan beräkna den totala kostnaden för alla tre varorna inklusive moms (25%). Om den totala kostnaden överstiger 500 SEK, skriv ut ett meddelande som erbjuder 10% rabatt. Beräkna och skriv ut slutpriset efter eventuell rabatt.
   - **Tidsåtgång:** 45-60 minuter.

8. **Simulera en enkel frågesport**
   - Skriv ett program som ställer tre frågor till användaren. Varje fråga ska ha tre svarsalternativ. Programmet ska hålla reda på hur många rätt användaren får och skriva ut resultatet i slutet. Använd `if-else`-satser för att hantera svaren.
   - **Tidsåtgång:** 90-120 minuter.

---

9. **Skapa en enkel kalkylator**
   - Skriv ett program som fungerar som en enkel kalkylator. Användaren ska kunna mata in två tal och sedan välja en operation (addition, subtraktion, multiplikation, division). Programmet ska utföra den valda operationen och skriva ut resultatet. Lägg till hantering av ogiltiga inmatningar och fall som division med noll.
   - **Tidsåtgång:** 60-90 minuter.


10. **Slumpa ett tal och låt användaren gissa**
    - Skriv ett program som genererar ett slumpmässigt tal mellan 1 och 100. Låt användaren försöka gissa talet och ge feedback om gissningen är för hög eller för låg. Programmet ska fortsätta tills användaren gissar rätt. Använd `random`-modulen för att generera det slumpmässiga talet.
    - **Tidsåtgång:** 60-90 minuter.
