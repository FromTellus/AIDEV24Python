---
marp: true
paginate: true
theme: distansakademin
class: lead gaia
---

# Klasser och objekt i Python

---

## Agenda
- Grundläggande begrepp: Klasser och objekt
- Attribut och metoder
- Konstruktorer (`__init__`)
- Praktiska exempel och bästa praxis
- Introduktion till objektorienterad programmering (OOP)


---

## Vad är en klass?

En **klass** kan ses som en mall för att skapa objekt. Det är ett sätt att definiera en specifik datatyp och ge den vissa egenskaper (attribut) och beteenden (metoder).

- **Klasser** definierar:
  - Vilken data ett objekt ska ha (attribut).
  - Vilka funktioner objektet kan utföra (metoder).

---

**Exempel på en klass:**

    class Bil:
        def __init__(self, märke, modell, år):
            self.märke = märke
            self.modell = modell
            self.år = år

- Här definierar vi en klass `Bil` med tre attribut: `märke`, `modell` och `år`.
  
**Förklaring:**
- **`__init__`** är en speciell metod som kallas **konstruktor**. Den används för att initiera (eller ge värden till) objektets attribut när det skapas.

---
## Konstruktorn (`__init__`)

Konstruktorn är en speciell metod som körs när ett nytt objekt skapas. I Python heter konstruktorn alltid `__init__`. Det är här vi definierar de initiala värdena för objektets attribut.

- **Syntax för `__init__`:**
```
    class KlassNamn:
        def __init__(self, attribut1, attribut2):
            self.attribut1 = attribut1
            self.attribut2 = attribut2
```
- **`self`**: Det här argumentet refererar till det aktuella objektet som skapas och används för att tilldela värden till objektets attribut.

---


## Vad är ett objekt?

Ett **objekt** är en instans av en klass. Med andra ord, när du skapar ett objekt från en klass, blir det ett specifikt exempel av den klassen, med sina egna attributvärden.

- Om klassen är en ritning för en bil, så är ett objekt en faktisk bil, med ett specifikt märke, modell och årtal.

---

**Exempel på att skapa ett objekt:**

    class Bil:
        def __init__(self, märke, modell, år):
            self.märke = märke
            self.modell = modell
            self.år = år

    min_bil = Bil("Volvo", "XC60", 2020)
    print(min_bil.märke)  # Output: Volvo

- Här har vi skapat ett objekt `min_bil` av klassen `Bil` med specifika värden för attributen `märke`, `modell`, och `år`.

---

### Flera objekt från samma klass

Du kan skapa hur många objekt du vill från en och samma klass, och varje objekt kan ha olika värden för sina attribut.

---

**Exempel:**

    class Bil:
        def __init__(self, märke, modell, år):
            self.märke = märke
            self.modell = modell
            self.år = år

    bil1 = Bil("Volvo", "XC60", 2020)
    bil2 = Bil("Toyota", "Corolla", 2018)

    print(bil1.märke)  # Output: Volvo
    print(bil2.märke)  # Output: Toyota

- Båda objekten `bil1` och `bil2` är instanser av klassen `Bil`, men de har olika värden för sina attribut.

---

## Attribut i klasser

**Attribut** representerar egenskaper hos objektet. Dessa attribut kan vara olika typer av data, såsom strängar, tal, listor, eller andra datatyper.

---

**Exempel på attribut:**

    class Student:
        def __init__(self, namn, ålder, program):
            self.namn = namn
            self.ålder = ålder
            self.program = program

    student1 = Student("Rosie", 22, "Datalogi")
    student2 = Student("Bob", 24, "Elektroteknik")

    print(student1.namn)  # Output: Rosie
    print(student2.program)  # Output: Elektroteknik

---

### Olika typer av attribut

Attribut kan vara:
- **Instansattribut**: Definieras inuti konstruktorn och är unika för varje objekt. 
- **Klassattribut**: Delas mellan alla instanser av klassen. Definieras utanför konstruktorn.

---

**Exempel på klassattribut:**

    class Djur:
        antal_ben = 4  # Klassattribut

        def __init__(self, namn):
            self.namn = namn  # Instansattribut

    hund = Djur("Fido")
    katt = Djur("Whiskers")

    print(hund.antal_ben)  # Output: 4
    print(katt.antal_ben)  # Output: 4

- Alla objekt delar attributet `antal_ben`, medan `namn` är unikt för varje objekt.

---

## Metoder i klasser

**Metoder** är funktioner som definieras inuti klasser och utför åtgärder på objekt. Alla metoder måste ta emot objektet självt som första parameter, vilket representeras av `self`.

