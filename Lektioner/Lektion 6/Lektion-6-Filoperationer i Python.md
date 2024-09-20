---
marp: true
paginate: true
theme: distansakademin
class: lead gaia
---


# Filhantering i Python

---

## Agenda
- Grundläggande filoperationer i Python
- Olika lägen för filhantering
- Läsa från filer: djupdykning i metoder och exempel
- Skriva till filer
- Hantering av undantag i samband med filhantering
- Uppgifter för praktiska övningar

---

## Inledning

I många program behöver vi kunna spara och läsa in data till och från filer. Filhantering är därför en viktig del av programmering, speciellt när du vill lagra information för senare användning. Python gör det enkelt att hantera filer genom att erbjuda ett intuitivt och flexibelt sätt att läsa och skriva till filer. Den här lektionen kommer att ge dig en djupare förståelse för hur du använder Pythons inbyggda funktioner för filhantering på ett säkert och effektivt sätt.

---

## Filoperationer i Python

För att kunna läsa och skriva till en fil i Python används funktionen `open()`. Denna funktion öppnar en fil och låter oss utföra olika operationer som att läsa, skriva eller lägga till data i filen.

Funktionen tar två huvudsakliga argument: filens namn och i vilket **läge** filen ska öppnas. Det finns olika lägen beroende på vad vi vill göra med filen.

Syntax:

```
fil = open('filnamn', 'läge')
```
---

### Viktigt!
När vi öppnar en fil måste vi alltid komma ihåg att stänga den när vi är klara. Annars kan det leda till problem som dataförlust eller att systemresurser inte frigörs korrekt. Vi använder `close()` för att stänga filen när vi är klara med den. Alternativt kan vi använda **with-satsen** för att hantera filer säkert, vilket automatiskt stänger filen när blocket är klart.

## Olika lägen för filhantering

När vi öppnar en fil behöver vi specificera vilket läge vi vill använda. Här är en mer komplett lista över de olika lägena som finns i Python för filhantering:

---

### Vanliga lägen:

- **'r'**: Öppnar filen i **läsläge**. Detta innebär att vi bara kan läsa från filen. Om filen inte finns, kommer ett fel att uppstå.
  
- **'w'**: Öppnar filen i **skrivläge**. Detta innebär att vi kan skriva till filen. Om filen inte finns, skapas den automatiskt. Om filen redan finns, skrivs innehållet över.

- **'a'**: Öppnar filen i **appendläge**. Det här läget används när vi vill lägga till data i slutet av en fil utan att radera det som redan finns där. Om filen inte finns, skapas den.

- **'x'**: Öppnar filen för **exklusiv skapelse**. Om filen redan finns, kastas ett fel (FileExistsError). Detta är användbart när du vill undvika att skriva över en befintlig fil.

---

- **'r+'**: Öppnar filen i **både läs- och skrivläge**. Vi kan både läsa och skriva till filen, men filen måste redan finnas.

- **'w+'**: Öppnar filen för både **skrivning och läsning**. Om filen inte finns, skapas den. Om den finns, kommer innehållet att raderas innan skrivning. Detta fungerar som `'w'`, men med möjligheten att läsa filen efter att ha skrivit.

- **'a+'**: Öppnar filen för både **append och läsning**. Data läggs till i slutet av filen, och vi kan fortfarande läsa innehållet. Om filen inte finns, skapas den.

---

### Binärlägen:
Alla ovanstående lägen kan också användas i **binärt läge** genom att lägga till ett **'b'** i slutet av läget. Detta gör att filen behandlas som en binärfil snarare än en textfil, vilket är användbart när du arbetar med bilder, videor eller andra filer som inte är ren text.

- **'rb'**: Öppnar en fil i binärt **läsläge**.
  
- **'wb'**: Öppnar en fil i binärt **skrivläge**. Om filen redan finns, skrivs den över.

- **'ab'**: Öppnar en fil i binärt **appendläge**. Data läggs till i slutet av filen.

- **'r+b'**: Öppnar en fil i både binärt **läs- och skrivläge**.

- **'w+b'**: Öppnar en fil i både binärt **skriv- och läsläge**. Filens innehåll skrivs över.

- **'a+b'**: Öppnar en fil i både binärt **append- och läsläge**.

---

### Sammanfattning:

