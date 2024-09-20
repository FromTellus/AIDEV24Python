---
marp: true
paginate: true
theme: distansakademin
class: lead gaia
---

# Standardbibliotek i Python

## Agenda
- Introduktion till Pythons standardbibliotek
- `os`- Hantera operativsystemsfunktioner
- `sys`- Arbeta med systemparametrar och I/O-strömmar
- `math`- Matematiska funktioner och konstanter
- `datetime`- Arbeta med datum och tid
- `random`- Generera slumpmässiga värden
- `re`- Arbeta med reguljära uttryck (regex)
- `json`- Arbeta med JSON-data
- `collections`- Specialiserade datastrukturer
- `logging`-Logging
- Uppgifter för praktiska övningar

---

## Inledning

Python erbjuder ett brett utbud av standardbibliotek som underlättar programmeringen genom att tillhandahålla färdiga lösningar för vanliga problem. Dessa moduler kräver ingen installation och ingår direkt i Pythons kärna. I denna föreläsning kommer vi att titta på några av de mest använda standardbiblioteken som `os`, `sys`, `math`, `datetime`, `random`, `re`, `json`, och `collections`. Du kommer att lära dig hur man använder dessa moduler och hur de kan förenkla arbetet i många olika typer av projekt.

---
## `os`-biblioteket: Interagera med operativsystemet

Python's `os`-bibliotek gör det möjligt för ett program att kommunicera direkt med operativsystemet. Detta innebär att du kan utföra åtgärder som att navigera i filsystemet, hantera filer och kataloger, samt köra kommandon direkt från Python-skriptet.

Att använda `os`-modulen är särskilt användbart när du skapar systemadministrationsverktyg eller automatiserar uppgifter som annars skulle kräva manuella åtgärder, som att skapa kataloger, flytta filer, eller ändra miljövariabler.

---

### Vanliga funktioner i `os`-biblioteket

#### 1. `os.environ`
`os.environ` är en dictionary-liknande struktur som låter dig komma åt miljövariabler i operativsystemet. Miljövariabler är viktiga för att lagra systeminformation som filvägar, användarinställningar eller systemkonfigurationer.

```
Exempel:
hemdir = os.environ.get('HOME')  
print(f"Hemkatalogen är: {hemdir}")
```
Användningsområde: Om ditt program behöver hämta specifik information från operativsystemet, till exempel för att bestämma var användarens filer ska sparas eller för att hämta API-nycklar.

---

#### 2. `os.system(command)`
Denna funktion låter dig köra systemkommandon direkt från ditt Python-program. Det är ett sätt att automatisera shell-kommandon som du normalt skulle köra i en terminal.
Exempel:
```
os.system('ls')
```
Detta kommando listar alla filer och mappar i den aktuella katalogen, precis som om du skulle skriva det direkt i terminalen.

Användningsområde: Om du behöver utföra systemadministrationsuppgifter, som att starta eller stoppa tjänster, köra säkerhetskopieringar, eller exekvera skript.

---

#### 3. `os.path.join(path, *paths)`
Denna funktion används för att konstruera filvägar på ett plattformsoberoende sätt. Istället för att manuellt hantera olika filseparatörer ("/" för Unix-baserade system och "\\" för Windows), använder `os.path.join` rätt separator beroende på vilket operativsystem Python körs på.
Exempel:
```
filvag = os.path.join('min_mapp', 'fil.txt')  
print(f"Filens fullständiga sökväg är: {filvag}")
```
Användningsområde: När du bygger program som ska fungera på flera olika operativsystem och du behöver säkerställa att filvägar skapas korrekt oavsett plattform.

---

#### 4. `os.chdir(path)`
Denna funktion låter dig ändra den aktuella arbetskatalogen. Arbetskatalogen är den plats där ditt program för närvarande körs och där alla filoperationer sker om du inte anger något annat. Med `os.chdir` kan du flytta programmet till en annan katalog, vilket är användbart om du vill köra operationer i en specifik mapp.
```
Exempel:
os.chdir('/home/user/Documents')  
print(f"Nuvarande arbetskatalog är: {os.getcwd()}")
```
Användningsområde: Om ditt program behöver utföra filoperationer i olika kataloger, kan du använda `os.chdir` för att byta plats dynamiskt.

---

#### 5. `os.getpid()`
Denna funktion returnerar process-ID:t för det Python-program som körs. Process-ID (PID) är ett unikt nummer som identifierar varje körande process i ett operativsystem.
Exempel:
```
pid = os.getpid()  
print(f"Detta programs process-ID är: {pid}")
```
Användningsområde: Om du bygger ett program som hanterar flera processer eller behöver logga processinformation för felsökning eller övervakning, kan det vara värdefullt att veta vilket process-ID som används.

---

#### 6. `os.cpu_count()`
Denna funktion returnerar antalet CPU-kärnor som är tillgängliga på maskinen där programmet körs. Detta är särskilt användbart när du optimerar program som använder flera trådar eller processer, och du vill anpassa din programvara efter maskinens kapacitet.
Exempel:
```
cpu_antal = os.cpu_count()  
print(f"Antal CPU-kärnor tillgängliga: {cpu_antal}")
```
Användningsområde: Vid parallell bearbetning eller multithreading, där du vill optimera användningen av tillgängliga systemresurser.

---

### Sammanfattning
`os`-modulen i Python erbjuder kraftfulla verktyg för att interagera med operativsystemet. Genom att använda funktioner som `os.environ`, `os.system`, `os.path.join`, `os.chdir`, `os.getpid` och `os.cpu_count`, kan du skapa flexibla, plattformsoberoende program som automatiserar och effektiviserar olika systemuppgifter. Detta är särskilt värdefullt för systemadministration, datahantering och andra uppgifter som kräver direkt åtkomst till operativsystemet.

---

### Användningsområden:
- Dynamiskt hämta och ställa in miljövariabler för att konfigurera applikationer utan hårdkodning.
- Köra externa systemkommandon, till exempel för att hantera andra program eller utföra batch-processer.
- Skapa plattformsoberoende program som hanterar filvägar och systemkommandon på rätt sätt, oavsett operativsystem.
- Logga processinformation och optimera prestanda genom att anpassa ditt program till tillgängliga systemresurser.

---

## `sys`-biblioteket: Arbeta med systemparametrar och I/O-strömmar

