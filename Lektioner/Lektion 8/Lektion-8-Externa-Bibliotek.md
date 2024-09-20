---
marp: true
paginate: true
theme: distansakademin
class: lead gaia
---

# Externa bibliotek i Python

## Agenda
- Introduktion till externa bibliotek och deras betydelse
- Skillnader mellan ramverk och bibliotek
- Hur man installerar och importerar externa bibliotek i Python
- Vanliga utvecklingsområden med Python:
  - Webbutveckling
  - Dataanalys och vetenskaplig beräkning
  - Maskininlärning och AI
  - Automatisering och skript
  - Spelutveckling
  - GUI-utveckling
  - Cybersecurity och penetrationstester

---

## Inledning

Python är känt för sina externa bibliotek som drastiskt utökar språkets kapacitet bortom vad standardbiblioteket erbjuder. Dessa bibliotek gör det möjligt att bygga allt från webbapplikationer till maskininlärningsmodeller och spel. Externa bibliotek är därför en viktig del av Python-utveckling, oavsett vilket område du arbetar inom.

---

### Varför behövs externa bibliotek?

Medan Pythons standardbibliotek täcker många grundläggande behov (t.ex. filhantering, nätverkskommunikation, matematiska beräkningar), behövs externa bibliotek för att utföra mer avancerade eller specialiserade uppgifter. 

Externa bibliotek utvecklas ofta av tredje part och uppdateras regelbundet för att inkludera nya funktioner och förbättringar. Detta innebär att de ger utvecklare tillgång till de senaste teknikerna och funktionerna inom sina respektive områden.

---
# Skillnader mellan Ramverk och Bibliotek

---

När du utvecklar i Python stöter du ofta på termerna **ramverk** och **bibliotek**. Även om de båda är verktyg som underlättar utvecklingen, skiljer de sig åt i hur de används och deras roll i applikationsstrukturen.

---

## Ramverk

- **Inversion of Control**: Ramverk styr flödet av applikationen. Det anropar din kod vid specifika punkter, vilket innebär att du anpassar din kod till ramverkets struktur.
- **Struktur och Arkitektur**: Ramverk erbjuder en tydlig arkitektur och uppmuntrar till konventioner, vilket kan leda till mer organiserad och underhållbar kodbas.
- **Fullfjädrade Lösningar**: De inkluderar ofta en uppsättning verktyg och funktioner för att hantera olika aspekter av utvecklingen, såsom databashantering, autentisering, routing och mer.
- **Exempel i Python**:
  - **Django**: Ett komplett webbramverk som erbjuder allt från ORM (Object-Relational Mapping) till en inbyggd administrationspanel.
  - **Flask**: Även om Flask är ett mikroramverk, erbjuder det ändå en struktur för att bygga webbtjänster och hanterar routing och request handling.

---

## Bibliotek

- **Kontroll av Flödet**: När du använder ett bibliotek, har du kontroll över flödet i din applikation. Du anropar bibliotekets funktioner när du behöver dem.
- **Specifik Funktionalitet**: Bibliotek är designade för att utföra specifika uppgifter eller tillhandahålla specifika funktioner utan att diktera den övergripande strukturen på din applikation.
- **Flexibilitet**: De kan enkelt integreras i olika delar av din applikation utan att tvinga fram en viss arkitektur.
- **Exempel i Python**:
  - **Requests**: Ett bibliotek för att hantera HTTP-förfrågningar, vilket gör det enkelt att interagera med webbtjänster.
  - **NumPy**: Ett bibliotek för numeriska beräkningar som erbjuder stöd för stora, fler-dimensionella matriser och matriskomputation.

---

## Sammanfattning

- **Ramverk** är som en grundstruktur för din applikation som bestämmer hur olika delar ska interagera och organiseras. De erbjuder omfattande verktyg och kräver att du följer deras konventioner.
- **Bibliotek** är verktyg du kan använda för att utföra specifika uppgifter inom din applikation, utan att påverka dess övergripande struktur.


---

## Installation och import av externa bibliotek

För att kunna använda dessa bibliotek i dina projekt behöver de först installeras. Den vanligaste metoden för att installera externa bibliotek är genom ett paketinstallationsverktyg som heter **`pip`**. `pip` är ett inbyggt verktyg i Python och används för att hämta, installera och hantera paket från Python Package Index (PyPI).

---



### Vad är `pip`?

