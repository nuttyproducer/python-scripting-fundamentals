import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import make_nb, ROOT

# ---------------------------------------------------------------------------
# Sample dataset (also written as a real CSV so students can practice reading)
# ---------------------------------------------------------------------------
CSV_TEXT = """naam,maand,views,abonnees,donaties
NoraPlays,Jan,1250000,850000,1240
NoraPlays,Feb,1380000,912000,1500
PietGaming,Jan,430000,12000,88
PietGaming,Feb,410000,13500,92
ZoeStreams,Jan,2400000,2400000,9800
ZoeStreams,Feb,2650000,2500000,11200
YassineVlogs,Jan,780000,340000,560
YassineVlogs,Feb,820000,355000,610
LotteTech,Jan,560000,210000,410
LotteTech,Feb,610000,225000,455
"""

bestanden = [
    ("md", """# 07. Data Manipulatie — Bestanden lezen & schrijven

Echte programma's werken met **data op schijf**: CSV-exports van Spotify, JSON-antwoorden van API's, XML-feeds van webshops. Dit notebook leert je bestanden lezen en schrijven in de drie belangrijkste formaten.

> 🎯 **Waarom?** Een streamer die zijn statistieken wil analyseren, een developer die een API aanspreekt, een analyst die een CSV binnenhaalt — allemaal lezen en schrijven ze bestanden.
"""),
    ("md", """## 1. Basis: bestanden openen met `open()`

Je opent een bestand met `open()`, doet er iets mee, en sluit het. De **veilige** manier is met een `with`-blok: Python sluit het bestand dan automatisch, ook bij een fout.
"""),
    ("code", """# Schrijven naar een bestand
with open("mijn_bestand.txt", "w", encoding="utf-8") as f:
    f.write("Hallo, wereld!\\n")
    f.write("Tweede regel\\n")

# Lezen van een bestand
with open("mijn_bestand.txt", "r", encoding="utf-8") as f:
    inhoud = f.read()

print(inhoud)"""),
    ("md", """### 1.1 De modi

| Modus | Betekenis |
|-------|-----------|
| `"r"` | lezen (default) |
| `"w"` | schrijven (overschrijft!) |
| `"a"` | toevoegen (append) |
| `"r+"` | lezen én schrijven |

> ⚠️ **Gotcha**: `"w"` **wist** de bestaande inhoud. Wil je toevoegen, gebruik `"a"`.
"""),
    ("md", """## 2. CSV-bestanden

**CSV** (Comma-Separated Values) is hét uitwisselingsformaat voor tabellen. Python heeft er een ingebouwde module voor: `csv`.
"""),
    ("code", """import csv

# Voorbeeld CSV-inhoud (in het echt lees je dit uit een bestand)
import io
voorbeeld = io.StringIO('naam,maand,views\\nNoraPlays,Jan,1250000\\nPietGaming,Jan,430000\\n')

reader = csv.DictReader(voorbeeld)   # elke rij als een dict
for rij in reader:
    print(rij["naam"], "→", rij["views"], "views")"""),
    ("md", """### 2.1 Een CSV-bestand lezen

In de map van dit project staat `data/streams.csv`. Zo lees je hem:
"""),
    ("code", """import csv

with open("data/streams.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for rij in reader:
        print(f"{rij['naam']} ({rij['maand']}): {rij['views']} views")"""),
    ("md", """### 2.2 Schrijven naar CSV
"""),
    ("code", """import csv

data = [
    {"naam": "Ana", "score": 95},
    {"naam": "Bob", "score": 88},
]

with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    velden = ["naam", "score"]
    writer = csv.DictWriter(f, fieldnames=velden)
    writer.writeheader()
    writer.writerows(data)
"""),
    ("md", """## 3. JSON-bestanden

**JSON** (JavaScript Object Notation) is het formaat van het web: API's, config-bestanden en web-apps gebruiken het. Het lijkt erg op Python dicts.
"""),
    ("code", """import json

# Python → JSON (string)
data = {"naam": "Lotte", "abonnees": 850000, "is_premium": True}
tekst = json.dumps(data, indent=2)
print(tekst)"""),
    ("code", """# JSON (string) → Python
json_tekst = '{"naam": "Lotte", "abonnees": 850000}'
terug = json.loads(json_tekst)
print(terug["naam"])  # Lotte"""),
    ("md", """### 3.1 JSON naar een bestand schrijven / lezen
"""),
    ("code", """import json

data = {"naam": "Lotte", "abonnees": 850000}

# schrijven
with open("profiel.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# lezen
with open("profiel.json", "r", encoding="utf-8") as f:
    geladen = json.load(f)

print(geladen)"""),
    ("md", """> ⚠️ **Gotcha**: `json.dumps()` geeft een **string**, `json.dump()` schrijft naar een **bestand**. Idem voor `loads()` (van string) vs `load()` (van bestand).
"""),
    ("md", """## 4. XML-bestanden

**XML** is ouder dan JSON, maar nog steeds overal aanwezig (RSS-feeds, config-bestanden, webshops). Python parst het met `xml.etree.ElementTree`.
"""),
    ("code", """import xml.etree.ElementTree as ET

xml_tekst = '''
<kanaal>
    <video titel="Ep 1" views="1200" />
    <video titel="Ep 2" views="3400" />
</kanaal>
'''

root = ET.fromstring(xml_tekst)
for video in root.findall("video"):
    print(video.get("titel"), "→", video.get("views"), "views")"""),
    ("md", """## 5. Welk formaat wanneer?

| Formaat | Typisch gebruik | Python-module |
|---------|------------------|----------------|
| **CSV** | spreadsheets, exports | `csv` |
| **JSON** | API's, web, config | `json` |
| **XML** | legacy-systemen, RSS | `xml.etree.ElementTree` |

## 6. Samenvatting

- **`with open(...) as f`** opent een bestand veilig (auto-close).
- **CSV** → `csv.DictReader` / `csv.DictWriter`.
- **JSON** → `json.load`/`dump` (bestand) en `loads`/`dumps` (string).
- **XML** → `xml.etree.ElementTree`.
- Altijd **`encoding="utf-8"`** meegeven.
"""),
]

