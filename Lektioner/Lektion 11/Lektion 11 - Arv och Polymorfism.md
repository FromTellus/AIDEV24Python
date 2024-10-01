---
marp: true
paginate: true
theme: distansakademin
class: lead gaia
---

# Klasser och objekt i Python – Fortsättning

---

## Agenda

- Arv i Python
- **Polymorfism (utförlig förklaring)**
- Användning av `super()`
- Praktiska exempel
- Uppgifter att öva på

---

## Arv i Python

### Vad är arv?

- **Arv** låter oss skapa en ny klass som tar över egenskaper och metoder från en annan klass.
- Den nya klassen kallas **subklass** eller **barnklass**.
- Den klass vi ärver från kallas **superklass** eller **föräldraklass**.

### Varför använda arv?

- Återanvänd kod istället för att skriva om den.
- Skapa en struktur där liknande klasser kan grupperas.

---

### Hur använder vi arv?

- Vi anger superklassen inom parentes när vi definierar subklassen.

        class Djur:
            def __init__(self, namn):
                self.namn = namn

            def äta(self):
                print(f"{self.namn} äter.")

        class Hund(Djur):
            def skälla(self):
                print(f"{self.namn} skäller.")

- Här är `Hund` en subklass till `Djur` och får automatiskt attributet `namn` och metoden `äta`.

---

### Använda subklassen

    min_hund = Hund("Fido")
    min_hund.äta()     # Output: Fido äter.
    min_hund.skälla()  # Output: Fido skäller.

- `Hund` kan både äta (från `Djur`) och skälla (sin egen metod).
- Vi behöver inte använda `super()` här eftersom vi inte har definierat en egen `__init__`-metod i `Hund`.

---

## Polymorfism

### Vad är polymorfism?

- **Polymorfism** betyder "många former".
- Inom programmering innebär det att objekt av olika klasser kan behandlas på samma sätt genom en gemensam superklass.
- Det tillåter oss att använda samma metodnamn för att utföra liknande handlingar på olika objekt.

---

### Varför är polymorfism användbart?

- **Enhetlighet**: Vi kan skriva kod som fungerar med en superklass och vet att den kommer att fungera med alla dess subklasser.
- **Flexibilitet**: Lätt att utöka programmet genom att lägga till nya subklasser utan att ändra befintlig kod.
- **Läslighet**: Kod blir mer intuitiv och lättare att förstå.

---

### Exempel på polymorfism

    class Djur:
        def göra_ljud(self):
            print("Djuret gör ett ljud.")

    class Hund(Djur):
        def göra_ljud(self):
            print("Voff!")

    class Katt(Djur):
        def göra_ljud(self):
            print("Mjau!")

    class Ko(Djur):
        def göra_ljud(self):
            print("Muuu!")

    djur_lista = [Hund(), Katt(), Ko()]

    for djur in djur_lista:
        djur.göra_ljud()

    # Output:
    # Voff!
    # Mjau!
    # Muuu!

- Trots att objekten är av olika klasser kan vi anropa `göra_ljud()` på dem alla.

---

### Polymorfism med funktioner

    def låt_djuret_prata(djur):
        djur.göra_ljud()

    låt_djuret_prata(Hund())  # Output: Voff!
    låt_djuret_prata(Katt())  # Output: Mjau!

- Funktionen `låt_djuret_prata` behöver inte veta vilken typ av djur det är, bara att det kan `göra_ljud()`.

---

### Polymorfism med listor

    djur_lista = [Hund(), Katt(), Ko(), Djur()]

    for djur in djur_lista:
        djur.göra_ljud()

    # Output:
    # Voff!
    # Mjau!
    # Muuu!
    # Djuret gör ett ljud.

- Även om `Djur` inte är en subklass, kan det fortfarande användas i samma sammanhang.

---

### Överskuggning av metoder

- När en subklass definierar en metod med samma namn som i superklassen, överskuggar den superklassens metod.
- Detta är grunden för polymorfism; subklasser kan anpassa beteendet av metoder.

---

### Exempel: Enhetlig behandling av olika objekt

    class Form:
        def area(self):
            pass

    class Rektangel(Form):
        def __init__(self, inkommande_bredd, höjd):
            self.bredd = inkommande_bredd
            self.höjd = höjd

        def area(self):
            return self.bredd * self.höjd

    class Cirkel(Form):
        def __init__(self, radie):
            self.radie = radie

        def area(self):
            import math
            return math.pi * self.radie ** 2

    former = [Rektangel(3, 4), Cirkel(5)]

    for form in former:
        print(form.area())

    # Output:
    # 12
    # 78.53981633974483

- Båda formerna kan behandlas på samma sätt trots att de är olika typer.