`sys`-modulen är en central del av Python som låter oss hantera Python-tolken på en mer detaljerad nivå. Med `sys` kan vi få åtkomst till kommandoradsargument, systeminformation och standardströmmar som `stdin`, `stdout` och `stderr`. Den ger oss även möjlighet att avsluta program på ett kontrollerat sätt.

När du skapar skript som interagerar med användare via kommandoraden eller om du vill få detaljerad information om hur din applikation körs, är `sys`-modulen ett ovärderligt verktyg.

---

### Vanliga funktioner att känna till:

#### 1. `sys.argv`
`sys.argv` är en lista som innehåller de argument som skickas till programmet från kommandoraden när det körs. Det första elementet i listan är alltid programmets namn, medan följande element är de faktiska argumenten som användaren anger.
Exempel:
```
sys.argv[0]  
sys.argv[1]
```
Användningsområde: Om du vill skapa ett skript som tar in parametrar eller flaggor via kommandoraden, till exempel ett program som bearbetar filer baserat på användarinmatning.

---

#### 2. `sys.exit(status=0)`
Denna funktion avslutar programmet omedelbart och returnerar en statuskod. Om du skickar in `0` (eller inget alls) innebär det att programmet avslutades framgångsrikt. Andra värden indikerar att programmet avslutades på grund av ett fel.
Exempel:
```
sys.exit(1)  
```
Användningsområde: Om du vill avsluta programmet under specifika omständigheter, till exempel om ett fel upptäcks eller om användaren inte tillhandahåller nödvändiga kommandoradsargument.

---

#### 3. `sys.stdin`, `sys.stdout`, `sys.stderr`
Dessa tre standardströmmar representerar ingångs- och utgångskanaler för programmet.

- **`sys.stdin`**: Representerar standard inmatning. Normalt används den för att läsa från tangentbordet, men kan omdirigeras för att läsa från en fil eller annan källa.
- **`sys.stdout`**: Representerar standardutmatningen. Allt som skrivs med `print()` skickas till `sys.stdout`, men det kan omdirigeras till en fil om du vill logga utmatningen.
- **`sys.stderr`**: Standardströmmen för felmeddelanden. Felskrivningar skickas hit, vilket är användbart om du vill separera vanliga meddelanden från felmeddelanden.

---

Exempel:
```
data = sys.stdin.read()  
sys.stdout.write("Detta är en utskrift")  
sys.stderr.write("Det här är ett felmeddelande")  
```
Användningsområde: När du vill omdirigera indata eller utdata i ett program, till exempel för att skriva ut information till en fil istället för konsolen, eller för att skilja felmeddelanden från vanlig utmatning.

---

#### 4. `sys.path`
`sys.path` är en lista över sökvägar där Python letar efter moduler när du gör en import. Du kan lägga till sökvägar till denna lista för att dynamiskt ladda moduler från andra platser.

Exempel:
```
sys.path.append('/path/to/module')  
```
Användningsområde: Om du har moduler på anpassade platser utanför de vanliga sökvägarna och du behöver inkludera dessa i ditt projekt utan att flytta dem.

---

#### 5. `sys.platform`
Denna funktion returnerar en sträng som beskriver den plattform eller det operativsystem som Python körs på, till exempel `"linux"`, `"win32"`, eller `"darwin"` (för macOS).
Exempel:
```
sys.platform  
```
Användningsområde: Om du vill skapa plattformsoberoende program och behöver göra något annorlunda beroende på vilket operativsystem programmet körs på.

---

### Exempel:
Låt oss säga att vi bygger ett enkelt program som tar kommandoradsargument för att bearbeta filer, omdirigerar standardoutput till en fil, och avslutar programmet om något går fel.
```
sys.argv[0]  # Namn på programmet  
sys.argv[1]  # Första kommandoradsargumentet  
sys.stdout = open('output.log', 'w')  
print(f"Bearbetar filen: {sys.argv[1]}")  
sys.exit(0)  
```
---

### Användningsområden:
- **Skript som hanterar indata från kommandoraden**: Om du bygger verktyg som tar kommandoradsargument, till exempel filhanteringsverktyg eller automationsskript.
- **Kontrollerad programavslutning**: Om du vill avsluta programmet under specifika omständigheter och returnera en statuskod.
- **Loggning och omdirigering av output**: Omdirigera utmatning eller felmeddelanden till specifika filer för bättre loggning och felsökning.
- **Plattformsoberoende program**: Anpassa programmet baserat på vilken plattform det körs på, till exempel att köra olika systemkommandon beroende på om det är Windows eller Linux.

---

### Sammanfattning:
`sys`-modulen erbjuder ett kraftfullt sätt att kontrollera och hantera Python-program på en systemnivå. Genom att använda `sys.argv` kan vi hantera kommandoradsargument, med `sys.exit` kan vi kontrollera programflödet, och med `sys.stdin`, `sys.stdout` och `sys.stderr` kan vi hantera in- och utströmmen av data på ett flexibelt sätt. Oavsett om du bygger verktyg för systemadministration eller behöver kontrollera plattformsberoende kod, är `sys`-modulen en viktig del av Pythons ekosystem.

---

## `math`-biblioteket: Matematiska funktioner och konstanter

`math`-modulen i Python erbjuder ett brett utbud av matematiska funktioner som är användbara för att utföra både enkla och avancerade matematiska operationer. Från att räkna kvadratrötter och exponenter till att använda trigonometriska funktioner och matematiska konstanter som π, gör `math` det enklare att bygga vetenskapliga och tekniska applikationer.

Om du arbetar med matematik i någon form, som fysik, grafik, ingenjörsberäkningar eller statistik, kommer `math`-modulen att vara ett ovärderligt verktyg.

---

### Vanliga funktioner att känna till:

#### 1. `math.sqrt(x)`
Denna funktion returnerar kvadratroten av ett tal `x`. Det är en av de mest grundläggande funktionerna och används ofta i geometri, fysik och andra vetenskapliga beräkningar.

Exempel:
```
rot = math.sqrt(16)  # Resultat: 4  
```
Användningsområde: Vid beräkningar där du behöver räkna ut längden av en diagonal eller avståndet mellan två punkter i ett koordinatsystem (Pythagoras sats).

---

#### 2. `math.pow(x, y)`
`math.pow(x, y)` returnerar resultatet av att höja `x` till potensen `y`. Detta används för exponentiella beräkningar, till exempel när du behöver höja tal till kvadrat eller kub.