pandas = [
    ("md", """# 07. Data Manipulatie — Pandas

**Pandas** is dé bibliotheek voor datamanipulatie in Python. Het werkt met **DataFrames**: tabellen met rijen en kolommen, net als een spreadsheet, maar dan programmeerbaar.

> 🎯 **Waarom?** Elke data-analist en datascientist gebruikt pandas. Het is de standaard om data in te laden, te filteren, te groeperen en te analyseren.
"""),
    ("md", """## 1. Installeren & importeren

```bash
pip install pandas
```

De conventie is om pandas als `pd` te importeren:
"""),
    ("code", """import pandas as pd"""),
    ("md", """## 2. Series en DataFrames

- Een **Series** is één kolom (een gelabelde lijst).
- Een **DataFrame** is een tabel van meerdere Series.
"""),
    ("code", """import pandas as pd

s = pd.Series([10, 20, 30], name="aantallen")
print(s)"""),
    ("code", """df = pd.DataFrame({
    "naam": ["Ana", "Bob", "Carol"],
    "leeftijd": [30, 24, 28],
    "stad": ["Gent", "Brussel", "Antwerpen"],
})
print(df)"""),
    ("md", """## 3. Data inladen

Pandas leest CSV's, JSON, Excel en meer in één regel:
"""),
    ("code", """import pandas as pd

df = pd.read_csv("data/streams.csv")
df"""),
    ("md", """## 4. Eerste kennismaking met je data
"""),
    ("code", """import pandas as pd
df = pd.read_csv("data/streams.csv")

print(df.head(3))       # eerste 3 rijen
print(df.shape)         # (aantal rijen, aantal kolommen)
print(df.dtypes)        # datatype per kolom
print(df["naam"].unique())  # unieke waarden in een kolom"""),
    ("md", """## 5. Kolommen selecteren
"""),
    ("code", """import pandas as pd
df = pd.read_csv("data/streams.csv")

print(df["views"])          # één kolom → Series
print(df[["naam", "views"]].head())  # meerdere kolommen → DataFrame"""),
    ("md", """## 6. Filteren (rijen selecteren op voorwaarde)
"""),
    ("code", """import pandas as pd
df = pd.read_csv("data/streams.csv")

grote = df[df["views"] > 1_000_000]
print(grote)"""),
    ("code", """# meerdere voorwaarden: gebruik & (and) en | (or), met haakjes!
conditie = (df["views"] > 500_000) & (df["donaties"] > 500)
print(df[conditie])"""),
    ("md", """> ⚠️ **Gotcha**: in pandas gebruik je **`&`** en **`|`**, niet `and`/`or`. En zet elke voorwaarde **tussen haakjes**.
"""),
    ("md", """## 7. Nieuwe kolommen maken
"""),
    ("code", """import pandas as pd
df = pd.read_csv("data/streams.csv")

# inkomsten per 1000 views (aanname: €3 per 1000 views)
df["inkomsten"] = df["views"] / 1000 * 3
print(df[["naam", "maand", "views", "inkomsten"]].head())"""),
    ("md", """## 8. Groeperen & aggregeren

`groupby` is de krachtigste feature: groepeer op een kolom en bereken statistieken.
"""),
    ("code", """import pandas as pd
df = pd.read_csv("data/streams.csv")

per_naam = df.groupby("naam")["views"].sum().sort_values(ascending=False)
print(per_naam)"""),
    ("code", """# meerdere statistieken tegelijk
overzicht = df.groupby("naam").agg({
    "views": "sum",
    "donaties": "mean",
})
print(overzicht)"""),
    ("md", """## 9. Nuttige snelle analyses
"""),
    ("code", """import pandas as pd
df = pd.read_csv("data/streams.csv")

print(df["views"].mean())     # gemiddelde
print(df["views"].max())      # maximum
print(df["views"].min())      # minimum
print(df.describe())          # samenvatting in één keer"""),
    ("md", """## 10. Sorteren
"""),
    ("code", """import pandas as pd
df = pd.read_csv("data/streams.csv")

df_sorted = df.sort_values("views", ascending=False)
print(df_sorted.head())"""),
    ("md", """## 11. Samenvatting

- **`pd.read_csv(...)`** laadt data in een DataFrame.
- **`df["kolom"]`** selecteert, **`df[conditie]`** filtert.
- **`df["nieuw"] = ...`** maakt een nieuwe kolom.
- **`df.groupby("kolom").agg(...)`** groepeert en aggregeert.
- Gebruik **`&` / `|`** met haakjes, niet `and`/`or`.
"""),
]

