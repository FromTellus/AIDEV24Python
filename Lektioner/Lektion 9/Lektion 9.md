---
marp: true
paginate: true
theme: distansakademin
class: lead gaia
---

# Felhantering i Python

---

## Agenda
- Introduktion till felhantering och undantag i Python
- Användning av `try`, `except`, `else`, `finally`
- Hur man skapar och använder egna undantag
- Förklaring av nyckelbegrepp: `raise`, `pass`, och andra
- Förstå och hantera fel i Python
- Praktiska exempel och bästa praxis

---

## Inledning

Felhantering är en kritisk del av programmering som gör det möjligt för oss att skapa robusta och användarvänliga applikationer. I Python hanteras fel genom **undantag**, vilket ger oss kontroll över hur programmet reagerar på oväntade situationer.

- **Varför felhantering?**
  - Förhindra att programmet kraschar
  - Ge användaren informativa felmeddelanden
  - Underlätta felsökning och underhåll av koden

- **Vad kommer vi att lära oss?**
  - Hur undantag fungerar i Python
  - Hur man hanterar undantag effektivt
  - Hur man skapar egna undantag för anpassade fel

---

## Vad är undantag?

- **Undantag** är händelser som uppstår under körningen av ett program och stör det normala flödet av exekvering.
- De representerar fel eller oväntade situationer, som division med noll eller försök att öppna en fil som inte finns.
- Python har en mängd inbyggda undantag som kan användas för att identifiera och hantera olika typer av fel.

**Vanliga inbyggda undantag:**

- `ZeroDivisionError` - Försök att dividera med noll.
- `TypeError` - Felaktig typanvändning, t.ex. att addera en sträng och ett tal.
- `ValueError` - Ett objekt har rätt typ men felaktigt värde.
- `FileNotFoundError` - Försök att öppna en fil som inte finns.

**Exempel på ett undantag:**

Om vi försöker köra `resultat = 10 / 0` kommer Python att generera ett `ZeroDivisionError`.

---

## `try` och `except`

För att hantera undantag i Python använder vi `try` och `except`-satser.

- **`try`-blocket**: Här placerar vi koden som kan orsaka ett undantag.
- **`except`-blocket**: Här definierar vi hur undantaget ska hanteras om det uppstår.

**Syntax:**

    try:
        # Kodavsnitt som kan orsaka ett undantag
    except ExceptionType:
        # Kod som körs om ett specifikt undantag inträffar

- Vi kan ha flera `except`-block för att hantera olika typer av undantag.
- Om inget undantag inträffar i `try`-blocket, hoppar programmet över `except`-blocken.

---

### Exempel på `try` och `except`

Försöker dividera ett tal med noll:

    try:
        resultat = 10 / 0
    except ZeroDivisionError:
        print("Du kan inte dividera med noll!")

**Vad händer här?**

- Koden inom `try`-blocket försöker dividera 10 med 0.
- Detta genererar ett `ZeroDivisionError`.
- `except ZeroDivisionError` fångar undantaget och kör koden inom `except`-blocket.
- Meddelandet "Du kan inte dividera med noll!" skrivs ut till konsolen.

---

## Flera `except`-block

- Vi kan hantera olika typer av undantag separat genom att använda flera `except`-block.
- Detta gör att vi kan ge mer specifik felhantering beroende på vilket undantag som inträffar.

---

**Exempel:**

    try:
        tal = int(input("Ange ett heltal: "))
        resultat = 10 / tal
    except ValueError:
        print("Du måste ange ett giltigt heltal!")
    except ZeroDivisionError:
        print("Du kan inte dividera med noll!")

**Vad händer här?**

- Om användaren anger ett värde som inte är ett heltal, genereras ett `ValueError`.
- Om användaren anger noll, genereras ett `ZeroDivisionError`.
- Varje undantag hanteras i sitt eget `except`-block.

---

## `else`-blocket

- **`else`-blocket** körs endast om inget undantag inträffar i `try`-blocket.
- Används för kod som ska köras när allt går som förväntat.

---