---

### Viktiga punkter om polymorfism

- **Metodnamn**: Samma metodnamn används i olika klasser.
- **Olika implementationer**: Varje klass implementerar metoden på sitt eget sätt.
- **Gemensam superklass**: Klasserna ärver från samma superklass, vilket möjliggör enhetlig behandling.

---

## Användning av `super()`

### Varför använda `super()`?

- När vi behöver anropa metoder från superklassen inom vår subklass.
- Vanligt när vi har en egen `__init__`-metod i subklassen men vill behålla initialiseringen från superklassen.

---

### Exempel där vi behöver `super()`

    class Djur:
        def __init__(self, namn):
            self.namn = namn

    class Fågel(Djur):
        def __init__(self, namn, färg):
            super().__init__(namn)
            self.färg = färg

    min_fågel = Fågel("Tweety", "gul")
    print(min_fågel.namn)  # Output: Tweety
    print(min_fågel.färg)  # Output: gul

- Utan `super().__init__(namn)` skulle `namn` inte sättas korrekt.

---

### Använda `super()` i överskuggade metoder

    class Djur:
        def äta(self):
            print("Djuret äter.")

    class Katt(Djur):
        def äta(self):
            super().äta()
            print("Katten slickar sig om munnen.")

    min_katt = Katt()
    min_katt.äta()

    # Output:
    # Djuret äter.
    # Katten slickar sig om munnen.

- Vi anropar superklassens `äta` och lägger sedan till extra beteende.

---

## Praktiska exempel

### Exempel: Meddelandehantering

    class Meddelande:
        def skicka(self):
            print("Skickar meddelande...")

    class SMS(Meddelande):
        def skicka(self):
            print("Skickar SMS...")

    class Epost(Meddelande):
        def skicka(self):
            print("Skickar e-post...")

    meddelanden = [SMS(), Epost(), Meddelande()]

    for meddelande in meddelanden:
        meddelande.skicka()

    # Output:
    # Skickar SMS...
    # Skickar e-post...
    # Skickar meddelande...

- Alla meddelanden kan skickas, men sättet de skickas på varierar.

---

### Exempel: Betalningssystem

    class Betalning:
        def betala(self, belopp):
            print(f"Betalar {belopp} kr.")

    class Kortbetalning(Betalning):
        def betala(self, belopp):
            print(f"Betalar {belopp} kr med kort.")

    class SwishBetalning(Betalning):
        def betala(self, belopp):
            print(f"Betalar {belopp} kr med Swish.")

    betalningar = [Kortbetalning(), SwishBetalning(), Betalning()]

    for betalning in betalningar:
        betalning.betala(100)

    # Output:
    # Betalar 100 kr med kort.
    # Betalar 100 kr med Swish.
    # Betalar 100 kr.

- Samma metod `betala` används, men implementationen varierar.

---

# Klasser och objekt i Python – Fortsättning

---

## Uppgifter att öva på

### Uppgift 1: **Djurpark (Zoo) Hantering**

#### Beskrivning:

Du ska skapa ett program som modellerar olika djur i en djurpark. Varje djur har unika egenskaper och beteenden, men alla djur har vissa gemensamma attribut.

#### Instruktioner:

1. **Skapa en basklass `Djur`:**

   - Attribut:
     - `namn` (sträng)
     - `ålder` (heltal)
   - Metoder:
     - `ljud()` som inte gör något (använd `pass`).
     - `info()` som skriver ut djurets namn och ålder.

---

2. **Skapa subklasser som ärver från `Djur`:**

   - `Lejon`
     - Attribut:
       - `manens_storlek` (sträng)
     - Metoder:
       - Implementera `ljud()` som skriver ut "Lejonet ryter!"
---
   - `Elefant`
     - Attribut:
       - `betarnas_längd` (i meter)
     - Metoder:
       - Implementera `ljud()` som skriver ut "Elefanten trumpetar!"
   - `Apa`
     - Attribut:
       - `art` (sträng, t.ex. "Schimpans")
     - Metoder:
       - Implementera `ljud()` som skriver ut "Apan skriker!"

---

3. **Användning av `super()`:**

   - I varje subklass, använd `super().__init__(namn, ålder)` för att initiera gemensamma attribut.

---

4. **Testa dina klasser:**

   - Skapa objekt för varje djur med olika attributvärden.
   - Anropa metoderna `info()` och `ljud()` för varje djur och kontrollera att rätt information och ljud skrivs ut.

#### Tips:

- **Användning av `super()`:** Kom ihåg att anropa superklassens `__init__` innan du lägger till subklassens egna attribut.
- **Polymorfism:** Eftersom alla djur har metoden `ljud()`, kan du skapa en lista med djurobjekt och iterera över den för att anropa `ljud()` på varje djur.