`pip` är det verktyg som gör det enkelt att installera externa bibliotek från Python Package Index (PyPI). PyPI är en stor databas med tusentals Python-paket som utvecklare världen över har bidragit till. Med `pip` kan du snabbt och enkelt installera dessa paket direkt till din Python-miljö.

För att säkerställa att du har den senaste versionen av `pip`, kan du uppdatera det genom att köra följande kommando:
```
pip install --upgrade pip
```

Detta kommando ser till att du använder den senaste versionen av `pip`, vilket kan vara nödvändigt för att installera vissa moderna paket.

---

### Installera bibliotek med `pip`

För att installera ett bibliotek med `pip` använder du kommandot `pip install` följt av bibliotekets namn. Detta laddar ner biblioteket från PyPI och installerar det i din Python-miljö.

Exempel på installation av ett vanligt bibliotek, **Pandas**:
```
pip install pandas
```
Efter installationen är biblioteken tillgängliga och kan importeras i din kod. Notera att om du använder en **virtuell miljö** (vilket rekommenderas, speciellt för projekt med flera beroenden), kommer biblioteket att installeras endast för den aktuella miljön, vilket förhindrar konflikter med andra projekt.

---

#### Lokala vs. Globala installationer

- **Global installation** innebär att biblioteket installeras för alla Python-projekt på din dator. Detta kan leda till versioneringskonflikter om olika projekt kräver olika versioner av samma bibliotek.
- **Lokal installation** sker inom en specifik projektmiljö, vanligtvis i en **virtuell miljö**. Detta rekommenderas eftersom det isolerar biblioteket till ett enskilt projekt och förhindrar att beroendekonflikter uppstår.

---

### Hantera virtuella miljöer

En virtuell miljö är en isolerad Python-miljö där du kan installera paket och beroenden utan att påverka den globala Python-installationen på din dator. Att använda virtuella miljöer är en bra praxis när du arbetar med projekt som kräver specifika biblioteksversioner.

#### Skapa en virtuell miljö

För att skapa en ny virtuell miljö använder du kommandot `venv`, som är inbyggt i Python:
```
python -m venv venv
```

Detta kommando skapar en mapp som heter `venv` i ditt projekt. I denna mapp lagras en isolerad version av Python och de paket som installeras inom miljön.

---

#### Aktivera den virtuella miljön

För att använda en virtuell miljö måste den aktiveras. När den är aktiverad kommer alla kommandon du kör (som `pip install`) att påverka den isolerade miljön istället för din globala Python-installation.

- På **Windows**:
```
.\venv\Scripts\activate
```

- På **macOS/Linux**:
```
source venv/bin/activate
```

När miljön är aktiverad ser du något i stil med `(venv)` framför din kommandoprompt, vilket indikerar att du arbetar i den isolerade miljön.

---

#### Installera bibliotek i en virtuell miljö

När den virtuella miljön är aktiverad kan du installera bibliotek på samma sätt som du skulle göra globalt. Till exempel:

```
pip install numpy
```

Biblioteket installeras då endast i den virtuella miljön och är isolerat från andra projekt på din dator.

---

#### Inaktivera den virtuella miljön

När du är klar med arbetet i din virtuella miljö kan du inaktivera den genom att köra kommandot:

```
deactivate
```

Detta återställer din terminal till det globala tillståndet, där du återigen använder den globala Python-miljön.

---

### Importera bibliotek i Python

Efter att ha installerat ett externt bibliotek måste du importera det i ditt Python-program för att kunna använda dess funktioner. Detta görs med hjälp av `import`-kommandot. När du importerar ett bibliotek kan du även ge det ett alias för att göra koden mer kortfattad och läsbar.

Exempel på att importera **NumPy** och **Pandas** med alias:

```
import numpy as np
import pandas as pd
```

- **NumPy** importeras här som `np`, vilket gör att vi kan använda kortare kommandon i vår kod, som `np.array()` istället för `numpy.array()`.
- **Pandas** importeras som `pd`, vilket är en vanlig konvention i Python-communityn för att göra koden enklare att läsa.

---

#### Importera specifika funktioner från ett bibliotek

Ibland behöver du bara en specifik funktion från ett stort bibliotek. I sådana fall kan du välja att importera enbart den funktionen, vilket kan spara minne och förbättra kodens läsbarhet.

Exempel på att importera endast `array` från **NumPy**:
```
from numpy import array
```