**Exempel:**

    try:
        resultat = 10 / 2
    except ZeroDivisionError:
        print("Du kan inte dividera med noll!")
    else:
        print("Resultatet är:", resultat)

**Förklaring:**

- Eftersom `10 / 2` inte orsakar ett undantag, hoppar programmet över `except`-blocket.
- `else`-blocket körs och skriver ut "Resultatet är: 5".

---

## `finally`-blocket

- **`finally`-blocket** körs alltid, oavsett om ett undantag inträffar eller inte.
- Används för att utföra städning, som att stänga filer eller frigöra resurser.

---

**Exempel:**

    try:
        fil = open('data.txt', 'r')
        innehåll = fil.read()
    except FileNotFoundError:
        print("Filen hittades inte!")
    else:
        print("Filen lästes in korrekt.")
    finally:
        print("Stänger filen.")
        fil.close()

**Förklaring:**

- Om filen `data.txt` inte hittas, genereras ett `FileNotFoundError`.
- `except`-blocket fångar undantaget och skriver ut ett meddelande.
- Oavsett om ett undantag inträffar eller inte, körs `finally`-blocket.
- I `finally`-blocket stänger vi filen med `fil.close()`.

---

## Förklaring av `raise`

- **`raise`** används för att manuellt generera ett undantag i koden.
- Det kan användas för att signalera att något har gått fel i programmet, även om Python inte genererar ett undantag automatiskt.

---

**Syntax:**

    raise ExceptionType("Felmeddelande")

**Exempel:**
    try: 
        ålder = -5
        if ålder < 0:
            raise ValueError("Åldern kan inte vara negativ!")
    except ValueError:
        print(ValueError, "fel")


**Förklaring:**

- Här kontrollerar vi om variabeln `ålder` är negativ.
- Om den är negativ, använder vi `raise` för att generera ett `ValueError` med ett anpassat felmeddelande.
- Detta avbryter programmet om undantaget inte hanteras.

---

## Förklaring av `pass`

- **`pass`** är ett null-operation statement i Python.
- Det gör ingenting när det körs och används som en platshållare när en sats krävs syntaktiskt men ingen kod behöver köras.

**När används `pass`?**

- När du vill skapa en tom funktion eller klass som du planerar att implementera senare.
- När du vill ha ett `except`-block som inte gör något (även om detta vanligtvis bör undvikas).

---

**Exempel:**

    def min_funktion():

    try:
        resultat = 10 / 0
    except ZeroDivisionError:
        pass  # Ignorerar felet (inte rekommenderat)

**Var försiktig!**

- Att använda `pass` i ett `except`-block kan göra det svårare att felsöka koden eftersom undantaget tystas.
- Det är oftast bättre att hantera undantaget eller åtminstone logga det.

---

## Konstruera egna undantag

- Ibland behöver vi skapa egna undantag för att representera fel som är specifika för vår applikation.
- För att skapa ett eget undantag, definierar vi en ny klass som ärver från inbyggda `Exception`-klassen eller någon av dess subklasser.

**Varför skapa egna undantag?**

- För att ge mer beskrivande och specifika felmeddelanden.
- För att underlätta felsökning och felhantering i större applikationer.
- För att separera olika feltyper och hantera dem på olika sätt.

**Hur skapar man ett eget undantag?**

- Definiera en ny klass som ärver från `Exception`.

---

### Exempel på att skapa ett eget undantag

    class EgetUndantag(Exception):
        """Ett anpassat undantag för specifika fel."""
        pass

**Förklaring:**

- Här skapar vi en ny klass `EgetUndantag` som ärver från `Exception`.
- Dokstrings kan användas för att dokumentera undantaget.
- `pass` används eftersom vi inte behöver lägga till ytterligare funktionalitet i klassen.

---

**Använda det egna undantaget:**

    raise EgetUndantag("Ett anpassat fel inträffade!")

- Med `raise` kan vi generera vårt egna undantag när en specifik situation uppstår.

---

## Varför använda felhantering?