- **'r'**: Läs från en fil (finns redan).
- **'w'**: Skriv till en fil (skriv över).
- **'a'**: Lägg till data till en fil.
- **'r+'**: Läs och skriv till en existerande fil.
- **'w+'**: Läs och skriv, skapa om den inte finns, skriv över om den finns.
- **'a+'**: Läs och lägg till data, skapa om den inte finns.
- **'x'**: Skapa en fil, kasta ett fel om den redan finns.
- Lägg till **'b'** för binärt läge (t.ex. `'rb'`, `'wb'`, `'ab'`).

Det här ger oss stor flexibilitet beroende på om vi vill skapa, läsa, skriva eller lägga till i filer och om vi vill arbeta med text eller binära filer.

---

## Läsa från en fil

När vi öppnar en fil i läsläge finns det flera olika metoder vi kan använda för att läsa innehållet. Varje metod är användbar beroende på vilken typ av data vi hanterar och hur stor filen är.

### 1. `read(size)`
Den här metoden läser hela filens innehåll som en enda stor sträng. Standardbeteendet är att läsa in hela filen om inget argument ges, men vi kan också specificera hur många tecken (eller bytes för binära filer) vi vill läsa genom att ange en parameter.

#### Parametrar:
- **size** *(valfritt)*: Anger hur många tecken (bytes) som ska läsas. Om inget anges, läses hela filen.

---

### Exempel:
```
fil = open('fil.txt', 'r')  
innehåll = fil.read()  
print(innehåll)  
fil.close()
```
---

### 2. `readline()`
Denna metod läser en rad i taget från filen. Varje gång vi anropar `readline()`, får vi nästa rad inklusive radbrytningen. Om vi vill kan vi också specificera hur många tecken vi vill läsa från den aktuella raden.

#### Parametrar:
- **size** *(valfritt)*: Anger hur många tecken från raden som ska läsas. Om inget anges, läses hela raden.

---

### Exempel:
Vi har en fil som innehåller strängen:  
"Hello, World! \n       
Python är kul"

```
fil = open('fil.txt', 'r')  
rad = fil.readline()  
print(rad)  # Skriver ut "Hello, World\n" 
rad = fil.readline() 
print(rad)   # Skriver ut "Python är kul"

fil.close()
```
---
### Exempel när parametern används
Vi har en fil som innehåller strängen "Hello, World! Python är kul."
```
fil = open('fil.txt', 'r')  

# Läser de första 5 tecknen från den första raden
rad = fil.readline(5)  
print(rad)  # skriver ut "Hello"

# Fortsätter att läsa de nästa 5 tecknen från samma rad
rad = fil.readline(5)  
print(rad)  # Skriver ut ", Wor"

fil.close()

```

---

### 3. `readlines(hint=-1)`
Denna metod läser hela filen och returnerar en lista där varje rad i filen blir ett element i listan. Om filen är stor kan vi begränsa antalet rader som läses genom att ange en parameter.

#### Parametrar:
- **hint** *(valfritt)*: Anger det maximala antalet tecken som ska läsas in totalt. Om detta värde är lägre än filens totala tecken, kommer läsningen att avbrytas efter att detta antal tecken har lästs.

---

### Exempel:
```
fil = open('fil.txt', 'r')  
alla_rader = fil.readlines()  
print(alla_rader)  
fil.close()
```
---

### Exempel när parametern används

```
fil = open('fil.txt', 'r')  
alla_rader = fil.readlines(20)  # Läser upp till totalt 20 tecken från filen  
print(alla_rader)  
fil.close()
```

---

### Iterera över filen med en for-loop

Ett smidigt sätt att läsa en fil rad för rad är att iterera över filobjektet direkt med en for-loop. Detta är minneseffektivt eftersom bara en rad laddas åt gången.

### Exempel:
```
fil = open('fil.txt', 'r') 
for rad in fil:  # Loopar igenom varje rad i filen
    print(rad.strip())  # strip() tar bort radbrytningar och extra mellanslag

fil.close()  # Stänger filen manuellt

```

---

## Använda with-satsen för säker filhantering

För att säkerställa att en fil stängs automatiskt, även om ett fel uppstår, kan vi använda **with-satsen**. Det gör koden säkrare och enklare att läsa, eftersom vi inte behöver stänga filen manuellt med `close()`.

Exempel:
```
with open('fil.txt', 'r') som fil:  
   innehåll = fil.read()  
   print(innehåll)
```
---