Nu kan du direkt använda `array`-funktionen utan att först skriva `numpy.array`.

---

### Hantera bibliotek och beroenden

När du arbetar med ett Python-projekt är det viktigt att hålla reda på vilka externa bibliotek du använder och vilka versioner av dem som fungerar bäst med din applikation. Ett vanligt sätt att hantera detta är att använda en **`requirements.txt`**-fil. Denna fil listar alla beroenden för ditt projekt och deras versioner, vilket gör det enkelt att återskapa miljön på en annan dator.

#### Skapa en `requirements.txt`-fil

För att skapa en lista över alla installerade bibliotek och deras versioner kan du använda kommandot:
```
pip freeze > requirements.txt
```

Detta kommando genererar en `requirements.txt`-fil som listar alla aktuella bibliotek i din miljö.

---

#### Installera beroenden från `requirements.txt`

Om du delar ditt projekt med någon annan, eller om du själv vill installera alla beroenden i en ny miljö, kan du använda `requirements.txt` för att installera alla bibliotek samtidigt:
```
pip install -r requirements.txt
```

Detta ser till att exakt samma bibliotek och versioner installeras, vilket minimerar risken för kompatibilitetsproblem mellan olika datorer eller miljöer.

---

### Sammanfattning

1. **`pip`** är det verktyg du använder för att installera externa bibliotek i Python. Det gör det möjligt att snabbt ladda ner och installera paket från PyPI.
2. För att undvika beroendekonflikter och hålla dina projekt organiserade är det en god praxis att använda **virtuella miljöer**, där varje projekt har sina egna biblioteksversioner.
3. Efter installation kan du importera biblioteken i din kod med `import`, och ibland är det praktiskt att använda alias för att göra koden mer kortfattad och lättläst.
4. **`requirements.txt`** är ett verktyg för att hantera och dokumentera projektets beroenden, vilket gör det enkelt att återskapa projektmiljön på andra maskiner.

Genom att använda `pip` och virtuella miljöer kan du hantera externa bibliotek och säkerställa att dina Python-projekt är välorganiserade och lätta att underhålla.

---

## Vanliga utvecklingsområden med Python

Python är ett mångsidigt språk som används inom en rad olika utvecklingsområden, tack vare sina många bibliotek, ramverk och verktyg. Nedan listas några av de mest populära områdena, tillsammans med rätt terminologi för de verktyg som används inom dessa sammanhang.

---

### Webbutveckling

Python är ett populärt språk för att bygga webbapplikationer, särskilt på serversidan. För att strukturera och utveckla webbprojekt används oftast ramverk. Två av de mest populära webbramverken är **Flask** och **Django**.

---

- **Flask**: Flask är ett mikro-ramverk som används för att skapa webbapplikationer. Eftersom Flask är minimalistiskt och flexibelt, tillåter det utvecklare att välja externa komponenter som databas, autentisering och säkerhet. Det är särskilt användbart för små till medelstora applikationer och prototyper där utvecklare vill ha full kontroll över vilka komponenter som används.

Exempel:
```
from flask import Flask  
app = Flask(__name__)  

@app.route("/")  
def hello():  
    return "Hello, World!"  

if __name__ == "__main__":  
    app.run()
```
---

- **Django**: Django är ett fullskaligt webbapplikationsramverk som följer "batteries included"-principen. Det innebär att det levereras med många inbyggda funktioner som gör det möjligt att bygga komplexa applikationer med minimalt extra arbete. Django inkluderar funktioner för användarhantering, databasinteraktion, säkerhet och administrativt gränssnitt, vilket gör det idealiskt för större applikationer.

Exempel:
```
django-admin startproject myproject  
python manage.py runserver
```
---

### Användningsområden för webbutveckling

Flask används ofta för att bygga små till medelstora API:er och webbplatser, medan Django är mer lämpat för större projekt som kräver mycket funktionalitet, säkerhet och skalbarhet, till exempel e-handelsplattformar och sociala nätverk.

---

### Dataanalys och vetenskaplig beräkning

Python har blivit standard inom dataanalys och vetenskapliga beräkningar tack vare kraftfulla bibliotek som **NumPy**, **Pandas** och **SciPy**. Dessa är bibliotek och inte ramverk, då de erbjuder specifika funktioner för datahantering och beräkningar.

---

