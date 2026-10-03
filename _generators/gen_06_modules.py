import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import make_nb

theorie = [
    ("md", """# 06. Modules

Een **module** is een bestand (of bibliotheek) met Python-code dat je kan **importeren** en hergebruiken. Python scheept standaard met een enorme **standaardbibliotheek** ("batteries included"), en met `pip` installeer je er nog duizenden pakketten bij.

> 🎯 **Waarom?** Je hoeft het wiel niet opnieuw uit te vinden. Wil je random getallen, datums, bestanden of wiskunde — iemand heeft dat al geschreven. Je leert hier hoe je die kracht aanzet.
"""),
    ("md", """## 1. Importeren

Er zijn drie manieren om een module te importeren:
"""),
    ("code", """# 1) hele module importeren
import math
print(math.sqrt(16))   # 4.0

# 2) een specifieke functie importeren
from math import pi
print(pi)              # 3.14159...

# 3) met een alias (afkorting)
import random as rnd
print(rnd.randint(1, 6))"""),
    ("md", """> 💡 **Stijlregel**: importeer modules bovenaan je bestand, netjes gegroepeerd. Dat houdt de code leesbaar en helpt anderen zien waarvan je code afhangt.
"""),
    ("md", """## 2. De standaardbibliotheek

Python heeft tientallen ingebouwde modules. De belangrijkste voor dit semester:

| Module | Waarvoor | Voorbeeld |
|--------|----------|-----------|
| `math` | Wiskunde | `math.sqrt(9)` → 3.0 |
| `random` | Willekeur | `random.randint(1, 6)` |
| `datetime` | Datum & tijd | `datetime.date.today()` |
| `os` | Bestandssysteem & paden | `os.path.join(...)` |
| `json` | JSON lezen/schrijven | `json.dumps(...)` |
| `csv` | CSV-bestanden | `csv.reader(...)` |
"""),
    ("md", """### 2.1 `math`
"""),
    ("code", """import math

print(math.pi)          # 3.141592653589793
print(math.sqrt(25))    # 5.0
print(math.ceil(2.1))   # 3  (naar boven afronden)
print(math.floor(2.9))  # 2  (naar beneden afronden)
print(math.factorial(5))  # 120"""),
    ("md", """### 2.2 `random`
"""),
    ("code", """import random

print(random.random())          # float tussen 0 en 1
print(random.randint(1, 6))     # geheel getal tussen 1 en 6
print(random.choice(["kop", "munt"]))  # willekeurig element
print(random.shuffle([1, 2, 3]))  # let op: shuffle geeft None!"""),
    ("md", """> ⚠️ **Gotcha**: `random.shuffle(lijst)` schudt de lijst **in-place** en geeft `None` terug (net zoals `list.sort()`). Bewaar dus geen retourwaarde.
"""),
    ("md", """### 2.3 `datetime`
"""),
    ("code", """from datetime import date, datetime

vandaag = date.today()
print(vandaag)
print(vandaag.year, vandaag.month, vandaag.day)

nu = datetime.now()
print(nu.strftime("%d/%m/%Y %H:%M"))  # opmaken als string"""),
    ("md", """### 2.4 `os`
"""),
    ("code", """import os

print(os.getcwd())              # huidige werkmap
print(os.listdir("."))          # inhoud van de map

pad = os.path.join("data", "muziek.csv")
print(pad)"""),
    ("md", """### 2.5 `json`
"""),
    ("code", """import json

# Python dict → JSON-string
data = {"naam": "Lotte", "leeftijd": 21}
tekst = json.dumps(data)
print(tekst)  # {"naam": "Lotte", "leeftijd": 21}

# JSON-string → Python dict
terug = json.loads(tekst)
print(terug["naam"])  # Lotte"""),
    ("md", """## 3. Externe pakketten (pip)

Niet alles zit in de standaardbibliotheek. Met `pip` installeer je externe pakketten zoals `pandas`, `requests`, `matplotlib`.

```bash
pip install pandas requests matplotlib
```

Daarna importeer je ze gewoon zoals een ingebouwde module:
"""),
    ("code", """# import pandas as pd   # hoort bij hoofdstuk 7
# import requests       # om API's aan te spreken
"""),
    ("md", """## 4. Je eigen module maken

Elke `.py`-bestand is al een module. Maak bv. een bestand `mijn_tools.py` met functies, en importeer het.
"""),
    ("code", """# Stel: je hebt een bestand 'mijn_tools.py' met:
# def verdubbel(n):
#     return n * 2
#
# Dan importeer je het zo:
# import mijn_tools
# print(mijn_tools.verdubbel(4))
"""),
    ("md", """> ⚠️ **Gotcha**: Python zoekt modules in de huidige map en in `sys.path`. Staat je `.py`-bestand ergens anders, dan wordt het niet gevonden.
"""),
    ("md", """## 5. `if __name__ == "__main__"`

Vaak zie je onderaan een script dit blok. Het zorgt dat code **alleen** draait wanneer het bestand direct wordt uitgevoerd, en *niet* wanneer het als module geïmporteerd wordt.
"""),
    ("code", """def hoofd():
    print("Script draait!")

if __name__ == "__main__":
    hoofd()
"""),
    ("md", """## 6. Samenvatting

- **`import module`** → `module.functie()`.
- **`from module import naam`** → direct `naam()`.
- **`import module as alias`** → korte naam.
- **Standaardbibliotheek**: `math`, `random`, `datetime`, `os`, `json`, `csv`, ...
- **Externe pakketten** installeer je met `pip install`.
- Je eigen `.py`-bestand is automatisch een module.
"""),
]