### Hantera filposition: `seek()` och `tell()`

Metoderna `seek()` och `tell()` används för att manipulera filens läsposition. Detta kan vara användbart i flera situationer, exempelvis när vi behöver läsa om en viss del av filen eller hoppa över en del av innehållet.

#### Exempel på en situation där man vill flytta läspekaren
Låt oss säga att vi har en fil med flera sektioner och att vi bara är intresserade av en specifik del i mitten av filen. Istället för att läsa hela filen från början, kan vi använda `seek()` för att hoppa direkt till den relevanta delen. Det kan också vara praktiskt när vi vill läsa in delar av en fil flera gånger utan att öppna om den..

---

### Så här fungerar metoderna:
- **`seek(offset, whence=0)`**: Flyttar läspekaren till ett nytt läge.
  - **offset** är antalet byte från det läge som definieras av `whence`.
  - **whence** anger varifrån vi ska börja räkna:
    - `0`: Början av filen (standardvärde).
    - `1`: Den aktuella positionen.
    - `2`: Filens slut.

- **`tell()`**: Returnerar den aktuella positionen för filens läspekare i antal byte från filens början.

---

Exempel:
```
with open('fil.txt', 'r') as fil:  
   print(f"Nuvarande position: {fil.tell()}")  # Skriver ut 0 (början av filen)
   fil.read(5)  
   print(f"Position efter att ha läst 5 tecken: {fil.tell()}")  # Skriver ut 5
   fil.seek(0)  # Återställ läspekaren till början av filen  
   print(f"Position efter seek(): {fil.tell()}")  # Skriver ut 0
```

---

Exempel på att använda seek med offset och whence

```
with open('fil.txt', 'r') as fil:  
    # Visa nuvarande position i början
    print(f"Nuvarande position: {fil.tell()}")  # Output: 0
    
    # Läs de första 10 tecknen
    första_delen = fil.read(10)
    print(första_delen)
    
    # Visa positionen efter att ha läst 10 tecken
    print(f"Position efter att ha läst 10 tecken: {fil.tell()}")  # Output: 10
    
    # Flytta läspekaren 5 tecken framåt från nuvarande position
    fil.seek(5, 1)  # Flyttar 5 tecken framåt från nuvarande position
    print(f"Position efter seek(5, 1): {fil.tell()}")  # Output: 15
    
    # Flytta läspekaren 5 tecken bakåt från filens slut
    fil.seek(-5, 2)  # Flyttar 5 tecken bakåt från slutet av filen
    print(f"Position efter seek(-5, 2): {fil.tell()}")
```
---


## Skriva till en fil

Metoden `write()` används för att skriva data till en fil. Den är kraftfull, men hur den beter sig beror på vilket läge vi öppnar filen i. Här är några saker att tänka på när vi skriver till en fil i Python:

---

### Viktigt om lägen för skrivning:
1. **'w' (write)**: Om vi öppnar filen i **'w'**-läge, skapas en ny fil om den inte finns. Om filen redan finns, **skrivs allt tidigare innehåll över**. Detta betyder att om vi vill bevara befintligt innehåll, är inte 'w' rätt läge att använda.
   
2. **'a' (append)**: Om vi öppnar filen i **'a'**-läge, kommer vi att **lägga till** ny data i slutet av filen utan att radera det befintliga innehållet. Detta är användbart om vi vill bevara allt som redan finns i filen och bara lägga till ny information.

3. **'x' (exclusive creation)**: Använder vi **'x'**-läge, försöker Python att **skapa** filen, men om den redan existerar kommer ett undantag att kastas. Detta kan vara användbart om vi vill undvika att skriva över en existerande fil.

---

### Om `write()`-metoden:
- **write()** skriver en sträng till filen. Den returnerar antalet tecken som skrevs, vilket kan vara användbart om du vill verifiera hur mycket data som skrivits.
- Det är viktigt att notera att du måste skriva strängar till filer med `write()`. Om du försöker skriva något annat, som ett tal, måste du först konvertera det till en sträng med `str()`.

---

### Exempel på att skriva till en fil i 'w'-läge:
```
with open('ny_fil.txt', 'w') as fil:  
    fil.write("Detta är en ny fil.\n") 
    fil.write("Denna fil innehåller två rader.\n") # Kommer skriva över den gamla filen
```
---

