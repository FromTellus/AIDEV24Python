---
marp: true
paginate: true
theme: distansakademin
class: lead gaia
---

# Abstraktion och Inkapsling

---

## Agenda

- Vad är inkapsling?
- Vad är abstraktion?
- Hur skiljer sig dessa koncept?
- Getters och Setters i Python
- Mobbprogrammering
- Praktiska övningar

---

## Vad är Inkapsling?

**Inkapsling** innebär att vi skyddar objektets data och funktionalitet genom att dölja vissa delar och begränsa åtkomst från utsidan. Detta hjälper till att säkerställa att ett objekt inte manipuleras på ett oväntat sätt.

- **Syfte:** Skydda data och säkerställa att objektet används på ett korrekt sätt.

---

### Inkapsling i Python

I Python använder vi **publika**, **skyddade** och **privata** attribut för att hantera åtkomst till objektets data:

- **Publika attribut/metoder:** Kan nås från utsidan och anges utan något särskilt tecken.
- **Skyddade attribut/metoder:** Börjar med `_`, och det rekommenderas att dessa inte nås utanför klassen.
- **Privata attribut/metoder:** Börjar med `__`, och dessa kan inte nås direkt utanför klassen.

---

### Exempel på inkapsling

    class Bil:
        def __init__(self, märke, modell):
            self.__märke = märke  # Privat attribut
            self.__modell = modell

I detta exempel är attributen `__märke` och `__modell` privata och kan inte nås direkt från utsidan. Detta skyddar objektets data från otillåten manipulation.

---

## Vad är Abstraktion?

**Abstraktion** handlar om att dölja komplexiteten och endast visa den viktiga informationen. Abstraktionen fokuserar på **vad** ett objekt gör, inte **hur** det gör det.

- **Exempel i vardagen:** Du använder bilens ratten och pedaler utan att behöva veta exakt hur motorn eller växellådan fungerar.

Vi använder abstraktion genom att dölja detaljer och erbjuda ett förenklat gränssnitt till användaren via klasser och metoder.

---

### Exempel på abstraktion

    class Bil:
        def __init__(self, märke, modell):
            self.__märke = märke  # Privat attribut
            self.__modell = modell

        def starta_motorn(self):
            print(f"{self.__märke} {self.__modell} motorn har startat.")

        def stanna_motorn(self):
            print(f"{self.__märke} {self.__modell} motorn har stannat.")

Användaren av klassen bryr sig inte om hur bilen startar eller stannar. Det enda de behöver veta är att de kan använda metoderna `starta_motorn()` och `stanna_motorn()`.

---

## Inkapsling vs Abstraktion

### Vad är skillnaden?

- **Inkapsling:** Handlar om att skydda objektets interna data och förhindra direkt åtkomst till dessa.
- **Abstraktion:** Handlar om att dölja komplexiteten och bara visa användaren de relevanta funktionerna.

### Hur förhåller sig dessa till varandra?

- **Inkapsling** hjälper till att stödja **abstraktion** genom att kontrollera hur användaren interagerar med objektets data.
- Abstraktion är möjligt utan fullständig inkapsling, men inkapsling gör abstraktionen mer effektiv och säker.

---

    class Bankkonto:
        def __init__(self, innehavare, saldo):
            self.__innehavare = innehavare  # Privat attribut
            self.__saldo = saldo # Privat attribut

        def insättning(self, belopp):
            if belopp > 0:
                self.__saldo += belopp
                print(f"{belopp} kr har satts in på kontot.")
            else:
                print("Beloppet måste vara positivt.")
    
    konto = Bankkonto("Anna", 1000)
    konto.__saldo += 500 # Kommer inte fungera

- **Inkapsling:** Attributen `__innehavare` och `__saldo` är privata och kan inte ändras direkt från utsidan.
- **Abstraktion:** Användaren ser bara metoden `insättning()` för att interagera med kontot utan att behöva veta hur saldot uppdateras internt.

---

## Getters och Setters i Python

I Python använder vi **getters** och **setters** för att hantera åtkomst och modifiering av privata attribut i en klass. Detta gör att vi kan kontrollera hur värden hämtas och uppdateras och tillför validering om det behövs.

### Varför använda getters och setters?

- **Getter**: En metod som används för att hämta värdet av ett privat attribut.
- **Setter**: En metod som används för att ändra värdet på ett privat attribut och samtidigt kontrollera att den nya datan är korrekt.