---

### Uppgift 2: **Musikspelare**

#### Beskrivning:

Du ska skapa ett program som hanterar olika typer av musikspelare och deras funktioner. Detta hjälper dig att öva på arv, polymorfism och användning av `super()`.

#### Instruktioner:

1. **Skapa en basklass `Musikspelare`:**

   - Attribut:
     - `märke` (sträng)
   - Metoder:
     - `spela_musik()` som inte gör något (använd `pass`).

---

2. **Skapa subklasser som ärver från `Musikspelare`:**

   - `CDSpelare`
     - Attribut:
       - `antal_skivor` (heltal)
     - Metoder:
       - Implementera `spela_musik()` som skriver ut ett meddelande om att spela musik från CD-skivor.

---

   - `MP3Spelare`
     - Attribut:
       - `minne` (i GB)
     - Metoder:
       - Implementera `spela_musik()` som skriver ut ett meddelande om att spela musik från digitala filer.
   - `Radio`
     - Attribut:
       - `frekvens` (tal)
     - Metoder:
       - Implementera `spela_musik()` som skriver ut ett meddelande om att spela musik från en radiokanal.

---

3. **Användning av `super()`:**

   - I varje subklass, använd `super().__init__(märke)` för att initiera attributet `märke`.

4. **Testa dina klasser:**

   - Skapa objekt för varje musikspelare med olika attributvärden.
   - Anropa metoden `spela_musik()` för varje objekt och kontrollera att rätt meddelande skrivs ut.

---

#### Tips:

- **Användning av `super()`:** Kom ihåg att anropa superklassens `__init__` innan du lägger till subklassens egna attribut.
- **Polymorfism:** Eftersom alla musikspelare har metoden `spela_musik()`, kan du skapa en lista med musikspelarobjekt och iterera över den för att anropa `spela_musik()` på varje spelare.

---

### Uppgift 3: **Anställda och arbetstid**

#### Beskrivning:

Du ska skapa ett system för att beräkna löner för anställda, där olika anställningstyper har olika sätt att beräkna lön.

#### Instruktioner:

1. **Skapa en basklass `Anstalld`:**

   - Attribut:
     - `namn` (sträng)
     - `timlon` (tal)
   - Metod:
     - `berakna_lon(timmar)` som beräknar lönen baserat på arbetade timmar (`timlon * timmar`).

---

2. **Skapa subklasser som ärver från `Anstalld`:**

   - `Heltid`
     - Attribut:
       - `manadslon` (tal)
     - Metod:
       - Överskugga `berakna_lon(timmar)` så att den returnerar `manadslon`, oavsett antal timmar.
   - `Deltid`
     - Använder superklassens `berakna_lon(timmar)` utan ändringar.

---

3. **Användning av `super()`:**

   - I `Heltid`, använd `super().__init__(namn, timlon=0)` om du behöver initiera attribut från basklassen.

4. **Testa dina klasser:**

   - Skapa objekt för både heltids- och deltidsanställda.
   - Anropa `berakna_lon()` och kontrollera att lönen beräknas korrekt för båda typerna.

---

#### Tips:

- **Överskuggning av metoder:** I `Heltid` behöver du anpassa metoden `berakna_lon` för att passa månadslön.
- **Användning av `super()`:** Använd det för att initiera gemensamma attribut i basklassen.
- **Exempel på beräkning:**

  - Heltid: lönen är alltid `manadslon`.
  - Deltid: lönen är `timlon * timmar`.

---

### Uppgift 4: **Köhantering i en Butik**

#### Beskrivning:

Du ska skapa ett program för att hantera olika typer av kunder i en butikskö. Kunder kan vara vanliga kunder, medlemmar eller VIP-kunder, och de har olika prioritet i kön.

#### Instruktioner:

1. **Skapa en basklass `Kund`:**

   - Attribut:
     - `namn` (sträng)
   - Metod:
     - `get_prioritet()` som returnerar en siffra för kundens prioritet (standardvärde 3).

---

2. **Skapa subklasser som ärver från `Kund`:**

   - `Medlem`
     - Överskugga `get_prioritet()` så att den returnerar en högre prioritet (t.ex. 2).
   - `VIPKund`
     - Överskugga `get_prioritet()` så att den returnerar högsta prioritet (t.ex. 1).

3. **Hantera kön:**

   - Skapa en lista med olika kundobjekt (blandning av `Kund`, `Medlem`, `VIPKund`).
   - Sortera kön baserat på kundernas prioritet (högre prioritet går före i kön).
   - Skriv ut kundernas namn i ordning baserat på prioritet.