Exempel:
```
upphojt = math.pow(2, 3)  # Resultat: 8  
```
Användningsområde: Vanligt i vetenskapliga beräkningar och fysik, där många formler involverar potenser, till exempel i kraftlagar eller strömberäkningar.

---

#### 3. `math.pi`
`math.pi` ger dig tillgång till värdet av π (cirka 3.14159), som är en viktig konstant inom geometri och trigonometriska beräkningar. Den används för att beräkna omkrets och area av cirklar, samt i andra beräkningar som involverar vinklar och rotationer.

Exempel:
```
omkrets = 2 * math.pi * radie  
area = math.pi * radie ** 2  
```
Användningsområde: Geometri, fysik och ingenjörsberäkningar där cirklar och rotationer spelar en roll, till exempel beräkningar för hjul och roterande maskiner.

---

#### 4. Trigonometriska funktioner: `math.sin(x)`, `math.cos(x)`, `math.tan(x)`
Dessa funktioner returnerar sinus, cosinus och tangens av en vinkel (i radianer). De används flitigt i fysik och grafiska applikationer, särskilt i rörelseberäkningar och 3D-grafik.

Exempel:
```
sinusvarde = math.sin(math.pi / 2)  # Resultat: 1  
cosinusvarde = math.cos(0)  # Resultat: 1  
tangensvarde = math.tan(math.pi / 4)  # Resultat: 1  
```
Användningsområde: Fysikbaserade simuleringar som involverar vågrörelser, pendlar, eller projektionsberäkningar i grafik och animationer.

---

#### 5. `math.log(x, base)`
Denna funktion returnerar logaritmen av ett tal `x` baserat på den angivna basen. Om ingen bas anges, används naturliga logaritmen (bas e). Logaritmer används inom vetenskap och teknik för att hantera exponentiella tillväxt- och avtagande processer.

Exempel:
```
naturlig_log = math.log(10)  # Logaritmen av 10 i bas e  
log_base_10 = math.log(100, 10)  # Logaritmen av 100 i bas 10 (resultat: 2)
```
Användningsområde: Användbart i ekonomi (ränta och tillväxt), kemi (reaktionshastigheter) och fysik (radioaktivt sönderfall).

---

### Exempel på användning:
Låt oss bygga ett enkelt program som räknar ut både omkretsen och arean av en cirkel baserat på en radie som användaren matar in.
```
radie = float(input("Ange radien på cirkeln: "))  
omkrets = 2 * math.pi * radie  
area = math.pi * radie ** 2  
print(f"Omkretsen är: {omkrets}")  
print(f"Arean är: {area}")
```
---

### Användningsområden:
- **Geometriska beräkningar**: Använd `math`-modulen för att beräkna areor, volymer, och avstånd i olika former, som cirklar, sfärer och trianglar.
- **Vetenskapliga och tekniska beräkningar**: Perfekt för fysik och ingenjörsprojekt där avancerade matematiska beräkningar krävs.
- **Grafik och animation**: Trigonometriska funktioner är oumbärliga för att skapa realistiska rörelser och animationer i 2D- och 3D-grafik.
- **Logaritmer och exponentiella funktioner**: Används ofta i vetenskapliga simuleringar, tillväxtberäkningar, eller statistiska modeller där processer ökar eller minskar exponentiellt.

---

### Sammanfattning:
`math`-biblioteket ger dig alla verktyg du behöver för att utföra avancerade matematiska beräkningar i Python. Med funktioner för kvadratrötter, exponenter, trigonometriska funktioner och logaritmer kan du bygga program som hanterar allt från enklare geometri till mer avancerade fysik- och ingenjörsberäkningar. Genom att förstå och använda dessa funktioner effektivt kan du kraftigt förbättra noggrannheten och prestandan i dina beräkningar.

---


## `datetime`-biblioteket: Arbeta med datum och tid

`datetime`-modulen i Python erbjuder en uppsättning funktioner som låter dig arbeta med datum och tid på ett flexibelt och effektivt sätt. Oavsett om du behöver veta det aktuella klockslaget, manipulera datum, beräkna tidsskillnader eller formatera datum och tider, ger `datetime`-biblioteket dig de verktyg du behöver.

Att hantera datum och tid är en vanlig uppgift i många applikationer, allt från schemaläggning av uppgifter till loggning av händelser.

---

### Vanliga funktioner att känna till:

#### 1. `datetime.datetime.now()`
Denna funktion returnerar det aktuella datumet och klockslaget baserat på systemets tid. Det är användbart när du behöver veta det exakta ögonblicket då något sker, till exempel vid loggning av händelser.

Exempel:
```
nuvarande_tid = datetime.datetime.now()  
print(f"Nuvarande tid: {nuvarande_tid}")
```
Användningsområde: När du vill logga tidpunkter för händelser eller skapa tidsstämplar för filer eller databasposter.

---

#### 2. `datetime.timedelta()`
`timedelta` representerar ett tidsintervall eller skillnaden mellan två datum eller tider. Du kan använda `timedelta` för att lägga till eller dra ifrån tid från ett specifikt datum.

Exempel:
```
delta = datetime.timedelta(days=5)  
framtida_datum = datetime.datetime.now() + delta  
print(f"Fem dagar framåt: {framtida_datum}")
```
Användningsområde: När du behöver räkna ut framtida eller historiska datum, till exempel för att beräkna deadlines, scheman eller åldrar.

---

#### 3. `datetime.strftime(format)`
Denna metod formaterar ett `datetime`-objekt till en sträng enligt ett angivet format. Det är särskilt användbart när du vill skriva ut eller spara datum i en viss form, till exempel "YYYY-MM-DD" eller "DD/MM/YYYY".

Exempel:
```
datum = datetime.datetime.now()  
formaterat_datum = datum.strftime("%Y-%m-%d")  
print(f"Formaterat datum: {formaterat_datum}")
```
Användningsområde: Användbart för att presentera datum och tid i ett mänskligt läsbart format eller för att anpassa hur datum skrivs till filer eller skickas till andra system.

---

#### 4. `datetime.strptime(string, format)`
Denna metod konverterar en sträng som innehåller ett datum till ett `datetime`-objekt baserat på det angivna formatet. Detta är användbart när du arbetar med datum som lagras som strängar, till exempel i textfiler eller användarinmatning.