- **Instansmetoder**: Utför åtgärder på objektets instansdata (attribut).
- **Klassmetoder** och **statiska metoder**: Dessa skiljer sig från instansmetoder, men vi kommer att fokusera på instansmetoder här.

---

### Exempel på instansmetoder

    class Cykel:
        def __init__(self, färg, växlar):
            self.färg = färg
            self.växlar = växlar
        
        def cykla(self):
            print(f"Den {self.färg} cykeln med {self.växlar} växlar cyklar.")

    min_cykel = Cykel("blå", 7)
    min_cykel.cykla()  # Output: Den blå cykeln med 7 växlar cyklar.

- Här har vi en metod `cykla()` som använder objektets attribut för att utföra en åtgärd.

---

### Metoder som modifierar objekt attribut

Du kan också skapa metoder som modifierar objektets attribut.

---

**Exempel:**

    class Konto:
        def __init__(self, saldo):
            self.saldo = saldo
        
        def insättning(self, belopp):
            self.saldo += belopp
        
        def uttag(self, belopp):
            if belopp <= self.saldo:
                self.saldo -= belopp
            else:
                print("Otillräckligt saldo.")

    mitt_konto = Konto(1000)
    mitt_konto.insättning(500)
    print(mitt_konto.saldo)  # Output: 1500
    mitt_konto.uttag(2000)   # Output: Otillräckligt saldo.

---


## Sammanfattning

- **Klasser** är mallar för att skapa objekt.
- **Objekt** är instanser av klasser och har sina egna attribut och metoder.
- **Attribut** är data som är kopplade

---

# Objektorienterad programmering (OOP)

---

## Introduktion

Objektorienterad programmering (OOP) är ett av de mest använda programmeringsmönstren. OOP används för att organisera och strukturera kod genom att dela upp den i mindre enheter som representerar verkliga objekt eller abstrakta begrepp. Genom att använda **klasser** och **objekt** kan vi skapa en tydlig och logisk struktur som gör det enklare att arbeta med och vidareutveckla kod över tid.

I OOP representerar en klass en mall eller ett "blueprint" för att skapa objekt. Ett objekt är en instans av en klass och kan beskrivas som en konkret representation av ett verkligt eller abstrakt objekt med egenskaper (attribut) och beteenden (metoder). OOP används ofta för att modellera situationer och företeelser från verkligheten, vilket gör det lätt att skapa kod som är enkel att förstå och hantera.

---

### Vad är OOP?

- OOP står för **objektorienterad programmering**, där man bygger program genom att skapa och manipulera **objekt** baserade på **klasser**.
- Med klasser och objekt kan vi organisera vår kod så att den speglar den verklighet eller det system vi försöker modellera, vilket kan göra programmen mer intuitiva att arbeta med.
- OOP underlättar strukturering av program genom att bryta ner uppgifter i mindre, hanterbara enheter som kan utvecklas, testas och förstås separat.

OOP används ofta i system där vi hanterar många olika typer av data och komplexa relationer mellan dessa data. Det är särskilt effektivt för att bygga system där samma typ av objekt eller handlingar upprepas, och där vi behöver definiera gemensamma regler för hur dessa objekt ska bete sig.

---

### Varför använda OOP?

OOP erbjuder en rad fördelar som gör det till ett kraftfullt verktyg för att bygga och underhålla mjukvara. Här är några av de viktigaste fördelarna:

- **Modularitet**: Genom att använda klasser kan du dela upp din kod i mindre moduler som kan återanvändas och testas separat. Varje klass representerar en logisk enhet i ditt program och kan utvecklas oberoende av andra delar, vilket leder till mer strukturerad och underhållbar kod.
  
  - Exempel: En klass kan representera en specifik del av ett system, som en `Användare` i ett webbapplikationssystem. Varje användare har egna attribut (t.ex. namn, ålder) och beteenden (t.ex. logga in, logga ut). Genom att modulera din kod i sådana klasser blir programmet mer flexibelt och enkelt att vidareutveckla.

- **Enkelt att underhålla**: Eftersom klasser kan inkapsla data och logik inom sig själva, blir det enklare att göra ändringar i en del av programmet utan att påverka andra delar. Detta leder till färre fel när programmet växer och fler funktioner läggs till.
  
---

- **Lättare att förstå och utveckla**: OOP gör det möjligt att skriva kod som liknar hur vi tänker i verkligheten. Klasser representerar objekt eller enheter med egenskaper och beteenden, vilket gör koden mer läsbar och lättare att förstå. Andra utvecklare kan snabbt förstå en klass och dess objekt utan att behöva sätta sig in i hela programmet.
  