- **Förbättrad användarupplevelse**: Genom att hantera fel kan vi ge användaren tydliga och informativa felmeddelanden istället för att låta programmet krascha.
- **Robusthet**: Felhantering gör att programmet kan fortsätta köra eller avslutas på ett kontrollerat sätt vid fel.
- **Underhållbarhet**: Det blir lättare att hitta och fixa buggar när fel hanteras korrekt.
- **Säkerhet**: Genom att hantera undantag kan vi förhindra att känslig information exponeras vid fel.

---

## Bästa praxis för felhantering

- **Specificera undantag**: Fånga specifika undantag istället för att använda en generell `except`-sats.

---

  **Bra:**

      except ValueError:
          print("Ogiltigt värde!")

  **Dåligt:**

      except Exception:
          print("Ett fel inträffade!")

---

- **Undvik tyst felhantering**: Låt inte `except`-block vara tomma eller innehålla endast `pass`.

  **Dåligt:**

      except ZeroDivisionError:
          pass  # Tystar undantaget

  **Bra:**

      except ZeroDivisionError:
          print("Du kan inte dividera med noll!")

---

- **Använd `finally` för rengöring**: Använd `finally` för att frigöra resurser som filer eller nätverksanslutningar.

      try:
          fil = open('data.txt', 'r')
      finally:
          fil.close()

---

- **Logga fel**: Använd loggning för att registrera fel för senare analys.

      import logging

      logging.basicConfig(filename='app.log', level=logging.ERROR)

      try:
          resultat = 10 / 0
      except Exception as e:
          logging.error("Ett fel inträffade: %s", e)

---

- **Återanvänd egna undantag**: Skapa egna undantag för vanliga feltyper i din applikation.

- **Dokumentera felhanteringen**: Kommentera och dokumentera var och hur undantag hanteras.

- **Testa undantag**: Skriv testfall som verifierar att undantag höjs och hanteras korrekt.

---

## Sammanfattning

- Felhantering är en viktig del av att skriva robusta och pålitliga program.
- Genom att förstå och använda `try`, `except`, `else` och `finally` kan vi kontrollera hur vårt program reagerar på fel.
- Att skapa egna undantag hjälper oss att hantera applikationsspecifika fel på ett strukturerat sätt.
- Bästa praxis inom felhantering förbättrar inte bara användarupplevelsen utan underlättar också underhåll och vidareutveckling av koden.



---

## Övningar

1. **Fånga flera undantag**
   - Skriv ett program som läser in ett tal från användaren och dividerar 100 med det talet.
   - Hantera både `ZeroDivisionError` och `ValueError`.

2. **Eget undantag**
   - Skapa en egen undantagsklass `UnderÅlderError`.
   - Skriv en funktion som kontrollerar om en användare är över 18 år, annars kastar den `UnderÅlderError`.

3. **Användning av `finally`**
   - Skriv ett program som öppnar en fil och läser dess innehåll.
   - Använd `try`, `except` och `finally` för att säkerställa att filen alltid stängs, även om ett undantag inträffar.

---

4. **Använd `else`-blocket**
   - Skriv ett program som försöker konvertera en sträng till ett heltal.
   - Om konverteringen lyckas, skriv ut talet multiplicerat med 2.
   - Använd `try`, `except`, och `else` för att hantera möjliga undantag.

5. **Fångar alla undantag**
   - Skriv ett program där du använder en generell `except`-sats för att fånga alla typer av undantag.
   - Resonera kring varför detta kan vara en dålig idé i praktiken.

6. **Kedjade undantag**
   - Skriv en funktion som försöker öppna en fil och om det misslyckas, kastar ett eget undantag `FilFel` med en beskrivande feltext.
   - Använd `raise` från det ursprungliga undantaget för att behålla ursprungsinformationen.

---

7. **Logga undantag**
   - Skriv ett program som använder loggning för att skriva ut information om ett undantag till en loggfil.
   - Använd `try` och `except` och importera modulen `logging`.

8. **Validera inmatning**
   - Skriv en funktion som tar en e-postadress som inmatning.
   - Kontrollera att inmatningen innehåller "@" och "."
   - Om inte, kasta ett `ValueError` med ett lämpligt felmeddelande.