Exempel:
```
datum_strang = "2024-12-25"  
datum_objekt = datetime.datetime.strptime(datum_strang, "%Y-%m-%d")  
print(f"Omvandlat datum: {datum_objekt}")
```
Användningsområde: När du behöver konvertera datum från strängformat till `datetime`-objekt för att kunna bearbeta dem eller utföra beräkningar.

---

### Exempel på användning:
Låt oss säga att vi vill räkna ut hur många dagar som är kvar till en specifik händelse, som till exempel julafton. Vi kan använda `datetime` för att ta reda på det.
```
idag = datetime.datetime.now()  
julafton = datetime.datetime(year=idag.year, month=12, day=25)  
om_dagar = (julafton - idag).days  
print(f"Det är {om_dagar} dagar kvar till julafton.")
```
---

### Användningsområden:
- **Loggning**: Logga när händelser inträffar i ditt program, till exempel när användare loggar in eller när en viss process startar och slutar.
- **Schemaläggning och påmin

---

## `random`-biblioteket: Generera slumpmässiga värden

`random`-modulen i Python används för att generera pseudorandom tal och göra slumpmässiga val. Slumpmässiga tal och urval är viktiga i många applikationer, såsom spelprogrammering, simuleringar, statistik och automatiska tester. Python erbjuder en enkel och effektiv uppsättning funktioner i `random`-modulen för att hantera dessa behov.

Eftersom slumpmässighet används i så många områden, är `random`-modulen ett centralt verktyg när du behöver generera osäkerhet eller variation i ditt program.

---

### Vanliga funktioner att känna till:

#### 1. `random.random()`
Denna funktion returnerar ett flyttal mellan 0.0 och 1.0. Det är användbart när du behöver ett värde som representerar sannolikhet eller en slumpmässig faktor som påverkar programflödet.

Exempel:
```
slumptal = random.random()  
print(f"Slumpmässigt flyttal mellan 0 och 1: {slumptal}")
```
Användningsområde: När du vill simulera sannolikheter eller göra beslut baserat på en slumpmässig procentsats, som i spel där en viss händelse inträffar med viss sannolikhet.

---

#### 2. `random.randint(a, b)`
Denna funktion returnerar ett heltal mellan `a` och `b`, båda inkluderade. Detta är särskilt användbart när du behöver ett heltalsvärde inom ett specifikt intervall.

Exempel:
```
slumptal = random.randint(1, 100)  
print(f"Slumpmässigt tal mellan 1 och 100: {slumptal}")
```
Användningsområde: Vanligt inom spelutveckling där du behöver generera tärningskast, välja kort från en kortlek, eller simulera andra händelser som kräver heltalsvärden.

---

#### 3. `random.choice(sequence)`
Denna funktion returnerar ett slumpmässigt element från en sekvens, som en lista eller en sträng. Det är användbart när du behöver välja ett objekt från en mängd alternativ.

Exempel:
```
val = random.choice(['äpple', 'banan', 'körsbär'])  
print(f"Slumpmässigt valt objekt: {val}")
```
Användningsområde: Perfekt för scenarier där du har en lista med alternativ och vill välja ett av dem slumpmässigt, till exempel vid lottdragning eller slumpmässiga val i spel.

---

#### 4. `random.shuffle(sequence)`
Denna funktion slumpar om ordningen på elementen i en lista. Den modifierar listan direkt och är användbar när du behöver skapa oordning, till exempel när du blandar en kortlek eller skapar en slumpmässig ordning på uppgifter.

Exempel:
```
kortlek = ['Hjärter A', 'Spader K', 'Ruter 10', 'Klöver 5']  
random.shuffle(kortlek)  
print(f"Blandad kortlek: {kortlek}")
```
Användningsområde: Användbart inom spelutveckling eller testscenarier där du vill skapa en slumpmässig ordning på en mängd objekt, som att blanda en kortlek eller slumpa ordningen på frågor i ett quiz.

---

### Exempel på användning:
Låt oss säga att vi vill skapa ett program som låter användaren gissa ett slumpmässigt tal mellan 1 och 100. Vi kan använda `random.randint` för att generera talet och sedan låta användaren försöka gissa det.
```
slumptal = random.randint(1, 100)  
gissning = int(input("Gissa ett tal mellan 1 och 100: "))  
if gissning == slumptal:  
    print("Rätt gissat!")  
else:  
    print(f"Fel, det rätta talet var {slumptal}")
```
---

### Användningsområden:
- **Spelutveckling**: I spel behövs ofta slumpmässiga element som tärningskast, kortdragning, eller tilldelning av bonusar och vapen. `random`-modulen används för att skapa den variationen som gör spelet intressant och oförutsägbart.
- **Testdata och simuleringar**: Slumpmässiga tal används ofta för att skapa testdata för simuleringar och för att testa program under olika scenarier. Till exempel kan du skapa ett stort antal slumpmässiga fall för att säkerställa att ditt program hanterar alla möjliga indata korrekt.
- **Slumpmässiga urval**: Om du bygger applikationer som kräver slumpmässigt urval, såsom quiz-applikationer, lottdragning, eller beslutstagande baserat på olika alternativ, är `random.choice` ett enkelt och effektivt verktyg.
- **Säkerhet och lösenordsgenerering**: Du kan använda `random` för att skapa unika ID:n, lösenord, eller API-nycklar genom att kombinera slumpmässiga tecken och tal.

---

### Sammanfattning:
`random`-modulen ger dig de verktyg du behöver för att införa osäkerhet och slumpmässighet i ditt program. Med funktioner som `random.random()`, `random.randint()`, `random.choice()` och `random.shuffle()` kan du skapa spel, simuleringar, testdata och mycket mer. Genom att förstå och använda dessa funktioner effektivt kan du skapa mer dynamiska och engagerande applikationer.

---
## `re`-biblioteket: Arbeta med reguljära uttryck (regex)

`re`-modulen i Python erbjuder verktyg för att hantera och arbeta med reguljära uttryck (regex), som är kraftfulla mönster för att söka, bearbeta och validera text. Reguljära uttryck gör det möjligt att definiera komplexa sökningar och manipulationer av strängar, och används ofta i textanalys, dataextraktion och validering av indata. 

Att förstå och använda `re`-modulen kan spara mycket tid, särskilt när du arbetar med stora textdokument eller vill säkerställa att användarinmatning följer specifika mönster (som e-postadresser eller telefonnummer).

---

