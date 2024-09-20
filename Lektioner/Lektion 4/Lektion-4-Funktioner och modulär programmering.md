---
marp: true
paginate: true
theme: distansakademin
class: lead gaia
---

# Funktioner och Modulär Programmering i Python

---

## Agenda
    - Vad är funktioner
    - Inbyggda funktioner
    - Filhantering
    - Dicts
    - Modulär programmering

---
## Inledning

Denna föreläsning ger en djupgående förståelse för funktioner i Python. Vi kommer att utforska grundläggande funktioner, inbyggda funktioner, strängfunktioner, listfunktioner och modulär programmering. Vi kommer också att förklara hur parametrar fungerar i dessa funktioner och varför vissa har specifika syntaxer.

---

## Funktioner i Python

### Vad är en Funktion?

En funktion är ett block av kod som är designad för att utföra en specifik uppgift. Funktioner kan ta emot data (parametrar), bearbeta denna data och returnera ett resultat. De hjälper till att organisera kod och göra den mer läsbar och återanvändbar.

---

#### Grundläggande Syntax
```
def funktionens_namn(parametrar):
    # kod som utförs
    return resultat
```
- **def**: Nyckelordet som används för att definiera en funktion
- **funktionens_namn**: Namnet på funktionen
- **parametrar**: Data som skickas till funktionen
- **return**: Värdet som skickas tillbaka från funktionen

---

## Inbyggda Funktioner

Python har ett stort antal inbyggda funktioner som kan användas utan att definiera egna funktioner. Låt oss titta på några av de vanligaste funktionerna och de parametrar de tar.

---

### len()

Returnerar längden på ett objekt (t.ex., antal element i en lista eller antal tecken i en sträng). Den tar en enda parameter, som är det objekt vars längd du vill räkna.
```
print(len("Hej världen!"))  # Output: 12  
print(len([1, 2, 3, 4]))   # Output: 4  
```
### type()

Returnerar typen av ett objekt. Den tar också en enda parameter, som är det objekt vars typ du vill undersöka.
```
print(type(42))           # Output: <class 'int'>  
print(type("Python"))    # Output: <class 'str'>  
```
---

### range()

Genererar en sekvens av tal och används ofta med loopar. Funktionen kan ta upp till tre parametrar:

- **En parameter**: `range(stop)` – Genererar en sekvens från 0 till `stop-1`.
- **Två parametrar**: `range(start, stop)` – Genererar en sekvens från `start` till `stop-1`.
- **Tre parametrar**: `range(start, stop, step)` – `step` specificerar stegen mellan varje tal.

Exempel:
```
for i in range(2, 10, 2):
    print(i)
```
Här börjar sekvensen vid 2, slutar innan 10, och ökar med steg om 2.

---

### sum()

Beräknar summan av alla element i en iterable (t.ex., lista). Funktionen tar två parametrar:

- **En iterable**: Den obligatoriska parametern där elementen summeras.
- **En startparameter**: Den valfria startparametern anger ett värde att börja summeringen från, och standardvärdet är 0.

Exempel:
```
print(sum([1, 2, 3, 4], 10))  # Output: 20
```
---

### max() och min()

Båda dessa funktioner returnerar det största respektive minsta värdet i en iterable eller bland flera givna argument. De kan ta en iterable eller flera enskilda argument.

Exempel:
```
print(max(1, 5, 3))  # Output: 5  
print(min([1, 2, 3, 4]))  # Output: 1  
```
---

### map()

Används för att applicera en funktion på varje element i en iterable och returnera en ny iterable med resultaten. Den tar två parametrar:

- **En funktion**: Den första parametern är den funktion som ska appliceras på varje element.
- **En iterable**: Den andra parametern är den iterable vars element ska bearbetas.

Exempel:
```
print(list(map(int, ["1", "2", "3"])))  # Output: [1, 2, 3]  
```
---

## Strängfunktioner

