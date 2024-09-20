---
marp: true
paginate: true
theme: distansakademin
class: lead gaia
---

<h1 class="center-text">Webbapplikationer med realtidskommunikation i .NET och C#</h1>

<h2 class="center-text">Bygg en chatt med .NET, C# och SignalR</h2>

---

## Förutsättningar

1. Installera .NET SDK: Gå till <https://dotnet.microsoft.com/download> och hämta den senaste versionen av .NET SDK för ditt operativsystem.
2. Installera Visual Studio (valfritt): För att underlätta utvecklingen kan du använda Visual Studio IDE. Du kan ladda ner Visual Studio Community Edition gratis från <https://visualstudio.microsoft.com/downloads/>.

![bg left:23% 80%](./demo-img.png)

---

## Steg 1: Skapa ett nytt .NET-projekt

Öppna en terminal (eller kommandotolk) och skriv följande kommando för att skapa ett nytt ASP.NET-webbprojekt:

```bash
dotnet new web -n RealTimeChatApp
cd RealTimeChatApp
```

![bg left:23% 80%](./demo-img.png)