- **NumPy**: NumPy är ett bibliotek för numeriska beräkningar och hantering av stora datamängder i form av arrayer och matriser. Det möjliggör snabba och effektiva matematiska operationer som är mycket mer optimerade än vanliga Python-listor.

- **Pandas**: Pandas är ett bibliotek som erbjuder kraftfulla datastrukturer, särskilt **DataFrames**, vilket gör det enkelt att manipulera och analysera strukturerad data som tabeller och tidsserier. Det används flitigt för dataanalys och hantering av stora dataset.

- **SciPy**: SciPy bygger på NumPy och erbjuder ytterligare verktyg för vetenskapliga och tekniska beräkningar, inklusive optimering, integration och statistik. Detta gör det till ett populärt val för forskare och ingenjörer.

---

### Användningsområden för dataanalys

Python används inom forskning, ekonomi och affärsanalys för att bearbeta och analysera stora dataset. Bibliotek som Pandas och NumPy ligger till grund för dessa arbetsflöden, medan SciPy ger mer avancerade funktioner för vetenskapliga beräkningar.

---

### Maskininlärning och AI

Inom maskininlärning och artificiell intelligens (AI) används Python tillsammans med ett antal kraftfulla ramverk och bibliotek. Här är det viktigt att skilja mellan bibliotek som erbjuder specifika funktioner och ramverk som tillhandahåller en struktur för att bygga hela system.

---

- **Scikit-learn**: Scikit-learn är ett ramverk för maskininlärning och erbjuder verktyg för klassificering, regression, klustring och prediktiv modellering. Scikit-learn är perfekt för att bygga och utvärdera traditionella maskininlärningsmodeller.

- **TensorFlow**: TensorFlow kan fungera både som ett bibliotek och ett ramverk. Som bibliotek erbjuder det funktioner för att bygga och träna neurala nätverk och djupinlärningsmodeller, och som ramverk tillhandahåller det en komplett infrastruktur för att bygga och distribuera AI-modeller. TensorFlow används både i forskning och produktion för avancerade AI-system.

- **PyTorch**: PyTorch är ett ramverk för djupinlärning och har blivit mycket populärt inom forskningsvärlden tack vare sin flexibilitet och dynamiska beräkningsgraf. Det används främst för att bygga och träna komplexa neurala nätverk, och har fått en allt större användning inom industrin för att skapa produktionsklara AI-system.

---

### Användningsområden för maskininlärning och AI

Python är det mest populära språket för maskininlärning och AI-utveckling. Scikit-learn används för klassisk maskininlärning, medan TensorFlow och PyTorch används för mer avancerad djupinlärning och neurala nätverk, både inom forskning och kommersiella projekt.

---

### Automatisering och skript

Python är utmärkt för att skriva skript som automatiserar repetitiva uppgifter, och bibliotek som **Selenium** och **BeautifulSoup** används ofta för sådana uppgifter.

- **Selenium**: Selenium är ett verktyg för att automatisera webbläsarinteraktioner. Det används ofta för testautomation, där utvecklare kan simulera användarbeteenden och testa webbplatser automatiskt.

- **BeautifulSoup**: BeautifulSoup är ett bibliotek för webbskrapning, som används för att extrahera data från HTML- och XML-dokument. Det används ofta för att samla in data från webbplatser för vidare analys.

---

### Användningsområden för automatisering

Python används för att automatisera olika typer av arbetsflöden, från webbskrapning till att automatisera interaktioner med applikationer och system. Verktyg som Selenium och BeautifulSoup gör det enkelt att hantera webbläsare och samla in data.

---

### Spelutveckling

Python används ibland för enklare spelutveckling, och det mest använda biblioteket för detta ändamål är **Pygame**. Här handlar det om ett bibliotek, inte ett ramverk.

- **Pygame**: Pygame är ett bibliotek som används för att utveckla 2D-spel i Python. Det erbjuder stöd för grafik, ljud och användarinput, vilket gör det lämpligt för att bygga spelprototyper och utbildningsspel.

---

### Användningsområden för spelutveckling

Python används mest för enklare 2D-spel och prototyper. Pygame är ett populärt val för utvecklare som vill komma igång snabbt med spelutveckling utan att behöva lära sig komplexa spelmotorer.

---

### GUI-utveckling

Python kan också användas för att bygga grafiska användargränssnitt (GUI) för desktop-applikationer. Här används bibliotek som **Tkinter** och **PyQt**.