---

### Exempel på getters och setters

    class Bil:  
        def __init__(self, märke, modell):  
            self.__märke = märke  
            self.__modell = modell  

        # Getter för att hämta värdet av märke  
        def get_märke(self):  
            return self.__märke  

        # Setter för att ändra värdet av märke  
        def set_märke(self, nytt_märke):  
            if isinstance(nytt_märke, str):  
                self.__märke = nytt_märke  
            else:  
                print("Fel: Märket måste vara en sträng.")


---

## Mobbprogrammering

### Vad är mobbprogrammering?

**Mobbprogrammering** är en utvecklingsmetod där ett helt team samarbetar på en och samma uppgift, på en och samma dator. I stället för att en eller två personer arbetar med kodningen, deltar hela gruppen aktivt genom att diskutera lösningar, föreslå idéer och navigera tillsammans.

---

### Hur fungerar det?

I mobbprogrammering arbetar teamet i **roller** som roteras med jämna mellanrum. De två vanligaste rollerna är:

- **Föraren:** Den person som faktiskt skriver koden. Förarens roll är att ta emot instruktioner från resten av teamet och implementera deras idéer.
- **Navigatörerna:** Resten av teamet fungerar som navigatörer, och deras uppgift är att övervaka och guida föraren, föreslå förbättringar, samt lösa eventuella problem som dyker upp.

Efter en viss tid, vanligtvis 10-15 minuter, roterar rollerna så att en ny person blir förare, och cykeln upprepas.

---

### Fördelar med mobbprogrammering

1. **Ökad kvalitet och färre buggar:**
   Eftersom hela teamet granskar koden och ger förslag i realtid, fångas potentiella buggar och fel snabbt. Detta leder till högre kodkvalitet.

2. **Snabbare lärande:**
   Eftersom alla deltar och får insikt i hur olika delar av systemet fungerar, kan teammedlemmar lära sig av varandra i realtid. Det är särskilt värdefullt för nyare utvecklare som kan lära sig från mer erfarna kollegor.


3. **Bättre teamkommunikation:**
   Mobbprogrammering uppmuntrar konstant kommunikation och samarbete. Alla idéer diskuteras och övervägs, vilket stärker teamets sammanhållning och samarbete.

4. **Delad äganderätt av koden:**
   Eftersom alla bidrar till varje del av koden, finns det inte längre en ensam "expert" på en viss del av systemet. Detta gör det lättare för teamet att fortsätta utveckla och underhålla systemet om någon är frånvarande.

---

### Nackdelar med mobbprogrammering

1. **Tid och resurskrävande:**
   Det kan verka ineffektivt att ha hela teamet fokuserat på en uppgift när flera mindre uppgifter skulle kunna lösas parallellt. Men långsiktigt kan den ökade kvaliteten och snabbare problemlösningen ofta uppväga detta.

2. **Kan vara mentalt utmattande:**
   Eftersom mobbprogrammering kräver konstant uppmärksamhet och samarbete, kan det vara mentalt krävande under längre sessioner.

---

### När ska man använda mobbprogrammering?

Mobbprogrammering passar särskilt bra när:

- Teamet står inför komplexa eller kritiska problem som kräver fler perspektiv.
- Det finns nya teammedlemmar som behöver onboardas snabbt.
- Det handlar om stora arkitektoniska beslut eller kodförändringar som påverkar hela projektet.

---

### Tips för effektiv mobbprogrammering

1. **Roterande roller:** Se till att rotera rollerna regelbundet så att alla får möjlighet att vara både förare och navigatör.
2. **Tidsboxning:** Använd en timer för att hålla rotationerna på 10-15 minuter. Detta hjälper till att hålla tempot uppe och säkerställer att alla får delta aktivt.
3. **Vara öppen för andras idéer:** Det är viktigt att teamet har en öppen diskussionskultur där alla känner sig bekväma att dela sina tankar och idéer.
4. **Håll pauser:** Eftersom mobbprogrammering kan vara intensivt, se till att ta regelbundna pauser för att hålla teamet fräscht och fokuserat.

---

### Sammanfattning

Mobbprogrammering är en kraftfull teknik som förbättrar kvalitet, lärande och teamkommunikation genom att arbeta tillsammans på en gemensam uppgift. Det kräver disciplin och samarbetsvilja, men fördelarna i form av högre kodkvalitet och snabbare problemlösning kan vara mycket värdefulla för ett team.