### Exempel på att skriva till en fil i 'a'-läge:
Om vi vill lägga till data till en redan existerande fil, använder vi **'a'**-läget (append):

```
with open('ny_fil.txt', 'a') as fil:  
    fil.write("Nu lägger vi till en ny rad.\n")
    fil.write("Nu lägger vi till ännu en ny rad.\n") # Nu kommer båda raderna finnas i filen

```

---

### Att tänka på vid användning av `write()`:
1. **Överskrivning i 'w'-läge**: Om du öppnar en fil i 'w'-läge och den redan existerar, raderas allt tidigare innehåll i filen och ersätts med den nya texten. Var försiktig när du använder 'w' om du inte vill förlora data.

2. **Radbrytningar**: När du använder `write()`, lägg till **'\n'** för att få en radbrytning. Python gör det inte automatiskt, så varje gång du skriver med `write()` kommer texten att placeras direkt efter den tidigare texten utan några radbrytningar om du inte anger det manuellt.

3. **Antal skrivna tecken**: Metoden `write()` returnerar antalet tecken som skrevs till filen. Detta kan vara användbart om du vill kontrollera hur mycket data som faktiskt har skrivits.

---

Exempel:
```
with open('ny_fil.txt', 'w') as fil:  
    antal_tecken = fil.write("Hej, världen!\n")  
    print(f"{antal_tecken} tecken skrevs till filen.")
```
---

### Sammanfattning:
- **write()** används för att skriva strängar till filer.
- I **'w'**-läge skrivs allt tidigare innehåll över, medan **'a'**-läge lägger till ny data i slutet av filen.
- Kom ihåg att lägga till **'\n'** för radbrytningar och att konvertera andra datatyper till strängar innan du skriver.
- Vid användning av `write()`, var försiktig med att inte av misstag överskriva viktiga filer, och överväg att använda **'a'**-läge om du vill bevara tidigare innehåll.

---


## Hantering av undantag

När vi hanterar filer är det viktigt att tänka på att olika typer av fel kan uppstå under filoperationer. Några vanliga fel kan vara att:

- Filen vi försöker öppna existerar inte (exempelvis på grund av en felaktig filväg).
- Vi har inte tillräckliga rättigheter för att öppna eller skriva till filen.
- Filen kan vara korrupt eller i ett format som vi inte förväntade oss.
- Det uppstår ett oväntat fel under filoperationen.

För att programmet ska fortsätta fungera och hantera dessa scenarier på ett kontrollerat sätt, kan vi använda **undanthantering** med hjälp av `try-except-else-finally`-block i Python. Detta gör att vi kan fånga och hantera specifika fel och ge användaren ett vänligt meddelande istället för att låta programmet krascha.

---

### Undantag och deras betydelse

Undantag är en mekanism för att hantera fel under körning. När något går fel kastas ett undantag, som stoppar det normala körflödet i programmet. Med hjälp av `try-except`-block kan vi fånga dessa undantag och hantera dem utan att programmet kraschar. Det är en central mekanism för att hantera osäkerhet i program, såsom fel vid filhantering.

---

### Vanliga undantag vid filhantering

När vi arbetar med filer kan vi stöta på flera olika typer av undantag. Här är några av de vanligaste och vad de innebär:

- **FileNotFoundError**: Detta undantag uppstår om filen som vi försöker öppna inte existerar.
- **PermissionError**: Detta undantag uppstår om vi inte har rättigheter att öppna, läsa eller skriva till filen.
- **IsADirectoryError**: Detta undantag uppstår om vi försöker öppna en katalog som om det vore en fil.
- **IOError**: Detta undantag kan uppstå vid en mängd olika fel som rör input/output-operationer, till exempel om filen är korrupt eller om det uppstår problem under skrivning eller läsning.

Genom att fånga specifika undantag kan vi ge mer informativ och användbar feedback till användaren.

---

### Struktur för undantagshantering: `try-except-else-finally`

Strukturen för undantagshantering består av fyra delar:

1. **try-blocket**: Här placerar vi koden som vi vill övervaka för potentiella fel.
2. **except-blocket**: Här fångar vi specifika eller generella undantag och definierar vad vi vill göra om ett undantag kastas.
3. **else-blocket** *(valfritt)*: Här placerar vi kod som körs om inget undantag inträffar i `try`-blocket.
4. **finally-blocket** *(valfritt)*: Här placerar vi kod som alltid ska köras, oavsett om ett undantag har inträffat eller inte. Detta är särskilt användbart för att stänga resurser som filer.