### Vanliga funktioner att känna till:

#### 1. `re.match(pattern, string)`
Denna funktion försöker matcha ett givet mönster i början av strängen. Om mönstret stämmer returneras ett matchobjekt; om det inte stämmer returneras `None`. `match()` är användbart när du behöver kontrollera om en sträng börjar med ett visst mönster, till exempel om ett dokument börjar med en specifik rubrik.

Exempel:
```
re.match(r'^Hejsan', 'Hejsan alla!')  
```
Returnerar en match eftersom strängen börjar med "Hejsan"

Användningsområde: Validera om en sträng börjar med ett visst prefix, eller när du arbetar med fasta format, som datum eller tid.

---

#### 2. `re.search(pattern, string)`
`search()` söker efter det första matchande mönstret någonstans i strängen, inte bara i början. Det returnerar ett matchobjekt om det hittar en träff, annars `None`. Detta är praktiskt om du vill hitta en specifik term eller ett mönster någonstans i texten, oavsett var det ligger.

Exempel:
```
re.search(r'alla', 'Hejsan alla!')  
```
Hittar "alla" någonstans i texten och returnerar en match.

Användningsområde: Söka efter nyckelord eller termer i större textdokument eller loggfiler där ordens position inte är känd i förväg.

---

#### 3. `re.findall(pattern, string)`
`findall()` returnerar alla träffar av mönstret som en lista. Om inga träffar hittas returneras en tom lista. Detta är idealiskt när du behöver extrahera alla förekomster av ett mönster i en text, som alla e-postadresser eller alla nummer i ett dokument.

Exempel:
```
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'Kontakta oss: test@mail.com, info@domain.se')  
```
Returnerar: ['test@mail.com', 'info@domain.se']

Användningsområde: Extrahera data, som e-postadresser, telefonnummer eller andra mönster som upprepas flera gånger i en text.

---

#### 4. `re.sub(pattern, repl, string)`
`sub()` ersätter alla förekomster av mönstret i strängen med den angivna ersättningssträngen `repl`. Det är ett kraftfullt verktyg för att göra massiva textändringar på ett enkelt och effektivt sätt, som att byta ut alla förekomster av ett felaktigt ord i en text eller ersätta känslig information som kreditkortsnummer.

Exempel:
```
text = "Min email är test@mail.com"  
updated_text = re.sub(r'\S+@\S+', '[email censurerad]', text)  
```
Resultat: 'Min email är [email censurerad]'

Användningsområde: Användbart när du vill ersätta eller censurera känslig information i en text, eller automatiskt formatera text.

---

### Exempel på användning:
Anta att vi har en text och vi vill hitta alla e-postadresser i den. Vi kan använda `re.findall()` för att hämta alla förekomster.
```
text = "Kontakta oss på support@domain.com eller sales@company.org."  
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  
emails = re.findall(email_pattern, text)  
print(f"Följande e-postadresser hittades: {emails}")
```
---

### Användningsområden:
- **Validering av användarinmatning**: Om du bygger ett webbformulär och behöver säkerställa att användare anger en korrekt e-postadress, kan du använda reguljära uttryck för att validera inmatningen.
- **Textbearbetning**: Bearbeta stora textdokument och söka efter specifika mönster, såsom sökord, meningar, eller symboler.
- **Dataextraktion**: Använd `re` för att extrahera relevant information från ostrukturerad text, som e-postadresser, telefonnummer, datum eller andra specifika mönster.
- **Textformatering**: Automatiskt ersätta eller formatera text, till exempel att censurera känslig information, korrigera stavfel eller ersätta vissa termer med mer lämpliga.

---

### Sammanfattning:
`re`-modulen i Python är ett ovärderligt verktyg för textbearbetning och validering av mönster i strängar. Med funktioner som `re.match()`, `re.search()`, `re.findall()` och `re.sub()` kan du enkelt och effektivt söka, manipulera och validera textdata. Oavsett om du arbetar med stora textfiler, validerar formulärdata, eller bearbetar rådata, erbjuder `re`-modulen en kraftfull lösning för att hantera text på en avancerad nivå.

---

## `json`-biblioteket: Arbeta med JSON-data

`json`-modulen i Python gör det enkelt att arbeta med JSON (JavaScript Object Notation), ett populärt format för att utbyta och lagra data i webbaserade applikationer. JSON används ofta för att skicka strukturerad data mellan klienter och servrar, eller för att lagra applikationsinställningar och användarpreferenser. `json`-modulen i Python erbjuder verktyg för att konvertera Python-objekt till JSON och vice versa, vilket gör att du enkelt kan hantera data i ett format som är lätt att arbeta med och förstå.

---

### Vanliga funktioner att känna till:

#### 1. `json.dumps(obj)`
`dumps()` tar ett Python-objekt (som en dictionary eller lista) och konverterar det till en JSON-sträng. Detta är användbart när du vill skicka eller lagra data som JSON men fortfarande vill arbeta med Python-objekt i ditt program.

Exempel:
```
data = {'namn': 'Alice', 'ålder': 25}  
json_data = json.dumps(data)  
print(f"JSON-sträng: {json_data}")
```
Användningsområde: När du behöver skicka Python-objekt som JSON-data över ett nätverk eller spara dem i en fil som text.

---

#### 2. `json.loads(s)`
`loads()` konverterar en JSON-sträng till ett Python-objekt, oftast en dictionary. Detta är praktiskt när du tar emot JSON-data, till exempel från en API-förfrågan, och vill bearbeta den som ett Python-objekt.

Exempel:
```
json_data = '{"namn": "Alice", "ålder": 25}'  
data = json.loads(json_data)  
print(f"Python-objekt: {data}")
```
Användningsområde: När du mottar JSON-data från en extern källa, som en webbserver, och behöver konvertera den till ett Python-objekt för att bearbeta den.

---

#### 3. `json.dump(obj, file)`
`dump()` skriver ett Python-objekt till en fil i JSON-format. Det här är användbart om du vill spara strukturerad data på disk i JSON-format, till exempel för att bevara användarinställningar eller applikationskonfigurationer.

Exempel:
```
data = {'namn': 'Alice', 'ålder': 25}  
with open('data.json', 'w') as fil:  
    json.dump(data, fil)
```
Användningsområde: Används när du vill lagra Python-objekt i JSON-format i filer, som konfigurationsfiler eller för att spara sessioner och användarinställningar.