- **Tkinter**: Tkinter är Pythons standardbibliotek för att bygga enkla GUI-applikationer. Det erbjuder grundläggande komponenter som knappar, textfält och menyer.

- **PyQt**: PyQt är ett mer avancerat GUI-verktyg som används för att skapa plattformsoberoende, komplexa applikationer med professionella användargränssnitt.

---

### Användningsområden för GUI-utveckling

Python används för att bygga desktop-applikationer med grafiska användargränssnitt. Tkinter används för enklare applikationer, medan PyQt används för mer avancerade och professionella GUI-applikationer.

---

### Cybersecurity och penetrationstester

Python används också inom cybersäkerhet för att utveckla verktyg för penetrationstester och säkerhetsanalyser. Verktyg som **Scapy** och **Pwntools** är vanliga inom detta område.

- **Scapy**: Scapy är ett kraftfullt verktyg för att analysera och manipulera nätverkspaket. Det används inom penetrationstester för att skapa och analysera anpassade nätverkspaket.

- **Pwntools**: Pwntools är ett ramverk för utveckling av exploits och används av säkerhetsforskare och etiska hackare för att analysera och utnyttja sårbarheter i system.

---

### Användningsområden för cybersecurity

Python används flitigt inom nätverks- och säkerhetsforskning. Verktyg som Scapy och Pwntools gör det möjligt att utföra penetrationstester och utveckla verktyg för att analysera och exploatera säkerhetssårbarheter.

---

# Bibliotek – Rich, Tkinter och Requests

I denna presentation kommer vi att gå igenom tre populära Python-bibliotek: **Rich**, **Tkinter**, och **Requests**. Vi kommer att förklara deras huvudsakliga funktioner och vilka parametrar som används i viktiga metoder.

---

## **Rich – Skapa snygga terminalutskrifter med Python**

**Rich** är ett Python-bibliotek som gör det enkelt att skapa visuellt tilltalande terminalutskrifter. Det erbjuder flera funktioner som färgglad text, snygga tabeller, progress bars, och mer.

### Installation

För att installera **Rich** använder du följande kommando:

pip install rich

---

### Viktiga Funktioner

#### 1. **Färgglad Text**
Rich låter dig formatera och visa text i olika färger och stilar. Använd `Console`-klassen för att skriva ut i terminalen.

- **Metod:** `print(text, style)`
  - **Parameter `text`:** Strängen som ska skrivas ut.
  - **Parameter `style`:** En sträng som specificerar färg och stil, t.ex. `"bold red"`, `"underline blue"`.
  
Exempel: För att skriva ut "Hej, världen!" i fet röd text, använder du `console.print("Hej, världen!", style="bold red")`.

---

#### 2. **Tabeller**
Rich erbjuder ett enkelt sätt att skapa och visa tabeller i terminalen med hjälp av `Table`-klassen.

- **Metod:** `add_column(header, style, no_wrap, justify)`
  - **Parameter `header`:** Namnet på kolumnen.
  - **Parameter `style`:** Färg och stil för kolumnen, t.ex. `"cyan"`, `"magenta"`.
  - **Parameter `no_wrap`:** Boolesk värde som anger om texten ska brytas inom kolumnen.
  - **Parameter `justify`:** Justering av texten inom kolumnen, t.ex. `"left"`, `"right"`, `"center"`.

- **Metod:** `add_row(*columns)`
  - **Parameter `*columns`:** En sekvens av värden som representerar en rad i tabellen.

Exempel: För att lägga till en rad med data i tabellen, använder du `table.add_row("Alice", "Interstellar", "25")`.

---

#### 3. **Progress Bars**
Progress bars är ett utmärkt sätt att visa framsteg i långsamma processer. Med Rich kan du enkelt skapa progress bars och anpassa deras utseende med `Progress`-klassen.

- **Metod:** `track(iterable, description)`
  - **Parameter `iterable`:** En itererbar sekvens, t.ex. en lista eller ett intervall.
  - **Parameter `description`:** En sträng som beskriver vad progressbaren representerar, t.ex. `"Laddar..."`.

Exempel: För att visa en progress bar medan du itererar över ett intervall, använder du `for step in track(range(10), description="Laddar...")`.

---

#### 4. **Loggar**
Rich kan användas för att skapa färgglada loggar i terminalen med hjälp av `Console.log()`-metoden.