---

#### Exempel 1: Hantera ett `FileNotFoundError`

Här är ett exempel där vi försöker öppna en fil som inte finns. Vi fångar `FileNotFoundError` och skriver ut ett vänligt felmeddelande.
```
try:  
    fil = open('fil_som_inte_finns.txt', 'r')  
    innehåll = fil.read()  
except FileNotFoundError:  
    print("Fel: Filen existerar inte. Kontrollera filnamnet eller filvägen.")  
finally:  
    print("Denna kod körs alltid, oavsett om ett undantag uppstod eller inte.")
```
- **try**: Vi försöker öppna och läsa filen. Om filen inte finns, kommer undantaget `FileNotFoundError` att kastas.
- **except**: Om undantaget uppstår, fångas det här och vi skriver ut ett felmeddelande.
- **finally**: Detta block körs alltid, oavsett om ett undantag inträffade eller inte. Det är användbart när vi vill säkerställa att filen stängs, eller att resurser frigörs.

---

### Exempel 2: Hantera flera undantag

Vi kan också hantera flera typer av undantag. I detta exempel fångar vi både `FileNotFoundError` och `PermissionError`, beroende på vilket problem som uppstår.
```
try:  
    fil = open('viktig_fil.txt', 'r')  
    innehåll = fil.read()  
except FileNotFoundError:  
    print("Fel: Filen hittades inte.")  
except PermissionError:  
    print("Fel: Du har inte tillstånd att öppna denna fil.")  
finally:  
    print("Försöket att öppna filen är avslutat.")
```
- **PermissionError**: Om vi inte har tillräckliga rättigheter för att öppna filen, kastas detta undantag, och vi kan hantera det separat från `FileNotFoundError`.

---

### Exempel 3: Kombinera med `else`

Ett **else-block** kan användas tillsammans med try-except för att köra kod om inget undantag inträffar. Detta kan vara användbart för att separera lyckad logik från felhantering.
```
try:  
    fil = open('existerande_fil.txt', 'r')  
    innehåll = fil.read()  
except FileNotFoundError:  
    print("Fel: Filen existerar inte.")  
else:  
    print("Filen lästes in framgångsrikt!")  
finally:  
    print("Stänger programmet.")
```
- **else**: Det här blocket körs endast om inget undantag inträffar. Det är ett bra sätt att skilja logik där vi behandlar undantag från den normala flödeslogiken när allt går som förväntat.

---

### Exempel 4: Fånga generella undantag

Ibland vet vi inte exakt vilket fel som kan uppstå, så vi kan fånga alla typer av undantag genom att använda `Exception`. Detta gör att vi kan fånga generella fel och skriva ut ett meddelande med själva undantaget.

---

```
try:
    fil = open('fil.txt', 'r')
    innehåll = fil.read()
except Exception as e:
    print(f"Ett oväntat fel uppstod: {e}")
else:
    print("Filen lästes in framgångsrikt.")
finally:
    fil.close()  # Detta säkerställer att filen alltid stängs, oavsett om ett undantag inträffar.
```
- **Generellt undantag (Exception)**: Detta fångar alla typer av fel som inte fångas av de specifika undantagen. Vi använder variabeln `e` för att skriva ut information om det specifika felet.
- **else**: Detta block körs endast om inget undantag inträffar, vilket gör det användbart för att hantera den lyckade delen av koden separat från felhanteringen.
- **finally**: Används för att stänga filen eller frigöra andra resurser, oavsett om ett fel inträffade eller inte.

---

### Exempel 5: Använda undantag för att säkerställa att en fil stängs

Om vi inte använder `with`-satsen för att hantera filen, är det viktigt att vi manuellt stänger filen även om ett undantag uppstår. Vi kan använda `finally` för att säkerställa detta:
```
try:  
    fil = open('fil.txt', 'r')  
    innehåll = fil.read()  
except FileNotFoundError:  
    print("Fel: Filen hittades inte.")  
finally:  
    fil.close()  # Detta säkerställer att filen alltid stängs, även om ett undantag inträffar.
```
---

### Viktigt om undantagshantering i filhantering