---

#### 4. `json.load(file)`
`load()` läser in JSON-data från en fil och konverterar det till ett Python-objekt. Detta är användbart när du vill ladda in data från en fil som har sparats som JSON och bearbeta det i ditt program.

Exempel:
```
with open('data.json', 'r') as fil:  
    data = json.load(fil)  
print(f"Data från fil: {data}")
```
Användningsområde: När du behöver läsa in och använda data som tidigare sparats i en JSON-fil, till exempel användarkonfigurationer, inställningar eller sparade projekt.

---

### Exempel på användning:
Anta att vi vill spara en användares profiluppgifter i en JSON-fil och senare läsa tillbaka dem.

Spara användardata i JSON-format
```
anvandare = {'namn': 'Alice', 'ålder': 25, 'email': 'alice@mail.com'}  
with open('profil.json', 'w') as fil:  
    json.dump(anvandare, fil)

# Läs tillbaka data från filen

with open('profil.json', 'r') as fil:  
    anvandare_data = json.load(fil)  
print(f"Lästa användardata: {anvandare_data}")
```
---

### Användningsområden:
- **Kommunikation mellan klient och server**: JSON är standardformatet för att skicka data i webbapplikationer. När du bygger en applikation som kommunicerar med en API eller en server, är det vanligt att skicka och ta emot data i JSON-format.
- **Lagring av applikationsinställningar**: JSON-filer kan användas för att spara användarpreferenser eller inställningar som din applikation behöver komma ihåg mellan olika sessioner.
- **Konfigurationsfiler**: Många moderna applikationer använder JSON för att lagra konfigurationer, vilket gör det enkelt att läsa in och ändra inställningar utan att behöva omkompilera eller skriva om koden.
- **Serialisering av data**: Genom att konvertera Python-objekt till JSON kan du spara data i ett strukturerat format och återanvända det senare, till exempel när du sparar tillståndet för en applikation eller en session.

---

### Sammanfattning:
`json`-modulen i Python ger ett enkelt sätt att hantera JSON-data, vilket är ett av de mest använda formaten för datautbyte i moderna applikationer. Med funktioner som `json.dumps()`, `json.loads()`, `json.dump()`, och `json.load()` kan du enkelt konvertera mellan Python-objekt och JSON, spara data i filer och hantera datautbyte mellan klienter och servrar. JSON gör det enkelt att arbeta med strukturerad data på ett effektivt och standardiserat sätt.

---

## `collections`-biblioteket: Specialiserade datastrukturer

`collections`-modulen i Python tillhandahåller en uppsättning specialiserade datastrukturer som erbjuder mer funktionalitet och bättre prestanda än de inbyggda typerna som listor, tuples, och dictionaries. Dessa datastrukturer kan vara mycket användbara när du arbetar med specifika problem som kräver snabba insättningar och borttagningar, eller när du behöver en ordnad datastruktur med namngivna fält.

---

### Vanliga strukturer att känna till:

#### 1. `Counter`
`Counter` är en subclass av `dict` som används för att räkna hur många gånger varje element förekommer. Den returnerar en dictionary-liknande struktur där nycklarna är objekten som räknas och värdena är antalet förekomster.

Exempel:
```
text = "det var en gång en katt som hette Maja"  
ordlista = collections.Counter(text.split())  
print(ordlista)
```
Användningsområde: Perfekt för att räkna antalet förekomster av element, såsom ord i en text, händelser i en loggfil, eller objekt i en lista. Det används ofta inom statistik och analys där frekvens är viktig.

---

#### 2. `deque`
`deque` (dubbelriktad kö) är en datastruktur som tillåter snabb insättning och borttagning av element både från början och slutet. Det är idealiskt när du behöver implementera kö- eller stack-liknande beteende.

Exempel:
```
kö = collections.deque([1, 2, 3])  
kö.appendleft(0)  
kö.append(4)  
print(kö)
```
Användningsområde: `deque` används ofta i scenarier där du behöver hantera data i FIFO (First In, First Out) eller LIFO (Last In, First Out) ordning, såsom implementering av köer, buffers eller stacks.

---

#### 3. `namedtuple`
`namedtuple` är en tuple-liknande struktur där fälten har namn, vilket gör det lättare att referera till elementen än med vanliga numeriska index. Detta gör koden mer läsbar och förståelig.

Exempel:
```
Person = collections.namedtuple('Person', ['namn', 'ålder'])  
person = Person('Alice', 30)  
print(f"Namn: {person.namn}, Ålder: {person.ålder}")
```
Användningsområde: `namedtuple` är användbar när du vill organisera data på ett sätt som är lätt att förstå, exempelvis för att representera poster i en databas, koordinater i ett 3D-rum, eller andra komplexa dataenheter.

---

#### 4. `defaultdict`
`defaultdict` är en dictionary som låter dig ange en standardvärdesfunktion som tilldelas nycklar som inte finns i dictionaryn. Detta är praktiskt när du vill undvika att kontrollera om en nyckel finns innan du tilldelar ett värde.

Exempel:
```
nummer_lista = collections.defaultdict(int)  
nummer_lista['nyckel1'] += 1  
print(f"Värde för 'nyckel1': {nummer_lista['nyckel1']}")  
print(f"Värde för 'nyckel2': {nummer_lista['nyckel2']}")
```
Användningsområde: `defaultdict` används ofta när du bygger upp data strukturer där vissa nycklar kan saknas, till exempel vid räkning av objekt eller gruppering av data. Det förenklar koden genom att eliminera behovet av if-satser för att kontrollera om en nyckel redan existerar.

---

### Exempel på användning:
Anta att vi vill räkna hur många gånger varje ord förekommer i en text och sedan använda `defaultdict` för att bygga en lista av ord sorterade efter deras frekvens.
```
text = "det var en gång en katt som hette Maja"  
räkningar = collections.Counter(text.split())  
print(f"Ordens frekvens: {räkningar}")
```
---

### Användningsområden:
- **Räknare och statistik**: `Counter` kan användas för att analysera hur ofta något förekommer, till exempel ord i en text eller händelser i en loggfil.
- **Effektiva köer och stacks**: `deque` är ett utmärkt val när du behöver snabb åtkomst från både fram och bak av en datastruktur, till exempel vid implementering av köer eller stacks.
- **Namngivna tupler**: `namedtuple` gör det enklare att hantera data som har flera fält, till exempel en persons uppgifter eller data från en databas.
- **Hantering av standardvärden**: `defaultdict` kan förenkla din kod när du behöver hantera dictionaries med standardvärden och undvika fel när du arbetar med nycklar som kanske inte existerar.