Python erbjuder ett antal inbyggda metoder för att manipulera strängar, och de tar vanligtvis specifika parametrar som tillåter flexibla operationer.

---

### .upper() och .lower()

Konverterar strängar till stora respektive små bokstäver. De tar inga parametrar eftersom de direkt arbetar på strängens innehåll.

Exempel:
```
text = "Hello World"  
print(text.upper())  # Output: HELLO WORLD  
print(text.lower())  # Output: hello world  
```
---

### .strip()

Tar bort ledande och efterföljande mellanslag från en sträng. Den tar en valfri parameter som specificerar vilka tecken som ska tas bort. Standard är att ta bort mellanslag.

Exempel:
```
text = "   Hej   "  
print(text.strip())  # Output: Hej  
```
---

### .split()

Delar en sträng i en lista av substrängar baserat på ett avgränsningstecken. Den tar en valfri parameter som anger avgränsaren. Om ingen avgränsare anges, används mellanslag.

Exempel:
```
text = "äpple,banan,körsbär"  
print(text.split(","))  # Output: ['äpple', 'banan', 'körsbär']  
```
---

### .join()

Slår samman en lista av strängar till en enda sträng med ett specifikt tecken mellan varje element. Här anges separatorn (strängen som du vill använda för att sammanfoga elementen) först. Detta är en speciell syntax där separatorn är strängen på vilken du anropar metoden.

Exempel:
```
lista = ["Hej", "världen"]  
print(" ".join(lista))  # Output: Hej världen  
```
Förklaringen till varför separatorn anges först är att `join()` är en metod på strängobjektet, där strängen fungerar som det "lim" som binder samman elementen i iterable.

---

### .replace()

Ersätter alla förekomster av en delsträng med en annan delsträng. Den tar två parametrar:

- **old**: Den delsträng som ska ersättas.
- **new**: Den nya delsträngen som ska ersätta den gamla.

Exempel:
```
text = "Hej världen"  
print(text.replace("världen", "Python"))  # Output: Hej Python  
```
---

## Listfunktioner

Listor i Python har flera användbara metoder som tar olika typer av parametrar.

---

### .append()

Lägger till ett element i slutet av en lista. Den tar en enda parameter, som är det objekt du vill lägga till i listan.

Exempel:
```
lista = [1, 2, 3]  
lista.append(4)  
print(lista)  # Output: [1, 2, 3, 4]  
```
---

### .remove()

Tar bort det första förekomsten av ett specifikt element. Den tar en parameter som specificerar vilket element som ska tas bort.

Exempel:
```
lista = [1, 2, 3, 2]  
lista.remove(2)  
print(lista)  # Output: [1, 3, 2]  
```
---

### .extend()

Lägger till alla element från en annan iterable till listan. Den tar en iterable som parameter.

Exempel:
```
lista = [1, 2]  
lista.extend([3, 4])  
print(lista)  # Output: [1, 2, 3, 4]  
```
---

### .pop()

Tar bort och returnerar det sista elementet i listan eller ett element vid ett specificerat index. Den tar en valfri parameter som anger indexet på elementet som ska tas bort. Standard är det sista elementet.

Exempel:
```
lista = [1, 2, 3]  
print(lista.pop())  # Output: 3  
print(lista.pop(0))  # Output: 1  
print(lista)  # Output: [2]  
```
---

### .sort() och .sorted()

Sorterar en lista på plats eller returnerar en sorterad kopia av en lista. `.sort()` tar en valfri parameter `key` som kan användas för att ange en funktion för att styra sorteringsordningen. `.sorted()` fungerar på liknande sätt men returnerar en ny lista.

Exempel:
```
lista = [3, 1, 2]  
lista.sort()  
print(lista)  # Output: [1, 2, 3]  
```
```
lista = [3, 1, 2]  
print(sorted(lista))  # Output: [1, 2, 3]  
```
---

### .reverse()

Vänder på ordningen av elementen i listan på plats. Den tar inga parametrar.