oef = [
    ("md", """# 06 - Oefeningen (Modules)

* Maak deze oefeningen zelfstandig; ze worden klassikaal behandeld.
* 🔥 Modules zijn waar Python écht "batteries included" wordt — hier bouw je al echte kleine tools.
"""),
    ("md", """#### Oefening 1 — Dobbelsteen
Gebruik `random.randint` om 10 keer met een dobbelsteen te gooien en print elke worp.
"""),
    ("code", """import random
"""),
    ("md", """#### Oefening 2 — Wachtwoordgenerator
Genereer een "wachtwoord" van 8 willekeurige karakters uit een string met letters en cijfers. Gebruik `random.choice` in een lus (of een list comprehension).
"""),
    ("code", """import random, string

karakters = string.ascii_letters + string.digits
"""),
    ("md", """#### Oefening 3 — Wie betaalt de rekening?
Kies met `random.choice` wie van een lijst vrienden de rekening betaalt. Druk af: `"X betaalt de rekening!"`.
"""),
    ("code", """import random

vrienden = ["Ana", "Bob", "Carol", "Dave", "Erin"]
"""),
    ("md", """#### Oefening 4 — Cirkel-math
Vraag een straal in en bereken met `math` de **omtrek** (2·π·r) en **oppervlakte** (π·r²). Print beide met 2 decimalen.
"""),
    ("code", """import math

straal = float(input("Straal? "))
"""),
    ("md", """#### Oefening 5 — Verjaardag aftellen
Gebruik `datetime` om te berekenen hoeveel dagen er nog zijn tot je volgende verjaardag (of tot Nieuwjaar). Gebruik `date.today()`.
"""),
    ("code", """from datetime import date

# vandaag = date.today()
# doel = date(2027, 1, 1)
"""),
    ("md", """#### Oefening 6 — JSON roundtrip
Maak een dict met je eigen profiel (naam, leeftijd, stad). Zet hem om naar JSON met `json.dumps`, en daarna terug naar een dict met `json.loads`. Print beide.
"""),
    ("code", """import json

profiel = {"naam": "...", "leeftijd": 0, "stad": "..."}
"""),
    ("md", """#### Oefening 7 — Map-verkenner met `os`
Gebruik `os` om de huidige werkmap af te drukken en alle bestanden erin op te lijsten. (Bonus: toon enkel de `.ipynb`-bestanden.)
"""),
    ("code", """import os

# print(os.getcwd())
# print(os.listdir("."))
"""),
    ("md", """#### Oefening 8 — Shuffle gotcha
Deze code bevat een klassieke fout. Leg uit wat er misgaat en corrigeer.
"""),
    ("code", """import random

kaarten = ["A", "K", "Q", "J"]
geschud = random.shuffle(kaarten)
print(geschud)  # wat wordt hier afgedrukt?
"""),
    ("md", """#### Oefening 9 — Alias-stijl
Importeer `datetime` en `random` met een alias en gebruik beide om een "willekeurige datum" in december van dit jaar te genereren.
"""),
    ("code", """import datetime as dt
import random as rnd
"""),
    ("md", """#### Oefening 10 — Eigen module schrijven
Maak in dezelfde map een bestand `mijn_tools.py` met een functie `verdubbel(n)` en `begroet(naam)`. Importeer het hier en test beide functies.
"""),
    ("code", """# import mijn_tools
# print(mijn_tools.verdubbel(4))
"""),
    ("md", """#### Oefening 11 — `if __name__ == "__main__"`
Schrijf een klein script met een functie `hoofd()` en het `if __name__ == "__main__":`-blok. Leg in een comment uit wanneer `hoofd()` wordt uitgevoerd.
"""),
    ("code", """def hoofd():
    pass  # vul in

# if __name__ == "__main__":
"""),
    ("md", """#### Oefening 12 — Lotto-simulator
Gebruik `random.sample` om 6 unieke getallen te trekken uit 1–45. Sorteer ze en print je "lottobiljet".
"""),
    ("code", """import random

# getallen = random.sample(range(1, 46), 6)
"""),
]

make_nb("06-modules/theorie.ipynb", theorie)
make_nb("06-modules/oefeningen.ipynb", oef)
