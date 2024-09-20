---
marp: true
paginate: true
theme: distansakademin
class: lead gaia
---

# Föreläsning: Kontrollstrukturer och Loopar i Python

---

## Inledning
Den här föreläsningen syftar till att fördjupa din förståelse för kontrollstrukturer i Python, inklusive if-satser, for- och while-loopar. Dessutom kommer vi att introducera datatypen listor, som ofta används tillsammans med loopar för att hantera samlingar av data.

---

## Kontrollstrukturer i Python

### If-satser
If-satser används för att fatta beslut i ett program baserat på vissa villkor. Vi har tidigare gått igenom grunderna för if-, elif- och else-satser. Låt oss nu fördjupa oss i loopar.

---

## Loopar i Python

### For-loopar
En for-loop används för att iterera över en sekvens, såsom en lista, en sträng eller ett intervall av tal. For-loopar är mycket användbara när du vet i förväg hur många gånger du vill upprepa en operation.

---

### Iterera över en sekvens

En sekvens i Python kan vara vilken itererbar typ som helst, såsom en lista, ett intervall (range), eller en sträng. Varje element i sekvensen bearbetas i tur och ordning.

#### Grundläggande Syntax
```
for element in sekvens:
    kör denna kod för varje element i sekvensen
```
---

#### Exempel med Lista
```
frukter = ["äpple", "banan", "körsbär"]
for frukt i frukter:
    print(frukt)
```
I detta exempel itererar loopen över listan frukter och skriver ut varje frukt. Notera att variabeln frukt tar värdet av varje element i listan för varje iteration.

---

### Iterera över ett Intervall

Python har en inbyggd funktion range() som genererar en sekvens av tal, vilket är användbart när du vill iterera över ett intervall.
```
for i in range(1, 6):
    print(i)
```
Här itererar loopen över tal från 1 till 5. range(1, 6) skapar en sekvens av tal från 1 till 5, där den sista siffran är exkluderad.

---

### While-loopar
En while-loop upprepas så länge ett angivet villkor är sant. Den är användbar när du inte vet i förväg hur många gånger du behöver repetera en operation.

---

### Grundläggande While-loop
```
while villkor:
    kör denna kod så länge villkoret är sant
```
Denna loop fortsätter att köra den indragna koden så länge villkoret är sant. Det är viktigt att se till att villkoret så småningom blir falskt för att undvika oändliga loopar.

---

#### Exempel med While-loop
```
i = 1
while i <= 5:
    print(i)
    i += 1
```
Här skriver loopen ut värdet på i från 1 till 5 och ökar i med 1 för varje iteration. När i blir 6 upphör loopen att köras eftersom villkoret i <= 5 inte längre är sant.

---

### Användning av break och continue

- **Break:** Används för att omedelbart avbryta en loop.
- **Continue:** Används för att hoppa över den aktuella iterationen och fortsätta med nästa.

#### Exempel:
```
for i in range(10):
    if i == 5:
        break  # Avbryter loopen när i är 5
    if i % 2 == 0:
        continue  # Hoppar över jämna tal
    print(i)
```

Detta program skriver endast ut udda tal mellan 0 och 5, eftersom jämna tal hoppas över med continue och loopen avbryts när i blir 5.

---

## Datatypen Listor

### Vad är en Lista?
En lista i Python är en samling av element som kan bestå av olika datatyper. Listor är ordnade och indexerade, vilket innebär att varje element har en position som börjar med 0.

#### Skapa en Lista
```
min_lista = [1, 2, 3, 4, 5]
```
I detta exempel har vi skapat en lista med fem heltal. Listor kan också innehålla strängar, andra listor, eller blandade datatyper.

---

### Åtkomst till Element i en Lista

Du kan få åtkomst till ett specifikt element i en lista genom att använda dess index.
```
frukter = ["äpple", "banan", "körsbär"]
första_frukten = frukter[0]  # Ger "äpple"
```
Notera att listindex börjar på 0, så frukter[0] ger det första elementet.

---

### Loopar och Listor

Listor används ofta tillsammans med for-loopar för att iterera över alla element i listan. Detta är ett kraftfullt verktyg för att bearbeta och manipulera samlingar av data.

#### Exempel:
```
tal = [1, 2, 3, 4, 5]
summa = 0

for nummer i tal:
    summa += nummer

print("Summan är:", summa)
```
Detta program summerar alla tal i listan tal och skriver ut resultatet.

---

### Listmetoder
Listor har flera användbara metoder, såsom append(), remove(), och sort(), som gör det enkelt att manipulera listdata.

#### Exempel:
```
frukter = ["äpple", "banan", "körsbär"]
frukter.append("druva")  # Lägg till ett element
frukter.remove("banan")  # Ta bort ett element
frukter.sort()  # Sortera listan alfabetiskt
```
---
## Strängmetoder i Python: .split() och liknande funktioner

När vi arbetar med strängar i Python finns det många inbyggda metoder som gör det enkelt att bearbeta och manipulera text. En av de mest användbara strängmetoderna är `.split()`, som används för att dela upp en sträng i en lista av substrängar baserat på ett specifikt avgränsningstecken.

---

#### Vad är `.split()`?

`.split()` är en metod som används för att dela upp en sträng i flera delar, och returnerar dessa delar som en lista. Standardavgränsaren är ett mellanslag, men du kan specificera ett annat tecken som avgränsare.

---

#### Grundläggande användning:

Om vi har strängen `text = "Det här är en mening"`, och vi använder `ord_lista = text.split()`, kommer den att dela upp strängen vid varje mellanslag och skapa en lista `ord_lista` som innehåller varje ord som ett separat element: `['Det', 'här', 'är', 'en', 'mening']`.

---

#### Dela upp strängar med andra avgränsare:

Du kan också ange ett specifikt tecken som avgränsare. Om du till exempel har en sträng där orden är separerade med kommatecken, kan du använda `.split(",")` för att dela upp strängen.

Till exempel: Om vi har strängen `data = "äpple,banan,körsbär"` och om vi använder `frukt_lista = data.split(",")` får vi en lista `frukt_lista` som innehåller `['äpple', 'banan', 'körsbär']`.

---

#### Andra användbara strängmetoder:

- `.join()`: Används för att slå samman en lista av strängar till en enda sträng, med ett specifikt tecken mellan varje element. Om vi har en lista `lista = ["Det", "här", "är", "en", "mening"]` kan vi använda `mening = " ".join(lista)` för att få strängen `"Det här är en mening"`.

- `.strip()`: Tar bort ledande och efterföljande mellanslag (eller andra specifika tecken) från en sträng. Om vi har strängen `text = "   Hej världen!   "` och använder `text = text.strip()` får vi `"Hej världen!"`.

- `.replace()`: Ersätter alla förekomster av en delsträng med en annan delsträng. Om vi har strängen `text = "Jag älskar bananer"` och använder `text = text.replace("bananer", "äpplen")` får vi `"Jag älskar äpplen"`.

---

#### Användning av `.split()` i program:

Om du till exempel ber en användare att mata in flera ord eller tal separerade med mellanslag eller kommatecken, kan du använda `.split()` för att omvandla inmatningen till en lista som du sedan kan iterera över eller bearbeta vidare.

Om vi har `input_str = "10,20,30,40,50"` och använder `tal_lista = input_str.split(",")` på den, omvandlas strängen till en lista `tal_lista` med värdena `[10, 20, 30, 40, 50]`.

Dessa strängmetoder är viktiga verktyg i Python som hjälper till att enkelt bearbeta och manipulera textdata, vilket är särskilt användbart när man arbetar med inmatning från användare eller analyserar textinnehåll.

---


## Uppgifter för Vecka 36 - Tisdag

1. **Kontrollera om ett tal är udda eller jämnt**
   - Skriv ett program som frågar användaren om ett tal och använder en if-sats för att avgöra om talet är jämnt eller udda. Använd modulus-operatorn (%) för att göra detta.
   - **Tidsåtgång:** 30-45 minuter.

---

2. **Iterera över en lista och skriv ut element**
   - Skriv ett program som tar en lista med minst fem element och itererar över den med en for-loop. Programmet ska skriva ut varje element i listan.
   - **Tidsåtgång:** 30 minuter.

---

3. **Beräkna summan av tal med en while-loop**
   - Skriv ett program som använder en while-loop för att beräkna summan av alla heltal från 1 till 100. Skriv ut resultatet när loopen är klar.
   - **Tidsåtgång:** 45 minuter.

---

4. **Kontrollera om ett tal finns i en lista**
   - Skriv ett program som frågar användaren om ett tal och kontrollerar om detta tal finns i en fördefinierad lista. Använd en for-loop och en if-sats för att avgöra om talet finns i listan och skriv ut ett meddelande beroende på resultatet.
   - **Tidsåtgång:** 30 minuter.


---

5. **Hitta det största talet i en lista**
   - Skriv ett program som itererar över en lista med heltal och hittar det största talet. Använd en for-loop och en if-sats för att jämföra talen.
   - **Tidsåtgång:** 45 minuter.

---

6. **Beräkna produkten av tal i en lista**
   - Skriv ett program som tar en lista med minst fem heltal och beräknar produkten av alla tal i listan. Använd en for-loop för att multiplicera varje tal med varandra.
   - **Tidsåtgång:** 30 minuter.

---

7. **Simulera ett enkelt spel**
   - Skapa ett enkelt spel där användaren får försöka gissa ett slumpmässigt tal mellan 1 och 50. Använd en while-loop för att låta användaren fortsätta gissa tills rätt tal hittas. Ge feedback om gissningen är för hög eller för låg.
   - **Tidsåtgång:** 60 minuter.

---

8. **Beräkna medelvärdet av tal i en lista**
   - Skriv ett program som tar en lista med minst fem heltal och beräknar medelvärdet av dessa tal. Använd en for-loop för att summera talen och dela summan med antalet tal för att få medelvärdet.
   - **Tidsåtgång:** 45 minuter.

---

9. **Strängmanipulation och listor**
   - Skriv ett program som tar en lista med minst fem strängar som användaren matar in. Programmet ska skapa en ny lista som innehåller de ursprungliga strängarna, men där varje sträng är konverterad till versaler (stora bokstäver). Om en sträng redan är i versaler ska den inte inkluderas i den nya listan. I slutet ska programmet skriva ut den nya listan.
   - **Tidsåtgång:** 60-90 minuter.

---

10. **Skapa ett program för att hantera en inköpslista**
   - Skriv ett program som låter användaren skapa en inköpslista. Användaren ska kunna lägga till nya varor, ta bort varor och se hela listan. Använd en while-loop för att fortsätta fråga användaren vad de vill göra tills de väljer att avsluta programmet.
   - **Tidsåtgång:** 60-90 minuter.

---