Exempel:
```
lista = [1, 2, 3]  
lista.reverse()  
print(lista)  # Output: [3, 2, 1]  
```
---

## Funktioner med Variabla Antal Parametrar

Python ger stöd för att skapa funktioner som tar emot ett variabelt antal positionella och nyckelordsargument med hjälp av `*args` och `**kwargs`.

### *args

- **args** samlar ett godtyckligt antal positionella argument i en tuple.

Exempel:
```
def summa(*args):
    return sum(args)

print(summa(1, 2, 3, 4))  # Output: 10  
```
---

### **kwargs

- **kwargs** samlar nyckelordsargument i en dictionary.

Exempel:
```
def hälsa(**kwargs):
    for namn, ålder in kwargs.items():
        print(f"{namn} är {ålder} år gammal.")

hälsa(Anna=25, Erik=30)  
# Output: Anna är 25 år gammal.  
# Output: Erik är 30 år gammal.  
```
---

## Lambda-funktioner

Lambda-funktioner är små, anonyma funktioner som definieras med nyckelordet `lambda`. De används oftast för att skapa enkla funktioner på en rad.

---

### Syntax

lambda argument: uttryck

Exempel:
```
addera = lambda x, y: x + y  
print(addera(5, 3))  # Output: 8  
```
---

## Funktioner som Returnerar Funktioner

En funktion kan returnera en annan funktion. Detta är användbart för att skapa högre ordningens funktioner, som kan skapa specialiserade versioner av en funktion baserat på vissa parametrar.

Exempel:
```
def skapa_adderare(n):
    def addera(x):
        return x + n
    return addera

addera_5 = skapa_adderare(5)  
print(addera_5(10))  # Output: 15  
```
---
# Filhantering i Python

---

## Introduktion till Filhantering

Att kunna läsa från och skriva till filer är en viktig del av många program. I Python är filhantering enkelt att implementera, och du kan arbeta med både text- och binärfiler. I denna sektion kommer vi att introducera grunderna för filhantering och använda funktioner för att läsa och skriva till filer.

---

## Grundläggande Syntax för att Öppna Filer

För att öppna en fil i Python använder vi funktionen `open()`. Den tar två argument:

- **filnamn**: Namnet på filen som du vill öppna.
- **läge**: Hur filen ska öppnas (skrivläge, läsläge, etc.).

Exempel:
```
file = open("filnamn.txt", "r")  # Öppnar filen för läsning
file = open("filnamn.txt", "w")  # Öppnar filen för skrivning (raderar tidigare innehåll)
file = open("filnamn.txt", "a")  # Öppnar filen för att lägga till text
```
---

## Läsa från en Fil

När du har öppnat en fil för läsning kan du använda olika metoder för att läsa innehållet:

- **.read()**: Läser hela filens innehåll.
- **.readline()**: Läser en rad i taget.
- **.readlines()**: Läser alla rader och returnerar dem som en lista.

Exempel:
```
file = open("filnamn.txt", "r")
innehåll = file.read()
print(innehåll)
file.close()
```
---

## Skriva till en Fil

För att skriva till en fil kan du använda lägena `"w"` (skrivläge) eller `"a"` (lägg till-läge):

Exempel:
```
file = open("filnamn.txt", "w")
file.write("Detta är en ny rad i filen.")
file.close()
```
---

## Att Stänga Filer

När du har läst eller skrivit till en fil är det viktigt att stänga den med **.close()** för att frigöra systemresurser.

---

## Hantera Filer med `with`

Du kan använda `with` för att automatiskt stänga filen när du är klar med den. Detta är att föredra eftersom du inte riskerar att glömma att stänga filen.

Exempel:
```
with open("filnamn.txt", "r") as file:
    innehåll = file.read()
    print(innehåll)
```
Med `with`-syntaxen stängs filen automatiskt när koden inom blocket är klar.

---

## Exempel på Användning