---

## Uppgift: Skapa en Krigare och ett Vapen

### Steg 1: Skapa klasserna `Krigare` och `Vapen`

---

#### Instruktioner:

1. **Skapa en klass `Vapen`:**
   - Skapa en konstruktor som tar två parametrar: `namn` (namnet på vapnet, t.ex. "Svärd") och `skada` (hur mycket skada vapnet orsakar, t.ex. 20). Dessa värden ska sparas som privata attribut.
   - Implementera metoder för att:
     - Hämta vapnets namn.
     - Hämta vapnets skada.

---

2. **Skapa en klass `Krigare`:**
   - Skapa en konstruktor som tar `namn` (krigarens namn) och sätter `hälsa` till ett standardvärde på 100. Dessa värden ska också sparas som privata attribut.
   - Krigaren ska även ha ett vapen, men i början är detta satt till `None`.
   - Implementera metoder för att:
     - Tilldela ett vapen till krigaren (genom en metod där vapnet skickas in som parameter).
     - Visa en text när krigaren använder sitt vapen (t.ex. "Thor använder Svärd").

---

#### Exempel på användning:

    krigare = Krigare("Thor")  
    vapen = Vapen("Svärd", 20)  
    krigare.lägg_till_vapen(vapen)  
    krigare.använd_vapen()  # Output: Thor använder Svärd  

---

### Steg 2: Lägg till skada och hälsa

#### Instruktioner:

1. **Utöka klassen `Krigare`:**
   - Lägg till en metod `ta_skada(skada)` där krigarens hälsa minskas när hen blir attackerad. Detta ska ske genom att dra av skadan från krigarens hälsa.
   - Lägg också till validering för att hälsan aldrig blir negativ.
   - Lägg till en metod `är_vid_liv()` som returnerar `True` om krigarens hälsa är över 0, och `False` annars. Detta låter oss kontrollera om krigaren fortfarande är vid liv efter att ha blivit attackerad.

---


#### Exempel på användning:

    krigare = Krigare("Thor")  
    vapen = Vapen("Svärd", 20)  
    krigare.lägg_till_vapen(vapen)  
    krigare.använd_vapen()  # Output: Thor använder Svärd  
    krigare.ta_skada(30)  # Output: Thor har tagit 30 skada. Hälsa nu: 70  

---

### Steg 3: Skapa en Fiende

#### Instruktioner:

1. **Skapa en klass `Fiende`:**
   - Skapa en konstruktor på samma sätt som för `Krigare`, där `Fiende` har ett namn och en startande hälsa på 100.
   - Implementera samma metoder som för `Krigare`, inklusive att fienden kan ta skada, tilldelas ett vapen och använda sitt vapen.
   - Implementera även metoden `är_vid_liv()` för att kontrollera om fienden fortfarande lever.


---

#### Exempel på användning:

    fiende = Fiende("Jätte")  
    vapen = Vapen("Yxa", 25)  
    fiende.lägg_till_vapen(vapen)  
    fiende.ta_skada(40)  # Output: Jätte har tagit 40 skada. Hälsa nu: 60  

---

### Steg 4: Kamp mellan krigaren och fienden

#### Instruktioner:

1. **Skapa en klass `Kamp`:**
   - Skapa en konstruktor som tar två parametrar: `krigare` och `fiende`. Dessa ska vara instanser av klasserna `Krigare` och `Fiende`.
   - Implementera en metod `starta()` som låter krigaren och fienden slåss. Varje runda ska krigaren och fienden använda sina vapen för att orsaka skada på varandra.
     - Krigaren och fienden turas om att attackera. Varje gång de attackerar ska vapnets skada dras från den andres hälsa.
     - Striden pågår tills någon av dem förlorar all sin hälsa.
   - Implementera en metod `slutresultat()` som visar vem som vann kampen genom att kontrollera vem som är vid liv när striden är över.


---

#### Exempel på användning:

    krigare = Krigare("Thor")  
    fiende = Fiende("Jätte")  
    vapen1 = Vapen("Svärd", 20)  
    vapen2 = Vapen("Yxa", 25)  
    krigare.lägg_till_vapen(vapen1)  
    fiende.lägg_till_vapen(vapen2)  

    kamp = Kamp(krigare, fiende)  
    kamp.starta()  
    kamp.slutresultat()  # Output: Thor vann kampen!  