visualisatie = [
    ("md", """# 07. Data Manipulatie — Visualisatie

Een goede grafiek zegt meer dan duizend cijfers. **Matplotlib** is de basis-bibliotheek voor plots; **seaborn** bouwt erop voort met mooiere, statistische grafieken.

> 🎯 **Waarom?** Dashboards, jaarrapporten, speler-statistieken — data visualiseren is de laatste stap om inzichten écht te tonen.
"""),
    ("md", """## 1. Installeren & importeren

```bash
pip install matplotlib seaborn
```

De conventies:
"""),
    ("code", """import matplotlib.pyplot as plt
import seaborn as sns"""),
    ("md", """## 2. Je eerste plot met matplotlib
"""),
    ("code", """import matplotlib.pyplot as plt

jaren = [2020, 2021, 2022, 2023, 2024]
abonnees = [100, 250, 900, 2100, 5400]

plt.plot(jaren, abonnees, marker="o")
plt.title("Groei van abonnees")
plt.xlabel("Jaar")
plt.ylabel("Abonnees")
plt.show()"""),
    ("md", """## 3. Soorten plots

### 3.1 Staafdiagram (bar chart)
"""),
    ("code", """import matplotlib.pyplot as plt

platformen = ["YouTube", "Twitch", "TikTok"]
inkomsten = [4500, 2100, 3800]

plt.bar(platformen, inkomsten)
plt.title("Inkomsten per platform")
plt.show()"""),
    ("md", """### 3.2 Taartdiagram (pie chart)
"""),
    ("code", """import matplotlib.pyplot as plt

platformen = ["YouTube", "Twitch", "TikTok"]
inkomsten = [4500, 2100, 3800]

plt.pie(inkomsten, labels=platformen, autopct="%.1f%%")
plt.title("Aandeel per platform")
plt.show()"""),
    ("md", """### 3.3 Spreidingsdiagram (scatter) met seaborn
"""),
    ("code", """import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("data/streams.csv")
sns.scatterplot(data=df, x="views", y="donaties", hue="naam")
plt.title("Views vs. donaties")
plt.show()"""),
    ("md", """### 3.4 Histogram
"""),
    ("code", """import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("data/streams.csv")
sns.histplot(df["views"], bins=8)
plt.title("Verdeling van views")
plt.show()"""),
    ("md", """### 3.5 Boxplot — spreiding per groep
"""),
    ("code", """import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("data/streams.csv")
sns.boxplot(data=df, x="naam", y="views")
plt.title("Views per streamer")
plt.show()"""),
    ("md", """## 4. Je grafiek opslaan
"""),
    ("code", """import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.savefig("mijn_grafiek.png", dpi=150)
print("Grafiek opgeslagen als mijn_grafiek.png")"""),
    ("md", """## 5. Samenvatting

- **`plt.plot()`** → lijn, **`plt.bar()`** → staafjes, **`plt.pie()`** → taart.
- **`seaborn`** → `scatterplot`, `histplot`, `boxplot` (mooier & statistischer).
- Altijd **`plt.show()`** om te tonen, **`plt.savefig(...)`** om op te slaan.
- Titels en as-labels: `plt.title()`, `plt.xlabel()`, `plt.ylabel()`.
"""),
]