### 1. Läs Innehållet i en Fil
```
with open("dagbok.txt", "r") as file:
    dagbok = file.read()
    print(dagbok)
```
### 2. Skriv en Dagboksanteckning till en Fil
```
with open("dagbok.txt", "a") as file:
    file.write("\nIdag lärde jag mig om filhantering i Python!")
```
---

## Sammanfattning

Filhantering i Python är en funktion som låter dig spara och läsa data från filer. Genom att förstå hur du öppnar, läser, skriver och stänger filer kan du skapa mer komplexa och användbara program som hanterar data på ett effektivt sätt.

---

### Dictionaries (Dicts) i Python

En dictionary (dict) i Python är en datastruktur som lagrar data i nyckel-värde-par. Till skillnad från listor som indexeras med heltal, indexeras dictionaries med nycklar, vilket kan vara vilken oföränderlig datatyp som helst (t.ex. strängar eller tal). Detta gör dictionaries mycket användbara när du vill associera en nyckel med ett specifikt värde.

---

#### Skapa en dictionary
En dictionary skapas genom att placera nyckel-värde-par i klamrar {}. Varje par separeras med ett kolon `:`, och varje nyckel-värde-par separeras med ett kommatecken.

Exempel:
```
person = {"namn": "Anna", "ålder": 30, "stad": "Stockholm"}
```
I detta exempel är "namn", "ålder", och "stad" nycklar, medan "Anna", 30, och "Stockholm" är deras motsvarande värden.

---

#### Åtkomst till värden
Du kan få åtkomst till ett värde i en dictionary genom att använda nyckeln inom hakparenteser [].

Exempel:
```
print(person["namn"])  # Output: Anna  
print(person["ålder"])  # Output: 30
```
---

#### Lägg till eller uppdatera ett värde
För att lägga till ett nytt nyckel-värde-par eller uppdatera ett befintligt värde kan du tilldela ett värde till en nyckel.

Exempel:
```
person["land"] = "Sverige"  # Lägg till ny nyckel och värde  
person["ålder"] = 31  # Uppdatera värdet för en befintlig nyckel
```
---

#### Ta bort ett värde
För att ta bort ett nyckel-värde-par kan du använda `del` eller metoden `.pop()`.

Exempel:
```
del person["stad"]  # Tar bort nyckel-värde-paret med nyckeln "stad"
```
---

#### Vanliga metoder för dictionaries:
- **`.keys()`**: Returnerar alla nycklar i dictionaryn.
- **`.values()`**: Returnerar alla värden i dictionaryn.
- **`.items()`**: Returnerar en vy av både nycklar och värden som tuple-par.

Exempel:

```
person = {"namn": "Anna", "ålder": 31, "land": "Sverige"}

print(person.keys())  # Output: dict_keys(['namn', 'ålder', 'land'])  
print(person.values())  # Output: dict_values(['Anna', 31, 'Sverige'])  
print(person.items())  # Output: dict_items([('namn', 'Anna'), ('ålder', 31), ('land', 'Sverige')])
```
---

#### Sammanfattning:
Dictionaries är en kraftfull datastruktur för att hantera data i form av nyckel-värde-par. De erbjuder snabb åtkomst till värden baserat på nycklar och är mycket flexibla och dynamiska, vilket gör dem lämpliga för många olika programmeringsproblem.

---

## Modulär Programmering

### Fördelar med Modulär Programmering

- **Återanvändbarhet**: Funktioner kan återanvändas i olika delar av programmet, vilket minskar duplicering av kod.
- **Lättare att underhålla**: Kod är mer organiserad och lättare att felsöka.
- **Modularisering**: Kod delas upp i hanterbara delar, vilket gör programmet lättare att underhålla och vidareutveckla.

---