---

4. **Testa ditt program:**

   - Lägg till flera kunder av olika typer i kön.
   - Kontrollera att sorteringen fungerar korrekt och att kunderna betjänas i rätt ordning.

#### Tips:

- **Användning av `sort()` eller `sorted()`:** Du kan sortera listan genom att använda kundens prioritet som nyckel.
- **Utöka funktionaliteten (valfritt):** Lägg till fler attribut eller metoder, t.ex. tid i kön eller medlemsnummer.

---

### Uppgift 5: **Mat och dryck**

#### Beskrivning:

Du ska skapa ett program som hanterar produkter i en butik, med särskild hantering för mat och dryck.

#### Instruktioner:

1. **Skapa en basklass `Produkt`:**

   - Attribut:
     - `namn` (sträng)
     - `pris` (tal)
   - Använd `__init__` för att initiera attributen.

---

2. **Skapa subklasser som ärver från `Produkt`:**

   - `Mat`
     - Lägg till attributet `utgangsdatum` (sträng, t.ex. "2023-12-31").
   - `Dryck`
     - Lägg till attributet `volym` (sträng, t.ex. "1 liter").

3. **Användning av `super()`:**

   - I både `Mat` och `Dryck`, anropa `super().__init__(namn, pris)` för att initiera gemensamma attribut.

---

4. **Testa dina klasser:**

   - Skapa objekt för både mat och dryck.
   - Skriv ut information om produkterna, inklusive deras specifika attribut.

#### Tips:

- **Initiering av subklasser:** Kom ihåg att först anropa superklassens `__init__` innan du lägger till nya attribut.
- **Exempel på objektinstansering:**

  - Mat: `brod = Mat("Bröd", 25, "2023-12-31")`
  - Dryck: `mjolk = Dryck("Mjölk", 15, "1 liter")`

---

### Uppgift 6: **Biblioteksböcker**

#### Beskrivning:

Du ska skapa ett system för att hantera utlåning av böcker på ett bibliotek.

#### Instruktioner:

1. **Skapa en klass `Bok`:**

   - Attribut:
     - `titel` (sträng)
     - `forfattare` (sträng)
   - Använd `__init__` för att initiera attributen.

---

2. **Skapa en subklass `Lanebok` som ärver från `Bok`:**

   - Lägg till attributet `lantagare`, som initialt är `None`.

3. **Användning av `super()`:**

   - Anropa `super().__init__(titel, forfattare)` i `Lanebok`.

---

4. **Skapa metoder i `Lanebok`:**

   - `lana_ut(lantagare)`: Sätter `lantagare` om boken inte redan är utlånad, annars informerar om att boken är upptagen.
   - `aterlamna()`: Återställer `lantagare` till `None` och bekräftar att boken är återlämnad.

5. **Testa dina klasser:**

   - Skapa ett `Lanebok`-objekt.
   - Låna ut och återlämna boken, och kontrollera att status uppdateras korrekt.

---

#### Tips:

- **Hantering av tillstånd:** Kontrollera om `lantagare` är `None` för att avgöra om boken är utlånad eller inte.
- **Exempel på användning:**

  - `bok = Lanebok("1984", "George Orwell")`
  - `bok.lana_ut("Emma")`
  - `bok.aterlamna()`

---

### Uppgift 7: **Fordon**

#### Beskrivning:

Du ska modellera olika fordon och hur de framförs, med fokus på att använda polymorfism.

#### Instruktioner:

1. **Skapa en basklass `Fordon`:**

   - Attribut:
     - `hastighet` (tal)
   - Använd `__init__` för att initiera attributet.
   - Definiera en metod `framfor()` som inte gör något (använd `pass`).

---

2. **Skapa subklasser som ärver från `Fordon`:**

   - `Bil`
     - Implementera `framfor()` som skriver ut hur fort bilen kör på vägen.
   - `Cykel`
     - Implementera `framfor()` som skriver ut hur fort cykeln rullar på cykelbanan.
   - `Tag` (tåg)
     - Implementera `framfor()` som skriver ut hur fort tåget kör på rälsen.

---

3. **Användning av polymorfism:**

   - Skapa en lista med olika fordonsobjekt.
   - Iterera genom listan och anropa `framfor()` på varje objekt.

4. **Testa dina klasser:**

   - Se till att rätt meddelande skrivs ut för varje fordon.

---

#### Tips:

- **Användning av polymorfism:** Eftersom alla fordon har metoden `framfor()`, kan du behandla dem på samma sätt i din kod.
- **Exempel på lista:**

  - `fordon_lista = [Bil(100), Cykel(20), Tag(150)]`

---

# Lycka till med programmeringen!