- **Metod:** `log(message, style, log_locals)`
  - **Parameter `message`:** Meddelandet som ska loggas.
  - **Parameter `style`:** Färg och stil för loggen, t.ex. `"bold green"`.
  - **Parameter `log_locals`:** Boolesk värde som anger om lokala variabler ska loggas.

Exempel: För att logga ett meddelande med lokala variabler, använder du `console.log("Detta är en loggrad", log_locals=True)`.

---

#### 5. **Markdown Rendering**
Rich kan rendera Markdown direkt i terminalen med hjälp av `Markdown`-klassen.

- **Metod:** `print(content)`
  - **Parameter `content`:** En sträng som innehåller Markdown-formattering.

Exempel: För att rendera Markdown-text, använder du `console.print(md)` där `md` är en instans av `Markdown` med din Markdown-sträng.

---

### Sammanfattning

**Rich** gör terminalutskrifter mer visuellt tilltalande genom att erbjuda:
- Färgglad och formaterad text
- Snygga tabeller
- Progress bars
- Färgglada loggar
- Markdown-rendering

Dessa funktioner förbättrar användarupplevelsen i terminalbaserade Python-applikationer.

---

## **Tkinter – Skapa grafiska användargränssnitt (GUI) i Python**

**Tkinter** är ett inbyggt Python-bibliotek som gör det enkelt att skapa grafiska användargränssnitt (GUI). Med Tkinter kan du skapa fönster, knappar, textfält, etiketter och många andra komponenter som behövs för att bygga ett interaktivt program.

### Installation

**Tkinter** följer med Pythons standardinstallation, så du behöver vanligtvis inte installera det separat. Om det inte finns installerat kan du installera det med kommandot nedan.

pip install python-tk

---

### Viktiga Funktioner

#### 1. **Skapa ett fönster**
Med Tkinter kan du skapa ett huvudfönster för din applikation. Det görs genom att instansiera `Tk`-klassen, och med `mainloop()` kan du hålla fönstret öppet tills användaren stänger det.

- **Metod:** `Tk()`
  - **Beskrivning:** Skapar ett nytt fönster för din GUI-applikation.

- **Metod:** `mainloop()`
  - **Beskrivning:** Startar applikationen och håller fönstret öppet.

Exempel: För att skapa ett enkelt fönster använder du `root = Tk()` och sedan `root.mainloop()` för att starta applikationen.

---

#### 2. **Etiketter (Labels)**
Tkinter låter dig visa statisk text i ditt fönster genom `Label`-klassen.

- **Metod:** `Label(master, text)`
  - **Parameter `master`:** Fönstret där etiketten ska visas, oftast `root`.
  - **Parameter `text`:** Texten som ska visas i etiketten.

Exempel: För att skapa en etikett som visar "Hej, världen!" i fönstret använder du `Label(root, text="Hej, världen!")`.

---

#### 3. **Knappar**
Med Tkinter kan du lägga till knappar i ditt fönster som användaren kan klicka på för att utföra handlingar.

- **Metod:** `Button(master, text, command)`
  - **Parameter `master`:** Fönstret där knappen ska visas.
  - **Parameter `text`:** Texten som ska visas på knappen.
  - **Parameter `command`:** Funktionen som ska köras när knappen klickas.

Exempel: För att skapa en knapp som skriver ut "Klickad" när den klickas, använd `Button(root, text="Klicka mig", command=klick_funktion)`.

---

#### 4. **Textfält (Entry)**
Textfält låter användaren skriva in data i GUI:t.

- **Metod:** `Entry(master)`
  - **Parameter `master`:** Fönstret där textfältet ska visas.

Exempel: För att skapa ett textfält där användaren kan skriva in text, använd `entry = Entry(root)`.

---

#### 5. **Placering av element (pack, grid, place)**
Tkinter erbjuder flera sätt att placera och arrangera GUI-komponenter i fönstret.

- **Metod:** `pack()`
  - **Beskrivning:** Packar komponenterna i fönstret automatiskt med de inställningar du anger.
  
- **Metod:** `grid(row, column)`
  - **Beskrivning:** Placerar komponenterna i ett rutnät där du kan specificera rad och kolumn.
  
- **Metod:** `place(x, y)`
  - **Beskrivning:** Placerar komponenterna exakt på en position baserat på x- och y-koordinater.

