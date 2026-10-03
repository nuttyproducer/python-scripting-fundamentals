import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import make_nb

# ---------------------------------------------------------------------------
# 01. Getting started — theorie
# ---------------------------------------------------------------------------
theorie = [
    ("md", """# 01. Getting Started

Welkom bij het vak **Scripting Essentials**! Voor we echte code schrijven, zetten we eerst je omgeving klaar. Dit hoofdstuk legt uit hoe je Python en Jupyter notebook installeert en gebruikt.

> 🎯 **Waarom dit hoofdstuk?** Een slecht geïnstalleerde omgeving is de nr. 1 reden waarom beginners vastlopen vóór ze ook maar één regel code schrijven. 10 minuten hier bespaart je uren frustratie later.
"""),
    ("md", """## 1. Installatie van Python

### 1.1 Python downloaden
1. Ga naar [python.org/downloads](https://python.org/downloads) en download de nieuwste stabiele versie (momenteel **Python 3.12** of hoger).
2. **Windows**: vink tijdens de installatie **"Add Python to PATH"** aan. Dit is cruciaal — zonder dit kan je Python niet aanroepen vanaf de command line.
3. **macOS / Linux**: Python is meestal al aanwezig. Controleer met `python3 --version`.

### 1.2 Versie controleren
Open een terminal (PowerShell op Windows, Terminal op macOS) en typ:
"""),
    ("code", """python --version
# of op sommige systemen:
# python3 --version
"""),
    ("md", """Verwacht iets zoals `Python 3.12.4`.

> ⚠️ **Opgelet (Windows)**: als `python` niet gevonden wordt, probeer dan `py`. De `py`-launcher wordt automatisch met Python geïnstalleerd en is de betrouwbaarste manier om Python te starten op Windows.
"""),
    ("md", """### 1.3 Een virtuele omgeving (venv)

Een **virtuele omgeving** is een geïsoleerde "sandbox" per project. Zo kan project A versie 1 van een library gebruiken en project B versie 2, zonder conflicten. In de industrie is dit de absolute standaard.
"""),
    ("code", """# Windows (PowerShell)
python -m venv .venv
.venv\\Scripts\\activate

# macOS / Linux
# python3 -m venv .venv
# source .venv/bin/activate
"""),
    ("md", """Na activatie zie je `(.venv)` vooraan je prompt. Alles wat je nu installeert met `pip`, blijft netjes binnen dit project.

### 1.4 Pakketten installeren met pip

`pip` is de pakketbeheerder van Python. Een pakket (of "library") is code die iemand anders schreef en die jij kan hergebruiken.
"""),
    ("code", """pip install jupyter notebook pandas matplotlib seaborn"""),
    ("md", """- **jupyter / notebook** → de omgeving waar je nu in werkt
- **pandas** → datamanipulatie (hoofdstuk 7)
- **matplotlib / seaborn** → visualisatie (hoofdstuk 7)
"""),
    ("md", """## 2. Jupyter Notebook

### 2.1 Wat is Jupyter Notebook?
Een **notebook** is een document dat **code** en **uitleg (markdown)** combineert in één bestand. Je kan code in stukjes ("cellen") uitvoeren en meteen het resultaat zien. Ideaal om te leren, te experimenteren en data te verkennen.

**Waar wordt het in het echte leven gebruikt?** Datascientists bij Netflix, Spotify en banken gebruiken Jupyter dagelijks om data te verkennen vóór ze productiecode schrijven. Zelfs bij OpenAI en Google start veel ML-onderzoek in een notebook.

### 2.2 Jupyter starten
"""),
    ("code", """# In je terminal (met je venv geactiveerd):
# jupyter notebook

# Of de modernere variant:
# jupyter lab
"""),
    ("md", """### 2.3 De twee soorten cellen

| Type | Doel | Voorbeeld |
|------|------|-----------|
| **Code cell** | Python uitvoeren | `print("Hallo")` |
| **Markdown cell** | Uitleg, titels, notities | `# Dit is een titel` |

### 2.4 Cellen uitvoeren

- **Shift + Enter** → voer de huidige cel uit en ga naar de volgende
- **Ctrl + Enter** → voer de huidige cel uit en blijf staan
- **A / B** → nieuwe cel toevoegen **boven** (A) of **onder** (B)
- **M / Y** → huidige cel omzetten naar **markdown** (M) of **code** (Y)
- **D D** → cel verwijderen
"""),
    ("md", """### 2.5 Je eerste code

Probeer het zelf: voer de cel hieronder uit met **Shift + Enter**.
"""),
    ("code", """print("Hello, world!")"""),
    ("md", """### 2.6 Magische commando's

Notebooks hebben speciale commando's die met `%` of `%%` beginnen. De twee die je echt moet kennen:
"""),
    ("code", """# %time meet hoe lang een commando duurt
%time 123456789 * 987654321
"""),
    ("code", """# %who toont alle variabelen die nu bestaan
x = 42
y = "hey"
%who
"""),
    ("md", """## 3. Samenvatting

- **Installeer** Python met "Add to PATH" aangevinkt (Windows).
- **Gebruik een venv** per project — zo hou je afhankelijkheden proper.
- **Jupyter notebook** combineert code + uitleg in cellen.
- **Shift + Enter** voert een cel uit.
- **Markdown** voor uitleg, **code** voor Python.
"""),
]