Exempel på modulär programmering:
```
def läs_lista():
    return list(map(int, input("Skriv in tal separerade med kommatecken: ").split(",")))

def beräkna_summa(lista):
    return sum(lista)

def skriv_ut_resultat(resultat):
    print(f"Summan är: {resultat}")

lista = läs_lista()  
resultat = beräkna_summa(lista)  
skriv_ut_resultat(resultat)  
```
Här delas uppgiften upp i tre funktioner: läs_lista(), beräkna_summa() och skriv_ut_resultat(), vilket gör koden lättare att förstå och underhålla.

---

### Användning av Funktioner i Modulär Programmering

Modulär programmering innebär att du delar upp din kod i separata moduler eller filer som var och en hanterar en specifik del av din programlogik. Istället för att ha all kod i en enda fil, kan du skapa flera mindre filer (moduler) som innehåller specifika funktioner eller klasser. Dessa moduler kan sedan importeras och användas i ditt huvudprogram.

### Fördelar med Modulär Programmering

- **Återanvändbarhet**: Moduler kan användas i flera program utan att du behöver skriva om funktioner. Du kan helt enkelt importera dem och använda dem när du behöver.
  
- **Lättare att underhålla**: När funktioner och logik är uppdelade i moduler är det enklare att hitta och rätta till fel eller förbättra koden utan att påverka andra delar av programmet.
  
- **Modularisering**: Kod som är uppdelad i mindre moduler är lättare att förstå och vidareutveckla. Varje modul hanterar en specifik uppgift eller funktionalitet.

---

### Exempel på Modulär Programmering med Flera Filer

Låt oss säga att du vill skapa ett program som tar in en lista av tal, beräknar summan av dessa tal, och skriver ut resultatet. Istället för att ha all kod i en enda fil kan du dela upp detta i flera moduler.

---

#### Fil 1: `input_modul.py`
Den här filen innehåller en funktion som hanterar inmatningen av listan med tal.

```
def läs_lista():
    return list(map(int, input("Skriv in tal separerade med kommatecken: ").split(",")))
```
---

#### Fil 2: `beräkning_modul.py`
Denna fil innehåller en funktion för att beräkna summan av tal i en lista.
```
def beräkna_summa(lista):
    return sum(lista)
```

---

#### Fil 3: `output_modul.py`
Denna fil innehåller en funktion som skriver ut resultatet.
```
def skriv_ut_resultat(resultat):
    print(f"Summan är: {resultat}")
```

---

#### Huvudfil: `huvudprogram.py`
Huvudprogrammet samlar alla moduler och kör programmet genom att importera och anropa funktionerna från de andra filerna.
```
from input_modul import läs_lista
from beräkning_modul import beräkna_summa
from output_modul import skriv_ut_resultat

lista = läs_lista()
resultat = beräkna_summa(lista)
skriv_ut_resultat(resultat)
```

---

### Hur fungerar detta?

1. **`input_modul.py`**: Här har du en funktion som hanterar inmatning. Den tar in en lista med tal från användaren och returnerar den.
   
2. **`beräkning_modul.py`**: Denna fil innehåller en funktion som tar in listan och beräknar summan av alla tal.
   
3. **`output_modul.py`**: Denna fil har en funktion som tar resultatet (summan) och skriver ut det på skärmen.

4. **`huvudprogram.py`**: Här importeras alla moduler och funktioner, och programmet körs genom att anropa de olika funktionerna i rätt ordning.

---

### Importera Moduler

För att använda funktioner från andra filer (moduler) använder vi `import`-satsen. Här är några exempel på hur du kan importera moduler och funktioner:

---

#### Importera hela modulen:
```
import input_modul
lista = input_modul.läs_lista()
```
---

#### Importera en specifik funktion:
```
from input_modul import läs_lista
lista = läs_lista()
```

---

#### Importera flera funktioner från en modul:
```
from input_modul import läs_lista, en_annan_funktion
```

---

### Sammanfattning

I modulär programmering delar du upp ditt program i flera filer, där varje fil (modul) innehåller funktioner som är relaterade till en specifik uppgift. Du kan sedan importera dessa moduler i ditt huvudprogram, vilket gör koden lättare att hantera, underhålla och återanvända.