---

### Sammanfattning:
`collections`-modulen ger dig kraftfulla och optimerade datastrukturer för att hantera olika problem effektivt. Med verktyg som `Counter`, `deque`, `namedtuple`, och `defaultdict` kan du bygga mer sofistikerade program och arbeta med stora datamängder på ett flexibelt och effektivt sätt. Genom att förstå när och hur du ska använda dessa strukturer kan du förbättra både prestanda och läsbarhet i dina Python-projekt.

---

## `logging`-biblioteket: Hantera loggning i Python

`logging`-modulen i Python erbjuder ett kraftfullt och flexibelt sätt att hantera loggning av händelser i dina program. Med `logging` kan du spåra viktiga händelser, fel och annan diagnostisk information under programmets körning. Det är ett mer robust alternativ än att använda `print()`, särskilt när du vill spåra vad som händer i produktion eller samla in statistik över körningen.

---

### Varför använda loggning?
Loggning ger flera fördelar, bland annat:
- **Informationsnivåer**: Du kan styra vilken nivå av information som ska loggas (exempelvis bara fel eller alla händelser).
- **Flexibilitet**: Loggar kan riktas till olika destinationer, som terminalen, filer eller till och med externa system.
- **Felsökning**: Du kan få detaljerad information om programmets körning utan att påverka prestandan eller produktionen.

---

### Nivåer av loggning
`logging`-modulen erbjuder olika nivåer av loggning, beroende på hur kritisk informationen är:
1. **DEBUG**: Detaljerad information för felsökning.
2. **INFO**: Generell information om programmets körning.
3. **WARNING**: Indikerar att något oväntat hände, men programmet kan fortsätta.
4. **ERROR**: Ett fel som hindrar normal körning av en viss del av programmet.
5. **CRITICAL**: Ett allvarligt fel som gör att programmet inte kan fortsätta.

---

### Grunderna i `logging`-modulen
För att använda loggning i Python behöver du konfigurera en logger. Den enklaste metoden är att använda `basicConfig()` för att snabbt komma igång med loggning.

Exempel på grundläggande loggning:
```
import logging  
logging.basicConfig(level=logging.INFO)  
logging.debug("Detta är en debug-logg")  
logging.info("Programmet startades korrekt")  
logging.warning("Detta är en varning")  
logging.error("Ett fel uppstod")  
logging.critical("Kritiskt fel: Programmet avbröts")
```
I detta exempel loggas information på `INFO`-nivå och högre, vilket innebär att `DEBUG`-meddelandet ignoreras eftersom loggnivån är satt till `INFO`.

---

### Logga till en fil
Du kan styra var loggmeddelandena ska skrivas, till exempel till en fil istället för terminalen. Detta görs med `basicConfig()` där du anger en fil som destination.

Exempel på att logga till en fil:
```
import logging  
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')  
logging.info("Detta loggas till en fil")
```
Här loggas alla meddelanden från `DEBUG` och uppåt till filen `app.log`. Varje loggmeddelande innehåller en tidstämpel, loggnivå och själva meddelandet.

---

### Logga till flera destinationer
En logger kan ha flera "handlers", vilket innebär att du kan logga till både terminalen och en fil samtidigt.

---

Exempel på att logga till både terminal och fil:
```
import logging  
logger = logging.getLogger('my_logger')  
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()  
console_handler.setLevel(logging.WARNING)

file_handler = logging.FileHandler('app.log')  
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
console_handler.setFormatter(formatter)  
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)  
logger.addHandler(file_handler)

logger.debug("Debugmeddelande loggas bara till fil")  
logger.warning("Varning loggas till både terminal och fil")  
logger.error("Fel loggas till både terminal och fil")
```
I detta exempel skrivs alla loggnivåer till filen `app.log`, medan bara varningar och högre loggas till terminalen.

---

### Exempel på användning:
Tänk dig att du bygger ett övervakningsprogram som loggar temperaturavläsningar. Du vill logga alla temperaturer men visa en varning när temperaturen överstiger en viss gräns.
```
import logging  
logging.basicConfig(level=logging.DEBUG, filename='temperatur.log', format='%(asctime)s - %(levelname)s - %(message)s')

temperatur = 75  
gräns = 70

logging.info(f"Nuvarande temperatur: {temperatur} grader")  
if temperatur > gräns:  
    logging.warning(f"Temperaturen {temperatur} överskrider gränsen på {gräns} grader")
```
---

### Användningsområden:
- **Felsökning**: Loggning ger detaljerad information under utveckling och produktion, vilket underlättar felsökning.
- **Övervakning**: Du kan använda loggning för att övervaka applikationer och samla in statistik över deras körning.
- **Felhantering**: Loggar hjälper dig att identifiera och åtgärda fel i realtid utan att krascha applikationen.
- **Statistik**: Genom att samla loggar kan du analysera hur programmet presterar och användarinteraktioner över tid.

---

### Sammanfattning:
`logging`-modulen är ett ovärderligt verktyg för att spåra och förstå vad som händer i ditt program under körning. Genom att använda olika loggnivåer och styra var loggar skrivs (till terminal eller fil), kan du hantera allt från enkel felsökning under utveckling till avancerad övervakning och analys av systemets körning i produktion.

---


### Uppgift 1: Arbeta med `os`-biblioteket

**Uppgift:** Skapa ett Python-program som listar alla filer i den aktuella katalogen och skapar en ny katalog som heter "backup".

**Instruktioner:**
1. Börja med att importera `os`-modulen. Denna modul ger tillgång till funktioner som låter dig interagera med operativsystemet.
2. Använd funktionen `os.getcwd()` för att hämta den aktuella arbetskatalogen. Detta innebär att du får den plats där programmet körs ifrån, till exempel din hemkatalog.
3. Använd funktionen `os.listdir()` för att lista alla filer och mappar i arbetskatalogen. Du kan spara resultatet i en variabel och sedan använda en for-loop för att skriva ut varje fil.
4. Använd funktionen `os.mkdir()` för att skapa en ny mapp. Ge mappen namnet "backup". Du kan kontrollera om mappen redan finns med hjälp av en `if`-sats och `os.path.exists()`.

