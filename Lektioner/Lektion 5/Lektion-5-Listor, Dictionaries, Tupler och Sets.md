---
marp: true
paginate: true
theme: distansakademin
class: lead gaia
---

# Listor, Dictionaries, Tupler och Sets i Python

---

## Agenda
    - Listor
    - Dictionaries
    - Tupler
    - Sets
    - List comprehensions och motsvarigheter.
---

## Inledning

I Python används flera olika datatyper för att strukturera och organisera information. Dessa datatyper har unika egenskaper, och hur de kan interagera med varandra är viktigt att förstå för att skapa flexibla och effektiva program. I den här föreläsningen kommer vi att gå igenom fyra viktiga datatyper: listor, dictionaries, tupler och sets. Vi kommer också att utforska hur dessa typer kan användas tillsammans, vilka begränsningar som finns, samt några best practices kring hur man nestar dessa datatyper.

---

## Listor i Python

### Vad är en Lista?

En lista i Python är en ordnad samling där du kan spara flera objekt, och dessa objekt kan vara av vilken datatyp som helst. Listor är **mutabla**, vilket betyder att du kan ändra innehållet efter att listan har skapats.

---

### Skapa och Modifiera Listor
```
min_lista = [1, 2, 3, 4]  
min_lista_via_function = list([1, 2, 3, 4])
```
- Listor skapas med hakparenteser `[]` och elementen separeras med kommatecken. 
- Listor kan även skapas med `list()`-funktionen som tar en iterable som argument.

---

### Exempel på Listor
```
min_lista = [1, "hej", 3.5, [1, 2, 3]]
```
Här ser vi att listan kan innehålla heltal, strängar, flyttal och till och med andra listor. Denna flexibilitet gör listor användbara för att hantera olika typer av data i en och samma samling.

---

### Vanliga Funktioner och Metoder för Listor

- **append()**: Lägger till ett element i slutet av listan.
```
  min_lista.append(5)  # Lägger till talet 5 i listan
```
- **remove()**: Tar bort den första förekomsten av ett specifikt element.
```
  min_lista.remove(3.5)  # Tar bort elementet 3.5
```
- **sort()**: Sorterar listan i stigande ordning (förutsatt att alla element kan jämföras).
```
  sorterad_lista = [3, 1, 4]
  sorterad_lista.sort()  # Resultat: [1, 3, 4]
```
---

### Användning av For-loopar med Listor

Listor kan itereras över med en for-loop:
```
min_lista = [1,2,3,4]
for element in min_lista:
    print(element)
```
I detta exempel kommer varje element i listan att skrivas ut i tur och ordning.

---

## Dictionaries i Python

### Vad är en Dictionary?

En dictionary i Python lagrar data i form av **nyckel-värde-par**. Nyckeln måste vara en oföränderlig datatyp (som en sträng eller tuple), medan värdet kan vara vilken datatyp som helst.

- **Viktigt:** Dictionaries skapas med måsvingar `{}`, men de kan också skapas med funktionen `dict()`.

---

### Skapa och Modifiera Dictionaries
```
person = {"namn": "Anna", "ålder": 30}  
person_via_function = dict(namn="Anna", ålder=30)
```
- Nycklar och värden separeras med ett kolon, och varje par separeras med kommatecken.
- Dictionaries kan även skapas med `dict()`-funktionen.

---

### Exempel på Dictionaries med en lista
```
person = {"namn": "Anna", "intressen": ["läsa", "resa"], "adress": {"stad": "Stockholm", "land": "Sverige"}}
```
Här lagrar vi en lista som ett värde under nyckeln "intressen", och en annan dictionary under "adress". Detta är användbart för att skapa komplexa datastrukturer.

---

### Vanliga Funktioner och Metoder för Dictionaries

- **keys()**: Returnerar en lista över alla nycklar i dictionaryn.
```
  print(person.keys())  # Output: dict_keys(['namn', 'intressen', 'adress'])
```
- **values()**: Returnerar en lista över alla värden.
```
  print(person.values())  # Output: dict_values(['Anna', ['läsa', 'resa'], {'stad': 'Stockholm', 'land': 'Sverige'}])
```
- **items()**: Returnerar en lista över alla nyckel-värde-par som tupler.
```
  print(person.items())  # Output: dict_items([('namn', 'Anna'), ('intressen', ['läsa', 'resa']), ('adress', {'stad': 'Stockholm', 'land': 'Sverige'})])
```
---

### Användning av For-loopar med Dictionaries

Du kan använda en for-loop för att iterera över nycklar, värden eller både och:

#### Iterera över nycklar:
```
for key in person.keys():
    print(key)
```
#### Iterera över värden:
```
for value in person.values():
    print(value)
```