- **Återanvändbarhet**: Genom att använda klasser kan du återanvända kod i olika delar av ditt program eller till och med i olika projekt. Istället för att skriva om samma kod flera gånger kan du skapa klasser som kan återanvändas när liknande objekt eller funktionalitet behövs.
  
  - Exempel: En klass som `Produkt` kan användas för att representera produkter i en webbshop, och samma klass kan användas för flera typer av produkter, såsom böcker, kläder och elektronik. Du kan sedan utöka funktionaliteten genom att skapa nya subklasser för att hantera specifika produkttyper.

---

### Jämförelse med andra paradigmer

Det är viktigt att notera att även om OOP erbjuder stora fördelar, så är det inte den enda vägen till modularitet och återanvändbarhet. Andra programmeringsparadigm, som **funktionell programmering**, har sina egna metoder för att uppnå dessa mål genom att fokusera på ren funktionell logik och undvika tillståndsförändringar.

I OOP är fokuset på objekt och deras interaktioner, medan funktionell programmering mer handlar om att manipulera data genom rena funktioner utan sidoeffekter. Båda paradigmen kan användas beroende på vilken typ av system du bygger, och ibland kan de även kombineras för att dra nytta av fördelarna med båda tillvägagångssätten.

---

Sammanfattningsvis är OOP ett kraftfullt verktyg för att organisera och strukturera din kod på ett sätt som gör den lättare att förstå, återanvända och underhålla. Genom att modellera objekt från verkligheten eller abstrakta idéer kan du bygga system som är både flexibla och robusta.

---


## Uppgift 1: Skapa en Person-klass

Skapa en klass `Person` som har attributen `namn`, `ålder`, och `stad`. Definiera en metod som heter `hälsa` som skriver ut en hälsning med personens namn och stad.

### Krav:
- Använd `__init__` för att tilldela värden till attributen.
- Metoden `hälsa` ska skriva ut något i stil med: "Hej! Jag heter [namn] och bor i [stad]."

---

## Uppgift 2: Bankkonto

Skapa en klass `Bankkonto` som har ett attribut `saldo`. Implementera metoderna `insättning` och `uttag` för att lägga till och ta bort pengar från kontot.

### Krav:
- Metoden `insättning` tar emot ett belopp och lägger till det till `saldo`.
- Metoden `uttag` tar emot ett belopp och subtraherar det från `saldo`, men ska inte tillåta att kontot går under 0. Om beloppet är större än saldot, skriv ut ett meddelande som varnar om otillräckligt saldo.

---

## Uppgift 3: Biluthyrning

Skapa en klass `Bil` som representerar en bil i en biluthyrning. Varje bil har ett attribut `tillgänglig` som är True om bilen är tillgänglig och False om den är uthyrd. Skapa metoderna `hyr` och `lämna_tillbaka` för att hantera uthyrning.

### Krav:
- `hyr` ska ändra bilens tillstånd till "uthyrd" om den är tillgänglig, och skriva ut ett meddelande om bilen hyrs ut.
- `lämna_tillbaka` ska göra bilen tillgänglig igen.

---

## Uppgift 4: Studentens studier

Skapa en klass `Student` som har attributen `namn`, `ämnen` (en lista över ämnen studenten läser), och en metod `lägg_till_ämne` för att lägga till nya ämnen till listan.

### Krav:
- Skapa en metod som tar emot ett ämne och lägger till det i listan.
- Skapa en metod `visa_ämnen` som skriver ut alla ämnen studenten läser.

---

## Uppgift 5: Bokbibliotek

Skapa en klass `Bibliotek` som hanterar en samling av böcker. Varje bok ska representeras av en titel och en författare. Implementera en metod för att lägga till böcker och en metod för att visa alla böcker i biblioteket.

### Krav:
- Metoden `lägg_till_bok` ska ta emot en boktitel och en författare och lägga till dem i biblioteket.
- Metoden `visa_böcker` ska skriva ut alla böcker i biblioteket.

---

## Uppgift 6: Filmkatalog

Skapa en klass `Film` som representerar en film med attributen `titel`, `år`, och `regissör`. Skapa sedan en klass `Filmkatalog` som hanterar en lista av filmer. Implementera metoder för att lägga till en film och för att söka efter en film baserat på titel.

### Krav:
- Metoden `lägg_till_film` ska ta emot en film och lägga till den i katalogen.
- Metoden `sök_film` ska ta emot en titel och skriva ut information om filmen om den finns i katalogen.

---

## Uppgift 7: Köhantering

Skapa en klass `Kö` som simulerar en kö. Implementera metoderna `lägg_till_person` för att lägga till en person till kön och `betjäna_person` för att ta bort den första personen i kön och skriva ut deras namn.

### Krav:
- Metoden `lägg_till_person` ska lägga till en person till kön.
- Metoden `betjäna_person` ska skriva ut namnet på den person som betjänas och sedan ta bort personen från kön.