---

### Uppgift 2: Arbeta med `sys.argv`

**Uppgift:** Skapa ett Python-program som tar emot ett filnamn som ett kommandoradsargument och skriver ut filens innehåll.

**Instruktioner:**
1. Börja med att importera `sys`-modulen. `sys.argv` är en lista där varje element representerar ett värde som skickas in via kommandoraden.
2. När du kör programmet via terminalen kan du skriva in `python program.py filnamn.txt`. Filnamnet kommer då att sparas i listan `sys.argv[]`, där index 0 alltid är namnet på programmet och index 1 är det första argumentet (filnamnet).
3. Hämta filnamnet från `sys.argv[1]` och spara det i en variabel.
4. Använd funktionen `open()` för att öppna filen. Läs filens innehåll och spara det i en variabel.
5. Skriv ut filens innehåll till skärmen med en for-loop som går igenom varje rad.
6. Avsluta med att stänga filen.

---

### Uppgift 3: Arbeta med `math`-biblioteket

**Uppgift:** Skapa ett Python-program som beräknar kvadratroten av ett tal som användaren anger.

**Instruktioner:**
1. Importera `math`-modulen, som innehåller funktioner för matematiska beräkningar.
2. Be användaren mata in ett tal med `input()`. Eftersom indata från användaren alltid är en sträng, behöver du konvertera det till ett tal med `float()`.
3. Använd funktionen `math.sqrt()` för att beräkna kvadratroten av talet och spara resultatet i en variabel.
4. Skriv ut resultatet till skärmen genom att kombinera en beskrivande text med det beräknade värdet.

---

### Uppgift 4: Arbeta med `datetime`-biblioteket

**Uppgift:** Skapa ett program som skriver ut dagens datum och tid samt räknar hur många dagar det är kvar till ett specifikt datum, till exempel julafton.

**Instruktioner:**
1. Importera `datetime`-modulen, som ger funktioner för att arbeta med datum och tid.
2. Använd funktionen `datetime.datetime.now()` för att hämta det aktuella datumet och tiden.
3. Skriv ut dagens datum och tid till skärmen.
4. Skapa ett datumobjekt för det specifika datumet (t.ex. julafton). Detta görs med `datetime.datetime(år, månad, dag)`. 
5. Beräkna skillnaden mellan dagens datum och det specifika datumet genom att subtrahera de två datumobjekten. Detta ger dig en `timedelta` som innehåller antalet dagar mellan datumen.
6. Skriv ut hur många dagar som är kvar till det specifika datumet.

---

### Uppgift 5: Arbeta med `random`-biblioteket

**Uppgift:** Skapa ett program som genererar ett slumpmässigt tal mellan 1 och 100, och låter användaren gissa talet.

**Instruktioner:**
1. Importera `random`-modulen, som används för att generera slumpmässiga tal.
2. Använd `random.randint(1, 100)` för att generera ett slumpmässigt tal mellan 1 och 100.
3. Be användaren gissa ett tal genom att använda `input()`.
4. Skapa en loop som fortsätter att be användaren gissa tills de gissar rätt. Använd en `while`-loop och en `if`-sats för att avgöra om användarens gissning är för hög, för låg eller korrekt.
5. När användaren gissar rätt, skriv ut ett gratulationsmeddelande och avsluta loopen.

---

### Uppgift 6: Arbeta med `re`-biblioteket

**Uppgift:** Skapa ett program som söker efter alla e-postadresser i en given text.

**Instruktioner:**
1. Importera `re`-modulen, som används för att arbeta med reguljära uttryck (regex).
2. Skapa en strängvariabel som innehåller text med flera e-postadresser och annan text.
3. Definiera ett regex-mönster för att hitta e-postadresser. Mönstret kan vara något i stil med `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`, som matchar en typisk e-postadress.
4. Använd `re.findall()` för att söka igenom strängen och spara alla e-postadresser i en lista.
5. Skriv ut listan med alla hittade e-postadresser till skärmen.

---

### Uppgift 7: Arbeta med `json`-biblioteket

**Uppgift:** Skapa ett program som sparar användarinformation (namn och ålder) i en JSON-fil och sedan läser tillbaka informationen.

**Instruktioner:**
1. Importera `json`-modulen, som används för att arbeta med JSON-data.
2. Be användaren mata in sitt namn och sin ålder med `input()`.
3. Skapa en dictionary där du sparar namnet och åldern.
4. Använd `json.dump()` för att skriva dictionaryn till en fil. Ge filen ett lämpligt namn, till exempel `user_data.json`.
5. Läs tillbaka informationen från filen med `json.load()` och spara den i en ny variabel.
6. Skriv ut den återlästa informationen för att verifiera att den har sparats korrekt.

---

### Uppgift 8: Arbeta med `collections`-biblioteket

**Uppgift:** Skapa ett program som använder `Counter` för att räkna hur många gånger varje ord förekommer i en given text.

**Instruktioner:**
1. Importera `collections`-modulen och använd klassen `Counter`.
2. Skapa en strängvariabel som innehåller en längre text.
3. Dela upp texten i en lista av ord med hjälp av funktionen `split()`.
4. Använd `Counter` för att räkna hur många gånger varje ord förekommer i listan.
5. Skriv ut resultatet, som kommer att visa varje ord och antalet gånger det förekommer.

---

### Uppgift 9: Arbeta med `logging`-biblioteket

**Uppgift:** Skapa ett Python-program som loggar olika meddelanden baserat på olika situationer (information, varningar och fel).

**Instruktioner:**
1. Börja med att importera `logging`-modulen, som ger funktioner för att logga meddelanden i programmet.
2. Konfigurera en grundläggande loggning med hjälp av `logging.basicConfig()`. Du kan ange loggnivå och format så att du får tydliga och strukturerade loggar. Till exempel kan du logga med tidstämpel och loggnivå.
3. Använd `logging.info()` för att logga informationsmeddelanden. Exempelvis när en uppgift har slutförts framgångsrikt.
4. Använd `logging.warning()` för att logga varningar, till exempel när ett program körs med felaktiga eller oväntade värden men fortfarande kan fortsätta köra.
5. Använd `logging.error()` för att logga felmeddelanden, till exempel när ett undantag fångas eller när ett fel uppstår som påverkar programmets funktionalitet.
6. Testa att köra ditt program flera gånger och se hur de olika loggnivåerna visas i konsolen.