# ---------------------------------------------------------------------------
# 01. Getting started — oefeningen
# ---------------------------------------------------------------------------
oef = [
    ("md", """# 01 - Oefeningen

* Deze oefeningen maak je zelfstandig.
* Ze worden klassikaal behandeld, niet individueel verbeterd.
* 🔥 Elke oefening heeft een modern "waarom" — zo zie je meteen waarvoor je dit in het echte leven gebruikt.
"""),
    ("md", """#### Oefening 1 — Versie-check
Open een terminal en controleer welke Python-versie je hebt. Noteer het volledige versienummer.
"""),
    ("code", """# Voer dit uit in je TERMINAL (niet hier):
# python --version
# python -m pip --version
"""),
    ("md", """#### Oefening 2 — Jouw eerste venv
Maak een virtuele omgeving voor dit project en activeer ze.
"""),
    ("code", """# Windows (PowerShell):
# python -m venv .venv
# .venv\\Scripts\\activate

# macOS / Linux:
# python3 -m venv .venv
# source .venv/bin/activate
"""),
    ("md", """#### Oefening 3 — Pakketten installeren
Installeer met `pip` de pakketten die je dit semester nodig hebt. Controleer achteraf met `pip list` dat ze er staan.
"""),
    ("code", """# pip install jupyter notebook pandas matplotlib seaborn
# pip list
"""),
    ("md", """#### Oefening 4 — Je eerste markdown-cel
Voeg **boven** deze cel een nieuwe markdown-cel toe (toets **A**) en schrijf erin:
- Een titel (met `#`)
- Een bolletjeslijst met 3 dingen die je dit semester wil leren
"""),
    ("md", """#### Oefening 5 — Spiergeheugen voor shortcuts
Zet de juiste shortcut naast elke actie:

| Actie | Shortcut |
|-------|----------|
| Cel uitvoeren en naar volgende | |
| Cel uitvoeren en blijven | |
| Nieuwe cel boven | |
| Cel naar markdown | |
| Cel naar code | |
| Cel verwijderen | |
"""),
    ("md", """#### Oefening 6 — Je eerste programma
Voer onderstaande cel uit met **Shift + Enter**. Zie je "Hello, world!" onder de cel verschijnen? Pas de tekst aan en voer de cel opnieuw uit.
"""),
    ("code", """print("Hello, world!")
"""),
    ("md", """#### Oefening 7 — Een variabele en concatenatie
Maak een variabele `naam` met jouw naam. Druk daarna "Goeiedag " gevolgd door je naam af met het plusteken (`+`). Vergeet de spatie niet.
"""),
    ("code", """naam = "..."  # vervang door jouw naam

print("Goeiedag " + naam)
"""),
    ("md", """#### Oefening 8 — Eenvoudig rekenen
Maak twee variabelen `getal1` en `getal2`, tel ze op in een derde variabele `getal3`, en druk `getal3` af. Probeer daarna ook een aftrekking en een vermenigvuldiging.
"""),
    ("code", """getal1 = 5
getal2 = 3
getal3 = getal1 + getal2

print(getal3)
"""),
]

make_nb("01-getting-started/theorie.ipynb", theorie)
make_nb("01-getting-started/oefeningen.ipynb", oef)