- **Specifika undantag**: Fånga specifika undantag istället för generella. Det gör koden tydligare och lättare att felsöka.
- **Felmeddelanden**: Ge alltid tydliga och användbara felmeddelanden till användaren.
- **Resursfrigöring**: Använd `finally` för att säkerställa att resurser, som öppnade filer, alltid frigörs, även om ett fel inträffar.

---

### Sammanfattning av undantagshantering vid filoperationer

1. **try-except-else-finally**: Strukturen hjälper oss att fånga fel under körning utan att krascha programmet. Det låter oss hantera olika typer av undantag beroende på situationen.
2. **Vanliga undantag**: Vi kan fånga specifika undantag som `FileNotFoundError`, `PermissionError`, och andra för att hantera specifika problem vid filoperationer.
3. **Rätt resurshantering**: Det är viktigt att alltid stänga öppnade filer, vilket kan göras antingen manuellt i ett `finally`-block eller automatiskt med **with-satsen**.

---

## Sammanfattning

- Filhantering i Python görs med `open()`-funktionen.
- Det finns flera olika lägen för att öppna filer, beroende på om vi vill läsa, skriva eller lägga till data.
- Metoder som `read()`, `readline()`, `readlines()`, samt iteration över filen ger oss flexibilitet att läsa filer på olika sätt.
- Användning av **with-satsen** för filhantering är ett säkrare alternativ då den automatiskt stänger filen när operationen är klar.
- Hantering av undantag med **try-except** säkerställer att programmet inte kraschar om något går fel vid filhantering.

---

### Uppgifter

#### Uppgift 1: Läsa från en fil
1. Skapa en textfil och skriv in några rader text manuellt.
2. Skapa ett Python-program som läser filen rad för rad och skriver ut varje rad till skärmen.

---

#### Uppgift 2: Skriva till en fil
1. Skapa ett Python-program som frågar användaren efter deras namn och ålder.
2. Skriv den här informationen till en fil som heter `info.txt`.

---

#### Uppgift 3: Hantera filoperationer med undantag
1. Skapa ett Python-program som ber användaren om ett filnamn och använd sedan användarinput till att öppna filen.
2. Hantera detta med en try-except-block och skriv ett meddelande om filen inte hittas.

---

### Uppgift 4: Läsa och summera tal från en fil

1. Skapa en fil som innehåller flera rader med heltal (ett tal per rad).
2. Skapa ett Python-program som öppnar filen, läser varje rad, och summerar alla tal.
3. Programmet ska skriva ut summan av alla tal i filen.

---

### Uppgift 5: Skriva och läsa en lista från en fil

1. Skapa ett Python-program som ber användaren att mata in fem olika fruktnamn.
2. Programmet ska spara alla fruktnamnen i en fil som heter `frukter.txt`.
3. Efter att ha skrivit till filen, öppna filen igen och skriv ut alla fruktnamn som finns i filen.

---

### Uppgift 6: Skriva till en fil med datum

1. Skapa en fil med namnet `log.txt`.
2. Skriv ett Python-program som varje gång det körs, lägger till ett meddelande till filen `log.txt` som innehåller strängen "Programmet kördes" följt av aktuell tid och datum.
3. Använd append-läget ('a') för att säkerställa att tidigare data i filen inte skrivs över.

---

### Uppgift 7: Söka efter ett specifikt ord i en fil

1. Skapa en textfil som innehåller flera meningar.
2. Skriv ett Python-program som ber användaren om ett ord att söka efter i filen.
3. Programmet ska öppna filen, söka efter ordet och skriva ut hur många gånger ordet förekommer i filen.

---

### Uppgift 8: Räkna rader och ord i en fil

1. Skapa en textfil som innehåller några meningar.
2. Skriv ett Python-program som öppnar filen och räknar antalet rader och det totala antalet ord i filen.
3. Programmet ska skriva ut både antalet rader och antalet ord.

---

### Uppgift 9: Spara och läsa dictionaries till/från en fil

1. Skapa ett Python-program som ber användaren att mata in namn och åldrar för fem olika personer.
2. Spara dessa uppgifter i en dictionary, där namnet är nyckeln och åldern är värdet.
3. Skriv denna dictionary till en fil i ett format som är lättläst.
4. Skapa sedan ett nytt program som öppnar filen, läser innehållet och skriver ut dictionaryn.