Exempel: För att placera en etikett på rad 0, kolumn 0 med `grid()`, använd `label.grid(row=0, column=0)`.

---

### Sammanfattning

**Tkinter** gör det enkelt att bygga grafiska användargränssnitt i Python med följande komponenter:
- **Fönster**: Skapa ett huvudfönster med `Tk()` och håll det öppet med `mainloop()`.
- **Etiketter**: Visa text med `Label()`.
- **Knappar**: Lägg till interaktivitet med `Button()`.
- **Textfält**: Låt användaren skriva in text med `Entry()`.
- **Placering av element**: Använd `pack()`, `grid()`, eller `place()` för att placera och arrangera komponenter.

Tkinter är ett kraftfullt verktyg för att skapa GUI-applikationer i Python på ett enkelt och effektivt sätt.

---

## **Requests – Enkel HTTP-förfrågningar i Python**

**Requests** är ett populärt Python-bibliotek som gör det enkelt att skicka HTTP-förfrågningar. Det används ofta för att hämta data från webbtjänster och API:er, eller för att interagera med webbplatser via GET, POST, PUT, DELETE och andra HTTP-metoder.

### Installation

För att installera **Requests** använder du följande kommando:

pip install requests


---

### Viktiga Funktioner

#### 1. **Skicka en GET-förfrågan**
Den vanligaste HTTP-metoden är `GET`, som används för att hämta data från en server.

- **Metod:** `get(url, params=None, headers=None, timeout=None)`
  - **Parameter `url`:** URL:en till den resurs du vill hämta.
  - **Parameter `params`:** (Valfritt) En dictionary eller bytes objekt som skickas som URL-parametrar.
  - **Parameter `headers`:** (Valfritt) En dictionary med HTTP-huvuden att inkludera i förfrågan.
  - **Parameter `timeout`:** (Valfritt) Tidsgränsen för förfrågan i sekunder.

Exempel: För att hämta en slumpmässig hundbild från Dog API, använd `requests.get("https://dog.ceo/api/breeds/image/random")`.

---

#### 2. **Skicka en POST-förfrågan**
Med `POST`-metoden kan du skicka data till en server, ofta för att skapa eller uppdatera resurser.

- **Metod:** `post(url, data=None, json=None, headers=None, timeout=None)`
  - **Parameter `url`:** URL:en till den resurs du vill skicka data till.
  - **Parameter `data`:** (Valfritt) Dictionary, bytes, eller filobjekt att skicka i förfrågans kropp.
  - **Parameter `json`:** (Valfritt) JSON-data som ska skickas i förfrågans kropp.
  - **Parameter `headers`:** (Valfritt) En dictionary med HTTP-huvuden att inkludera i förfrågan.
  - **Parameter `timeout`:** (Valfritt) Tidsgränsen för förfrågan i sekunder.

Exempel: För att skapa en ny post i JSONPlaceholder API, använd `requests.post("https://jsonplaceholder.typicode.com/posts", data=payload)` där `payload` är en dictionary med dina data.

---

#### 3. **Hantera JSON-data**
Många API:er använder JSON-format för att utbyta data. Requests har inbyggt stöd för att hantera JSON.

- **Metod:** `response.json()`
  - **Beskrivning:** Konverterar JSON-svaret från servern till en Python-dictionary.

Exempel: Efter att ha gjort en GET-förfrågan, använd `data = response.json()` för att konvertera svaret till en dictionary och sedan `print(data['key'])` för att få specifik information.

---

#### 4. **Skicka Headers**
Om du behöver skicka extra information som API-nycklar eller autentisering kan du inkludera HTTP-huvuden i dina förfrågningar.

- **Parameter `headers`:** En dictionary med nyckel-värde par som representerar HTTP-huvuden.

Exempel: För att skicka en autentiserings-token, använd `headers = {'Authorization': 'Bearer my_token'}` och inkludera den i din GET- eller POST-förfrågan.

---

#### 5. **Hantera Fel och Undantag**
Requests låter dig enkelt hantera fel med hjälp av `try-except` block för att fånga eventuella nätverksfel eller ogiltiga svar.

- **Metod:** `response.raise_for_status()`
  - **Beskrivning:** Kastar ett undantag om HTTP-förfrågan misslyckas (t.ex. statuskoden är 4xx eller 5xx).

Exempel: Använd `try-except` block för att fånga och hantera fel när du gör en förfrågan.