oef = [
    ("md", """# 07 - Oefeningen (Data Manipulatie)

* Maak deze oefeningen zelfstandig; ze worden klassikaal behandeld.
* 🔥 Je werkt met de fictieve dataset `data/streams.csv` — streamers en hun maandelijkse statistieken. Alsof je voor een creator-agency werkt.
"""),
    ("md", """#### Oefening 1 — CSV lezen met `csv`
Lees `data/streams.csv` met de `csv`-module en print elke rij als: `"<naam> had in <maand> <views> views"`.
"""),
    ("code", """import csv
"""),
    ("md", """#### Oefening 2 — Inladen met pandas
Laad `data/streams.csv` in een DataFrame en print de **eerste 5 rijen** en het **aantal rijen/kolommen**.
"""),
    ("code", """import pandas as pd
"""),
    ("md", """#### Oefening 3 — Filter de top
Filter alle rijen met meer dan **1.000.000 views** en print ze. Wie zijn de "grote" streamers?
"""),
    ("code", """import pandas as pd
df = pd.read_csv("data/streams.csv")
"""),
    ("md", """#### Oefening 4 — Nieuwe kolom: inkomsten
Maak een kolom `inkomsten` = views / 1000 * 3 (€3 per 1000 views). Toon naam, maand, views en inkomsten.
"""),
    ("code", """import pandas as pd
df = pd.read_csv("data/streams.csv")
"""),
    ("md", """#### Oefening 5 — Groepeer per streamer
Groepeer op `naam` en bereken de **totale views** per streamer, gesorteerd van hoog naar laag.
"""),
    ("code", """import pandas as pd
df = pd.read_csv("data/streams.csv")
"""),
    ("md", """#### Oefening 6 — Gemiddelde donaties
Wat is de **gemiddelde donatie** per streamer? Gebruik `groupby` met `agg` (kolom `donaties`, `mean`).
"""),
    ("code", """import pandas as pd
df = pd.read_csv("data/streams.csv")
"""),
    ("md", """#### Oefening 7 — Beschrijvende statistiek
Gebruik `df.describe()` en beantwoord: wat is de hoogste en laagste views-waarde in de dataset?
"""),
    ("code", """import pandas as pd
df = pd.read_csv("data/streams.csv")
"""),
    ("md", """#### Oefening 8 — Staafdiagram
Maak met matplotlib een staafdiagram van de **totale views per streamer** (tip: gebruik eerst `groupby`).
"""),
    ("code", """import pandas as pd
import matplotlib.pyplot as plt
"""),
    ("md", """#### Oefening 9 — Scatterplot met seaborn
Maak een scatterplot van `views` (x) tegen `donaties` (y), gekleurd per streamer.
"""),
    ("code", """import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
"""),
    ("md", """#### Oefening 10 — JSON schrijven en lezen
Bewaar je eigen "creator-profiel" (naam, abonnees, platformen) als JSON-bestand met `json.dump`, en lees het terug met `json.load`.
"""),
    ("code", """import json
"""),
    ("md", """#### Oefening 11 — XML parsen
Pars de onderstaande XML en print voor elk item de titel en prijs.
"""),
    ("code", """import xml.etree.ElementTree as ET

xml_tekst = '''
<winkel>
    <item naam="koptelefoon" prijs="89.99" />
    <item naam="muis" prijs="29.99" />
</winkel>
'''
"""),
    ("md", """#### Oefening 12 — End-to-end mini-rapport
Combineer alles: laad de CSV in pandas, groepeer per streamer de totale views, en maak er een **staafdiagram** van met een titel en as-labels. Sla de grafiek op als `rapport.png`.
"""),
    ("code", """import pandas as pd
import matplotlib.pyplot as plt

# 1) laad + groepeer
# 2) plot + save
"""),
]

# write notebooks + sample data
make_nb("07-data-manipulatie/theorie-bestanden.ipynb", bestanden)
make_nb("07-data-manipulatie/theorie-pandas.ipynb", pandas)
make_nb("07-data-manipulatie/theorie-visualisatie.ipynb", visualisatie)
make_nb("07-data-manipulatie/oefeningen.ipynb", oef)

(ROOT / "07-data-manipulatie" / "data").mkdir(parents=True, exist_ok=True)
(ROOT / "07-data-manipulatie" / "data" / "streams.csv").write_text(CSV_TEXT, encoding="utf-8")
print("wrote 07-data-manipulatie/data/streams.csv")