Att arbeta med moduler förbättrar också strukturen och gör det enklare att bygga större projekt genom att varje del är mer fristående och kan utvecklas separat från resten av programmet.

---

# Uppgifter för Modulär Programmering i Python

### 1. **Modulär textomvandlare**
   - Skapa ett program som delas upp i två moduler (filer):
     - Den ena modulen ska innehålla en funktion som konverterar en text till versaler.
     - Den andra modulen ska innehålla en funktion som tar bort alla mellanslag i texten.
   - I huvudprogrammet ska användaren kunna välja vilken omvandling de vill göra på en given text.

---

### 2. **Filtrera lista med funktioner**
   - Dela upp programmet i två moduler:
     - En modul med en funktion som filtrerar en lista och returnerar endast strängar som innehåller en viss bokstav (t.ex. 'a').
     - En annan modul som filtrerar ut alla strängar som är längre än ett visst antal tecken (specificerat av användaren).
   - Låt huvudprogrammet fråga användaren vilken filtrering de vill använda på en lista av strängar som de matar in.

---

### 3. **Valutaomvandlare med modulär struktur**
   - Skapa en modul som innehåller funktioner för att omvandla svenska kronor till tre andra valutor (USD, EUR, GBP). Använd fasta växelkurser.
   - Skapa ett huvudprogram där användaren får mata in ett belopp i SEK och välja till vilken valuta de vill omvandla.

---

### 4. **Användarhantering med modulär programmering**
   - Skapa ett program uppdelat i tre filer:
     - En modul för att lägga till användare (med namn och ålder) till en dict.
     - En modul för att söka efter användare i listan och returnera deras information.
     - En modul för att skriva ut alla användare.
   - Huvudprogrammet ska låta användaren välja vilken operation de vill utföra (lägga till, söka eller visa alla användare).
  

---

### 5. **Interaktiv uppgiftslista (todo-lista)**
   - Dela upp programmet i moduler:
     - En modul för att lägga till nya uppgifter.
     - En modul för att markera uppgifter som klara.
     - En modul för att ta bort uppgifter.
     - En modul för att visa uppgifter
   - Använd en lista för att lagra uppgifterna och en while-loop för att hålla programmet interaktivt tills användaren väljer att avsluta.
   
---

### 6. **Filbaserad textredigerare**
   - Skapa ett program som låter användaren skriva anteckningar och spara dem i en textfil. Använd tre moduler:
     - En för att skapa och skriva till filen.
     - En för att läsa från filen och visa innehållet.
     - En för att radera hela innehållet i filen.
   - Använd `with open()` för filhanteringen och låt användaren interagera med programmet via ett huvudprogram.



---

### 7. **Receptbok med modulär programmering**
   - Skapa en modul som hanterar att lägga till recept (titel, ingredienser, instruktioner).
   - En modul som söker efter ett recept baserat på titel.
   - En modul som listar alla sparade recept.
   - Huvudprogrammet ska fråga användaren vilken operation de vill utföra (lägga till, söka eller lista recept).



---

### 8. **Kontaktbok med filhantering**
   - Dela upp i moduler:
     - En modul för att lägga till nya kontakter (namn och telefonnummer) och spara dem i en fil.
     - En modul för att läsa och visa alla kontakter från filen.
     - En modul för att söka efter en specifik kontakt i filen.
   - Huvudprogrammet ska låta användaren välja vilken operation de vill utföra.
 
---

### 9. **Bibliotekssystem med flera filer**
   - Skapa ett enkelt bibliotekssystem som är uppdelat i flera moduler:
     - En modul för att lägga till böcker (titel och författare) i en lista.
     - En modul för att låna ut böcker och uppdatera listan över tillgängliga böcker.
     - En modul för att returnera böcker och uppdatera statusen för dessa.
   - Använd en huvudmodul som låter användaren hantera biblioteket.
  