---

#### 6. **Timeouts**
För att undvika att programmet hänger sig vid långsamma förfrågningar kan du ange en timeout.

- **Parameter `timeout`:** Specificerar hur länge programmet ska vänta på ett svar innan det avbryts.

Exempel: För att sätta en timeout på 5 sekunder, använd `requests.get(url, timeout=5)`.

---

### Sammanfattning

**Requests** gör det enkelt att arbeta med HTTP-förfrågningar i Python. Här är några viktiga funktioner:
- **GET och POST-förfrågningar:** Hämta eller skicka data till servrar.
- **JSON-hantering:** Enkelt att konvertera JSON-svar till Python-datastrukturer.
- **Headers och autentisering:** Skicka extra information som API-nycklar eller tokens.
- **Felhanteirng:** Hantera undantag och fel som uppstår under förfrågningar.
- **Timeouts:** Förhindra att ditt program fastnar på långsamma svar.

Requests är ett kraftfullt och enkelt verktyg för att interagera med API:er och webbtjänster i Python.

---

## **Uppgifter**

### **Turtle – Uppgifter**

#### 1. **Rita en kvadrat**
- Använd Turtle för att rita en kvadrat på 100x100 pixlar.
- Tips: Du kan använda metoder som `forward()` för att rita linjer och `right()` för att vända vid hörnen.

#### 2. **Rita en cirkel**
- Rita en cirkel med valfri radie.
- Tips: Använd Turtle-metoden för att rita cirklar.

#### 3. **Rita en stjärna**
- Rita en enkel femuddig stjärna.
- Tips: Du kan behöva använda en loop och justera vinkeln för att få till en stjärnform.

---

### **Requests – Uppgifter**

#### 1. **Skicka en GET-förfrågan**
- Använd Requests för att hämta data från ett gratis API som levererar randomiserade användaruppgifter. Du kan använda API:t nedan:
  - [Random User API](https://randomuser.me/api/)
- Gör en GET-förfrågan till API:t och skriv ut svaret.

#### 2. **Hämta och extrahera JSON-data från ett API**
- Hämta data från ett API som ger en slumpmässig hundbild och extrahera URL:en till bilden från svaret.
  - [Dog API](https://dog.ceo/dog-api/)
- Gör en GET-förfrågan till API:t och skriv ut URL:en till hundbilden som finns i JSON-svaret.

#### 3. **Skicka en POST-förfrågan**
- Skicka en POST-förfrågan till ett API och skicka med ett enkelt meddelande eller användardata. Använd detta API för att testa:
  - [JSONPlaceholder API](https://jsonplaceholder.typicode.com/guide/) (test-API som inte kräver autentisering)

---
## **Rich – Uppgifter**

### 1. **Skriv ut färgglad text**
- Använd Rich för att skriva ut en färgglad hälsning i terminalen. Välj en färg och stil (fet, understruken, etc.).
- **Tips:** Experimentera med olika färger och stilar för att göra texten mer visuellt tilltalande.

### 2. **Visa en enkel tabell**
- Skapa en tabell med Rich som visar tre rader med data, till exempel namn, ålder och favoritfärg.
- **Tips:** Använd `add_column` och `add_row` metoderna för att strukturera din tabell.

### 3. **Använd en progress bar**
- Skapa en progress bar med Rich som visar laddningen av ett fiktivt projekt.
- **Tips:** Använd `track` funktionen för att visualisera framstegen i en loop.

---

## **Tkinter – Uppgifter**

### 1. **Skapa ett enkelt fönster**
- Skapa ett Tkinter-fönster som öppnas och visar texten "Välkommen!" med hjälp av en etikett (`Label`).
- **Tips:** Använd `Tk()` för att skapa fönstret och `Label()` för att visa texten.

### 2. **Lägg till en knapp**
- Skapa ett fönster med en knapp som säger "Klicka mig". När användaren klickar på knappen ska texten "Klickad!" visas i terminalen.
- **Tips:** Använd `Button()` och `command` för att definiera vad som händer när knappen klickas.

### 3. **Skapa ett textfält och visa texten**
- Skapa ett fönster med ett textfält (`Entry`) och en knapp. När användaren skriver in något i textfältet och klickar på knappen ska texten som användaren skrivit visas i terminalen.
- **Tips:** Använd `Entry()` för att skapa textfältet och hämta användarens input med `entry.get()`.