---

#### Iterera över både nycklar och värden:
```
for key, value in person.items():
    print(f"{key}: {value}")
```
---

## Tupler i Python

### Vad är en Tuple?

En tuple är en **oföränderlig** sekvens av element. Detta innebär att när en tuple har skapats, kan du inte ändra dess innehåll. Tupler används ofta för att representera fasta dataset.

---

### Skapa och Modifiera Tupler
```
min_tuple = (1, 2, 3)  
min_tuple_via_function = tuple([1, 2, 3])
```
- Tupler skapas med parenteser `()` och kan också skapas med `tuple()`-funktionen.
- Tupler kan inte ändras, men om en tuple innehåller mutabla objekt, som listor, kan listans innehåll fortfarande ändras.

---

### Exempel på Tupler

```
min_tuple = (1, [2, 3], "text")
```
Här ser vi att tuplen innehåller en lista som ett av dess element. Även om tuplen inte kan ändras direkt, kan vi fortfarande modifiera innehållet i listan.
```
min_tuple[1].append(4)  # Resultat: (1, [2, 3, 4], "text")
```
---

### Användning av For-loopar med Tupler

Tupler kan också itereras över med en for-loop precis som listor:
```
for element in min_tuple:
    print(element)
```
---

## Sets i Python

### Vad är ett Set?

Ett set är en **oordnad** samling av **unika** element. Sets är användbara när du vill lagra värden som inte ska dupliceras, och de är mutabla, men alla element i ett set måste vara oföränderliga.

- **Viktigt**: Sets skapas med måsvingar `{}`, men de kan också skapas med `set()`-funktionen.

---

### Skapa och Modifiera Sets
```
mitt_set = {1, 2, 3, 4}  
mitt_set_via_function = set([1, 2, 3, 4])
```
- Sets skapas med måsvingar `{}` och kan också skapas med `set()`-funktionen.
- Sets kan inte innehålla duplicerade element.

---

### Exempel på Sets
```
mitt_set = {1, 2, 3, 3, 4}
```
Setet innehåller bara unika värden, så duplicerade värden som 3 tas bort.
```
print(mitt_set)  # Output: {1, 2, 3, 4}
```
---

### Användning av For-loopar med Sets

Eftersom sets är oordnade, kan du iterera över ett set med en for-loop, men ordningen på elementen är inte garanterad:
```
for element in mitt_set:
    print(element)
```
---



### List Comprehensions och motsvarigheter för andra datatyper

**Comprehensions** i Python är ett sätt att skapa nya samlingar som listor, dictionaries och sets på ett kompakt och lättläst sätt. Istället för att använda flera rader med for-loopar kan du skapa en ny samling på en enda rad.

---

#### List Comprehensions
En **list comprehension** är ett sätt att skapa en ny lista genom att applicera en operation eller ett villkor på varje element i en befintlig lista eller annan iterable. Syntaxen är:

Exempel:
Om vi har en lista med namn och vill skapa en ny lista som innehåller namnen i versaler, kan vi göra så här:
```

namn = ["Anna", "Erik", "Sara"]

versaler = [namn.upper() for namn in namn]

Resultat: ["ANNA", "ERIK", "SARA"]

```
---

Du kan också lägga till villkor (if-satser) för att filtrera elementen:

```

namn = ["Anna", "Erik", "Sara", "Eva"]

korta_namn = [namn for namn in namn if len(namn) <= 4]

Resultat: ["Anna", "Erik", "Eva"]

```
---


#### Dictionary Comprehensions
På samma sätt kan vi använda comprehensions för dictionaries. Syntaxen är:

---


Exempel:
Om vi har en lista med namn och vill skapa en dictionary där nyckeln är namnet och värdet är längden på namnet:

```
namn = ["Anna", "Erik", "Sara"]

namn_dict = {namn: len(namn) for namn in namn}

Resultat: {"Anna": 4, "Erik": 4, "Sara": 4}

```

---

Man kan även arbeta med både nycklar och värden i en dictionary comprehension. Exempelvis om vi har en dictionary med varor och deras priser, och vi vill skapa en ny dictionary med 10% rabatt på varje vara:

```
varor = {"mjölk": 20, "bröd": 25, "smör": 40}

rabatt_varor = {vara: pris * 0.9 for vara, pris in varor.items()}

Resultat: {"mjölk": 18.0, "bröd": 22.5, "smör": 36.0}
```
---

#### Set Comprehensions
Ett set comprehension liknar list och dictionary comprehensions men skapar ett set, som bara innehåller unika värden. Syntaxen är:


Exempel:
Om vi har en lista med siffror och vill skapa ett set som innehåller kvadraten av varje tal, kan vi göra så här:

```
siffror = [1, 2, 2, 3, 4]

kvadrater = {siffra ** 2 for siffra in siffror}

Resultat: {1, 4, 9, 16}

```
Eftersom sets bara innehåller unika värden, kommer det inte att finnas några dubbletter i resultatet, även om listan innehåller dem.

---

#### Tuple Comprehensions
För tupler finns det ingen direkt **tuple comprehension** i Python, men du kan använda en generator comprehension som skapar en generator, vilket i praktiken fungerar på liknande sätt för att iterera över elementen:



Exempel:

```
namn = ["Anna", "Erik", "Sara"]

namn_tuple = tuple(namn.upper() for namn in namn)

```
Resultat: ("ANNA", "ERIK", "SARA")

Comprehensions hjälper till att skriva kortare, mer effektiv och lättläst kod när du arbetar med listor, dictionaries, sets eller till och med generatorer.

---
## Sammanfattning

Vi har nu gått igenom hur listor, dictionaries, tupler och sets fungerar i Python. Dessa datatyper är mycket kraftfulla och flexibla, men de har också sina begränsningar. Genom att förstå hur de interagerar med varandra och använda rätt funktioner för rätt uppgifter, kan vi skapa effektiv och skalbar kod.

- **Listor** är flexibla och kan innehålla alla typer av data.
- **Dictionaries** organiserar data i nyckel-värde-par.
- **Tupler** är oföränderliga och används för fasta dataset.
- **Sets** säkerställer unika element och stöder mängdoperationer som union och intersektion.

---

### Uppgift 1: **Grundläggande Dictionaries – Hantera Elevers Information**

1. Skapa en tom dictionary.
2. Låt användaren mata in namn och ålder för tre elever.
3. Lägg till varje elev och deras ålder i dictionaryn.
4. Skriv ut alla elever och deras åldrar.

---

### Uppgift 2: **Tupler – Koordinater för Städer**

1. Skapa en tuple som innehåller tre element: namn på en stad, latitud, och longitud.
2. Skriv ut informationen om staden.
3. Be användaren skapa tre tupler för tre olika städer och skriv ut dem.

---

### Uppgift 3: **Grundläggande Sets – Unika Färger**

1. Skapa två sets, ett med färger från användaren och ett med fördefinierade färger (t.ex. {"röd", "grön", "blå"}).
2. Visa alla unika färger för båda setsen genom att kombinera båda setsen (använd union-metoden).
3. Visa de färger som finns i båda setsen (intersection).

---

### Uppgift 4: **Dictionary med Kontrollstrukturer – Födelsedagsbok**

1. Skapa en tom dictionary där nycklar är personnamn och värden är deras födelsedatum.
2. Låt användaren mata in namn och födelsedatum för tre personer.
3. Skriv ut alla personer och deras födelsedatum.
4. Låt användaren mata in ett namn och kontrollera om personen finns i dictionaryn. Om de finns, skriv ut deras födelsedatum.

---

### Uppgift 5: **Tupler – Koordinater för Platser**

1. Skapa en tuple som representerar latitud och longitud för en plats.
2. Skriv ut informationen om platsen.
3. Skapa en lista med tre tupler som representerar koordinaterna för tre olika platser (t.ex., städer eller intressanta platser).
4. Iterera över listan och skriv ut informationen om varje plats.



---

### Uppgift 6: **Sets – Fritidsintressen**

1. Skapa två sets, ett med fritidsintressen för två personer.
2. Använd en for-loop för att skriva ut alla intressen för varje person.
3. Använd union och intersection för att visa unika och gemensamma intressen.

---

### Uppgift 7: **Dictionary med Flera Nyckel-Värde-Par – Bokhylla**

1. Skapa en dictionary där nycklar är bokkategorier och värden är listor av böcker.
2. Låt användaren mata in böcker i olika kategorier.
3. Skriv ut alla böcker i en specifik kategori baserat på användarens val.

---

### Uppgift 8: **Kontrollstrukturer och Dictionaries – Produktfiltrering**

1. Skapa en dictionary där nycklar är produktnamn och värden är priser.
2. Låt användaren mata in produkter och deras priser.
3. Be användaren mata in ett maxpris och använd en for-loop och if-sats för att visa alla produkter som kostar mindre än maxpriset.

---

### Uppgift 9: **Kombinera Tupler och Dictionaries – Personregister**

1. Skapa en dictionary där varje nyckel är en persons namn och värdet är en tuple med ålder och stad.
2. Låt användaren mata in information om tre personer.
3. Skriv ut alla personer och deras information.
4. Använd en for-loop för att skriva ut namnen på personer som är äldre än 30 år.
