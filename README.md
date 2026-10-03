# Scripting Essentials — Python Oefenproject

Volledige cursus **Python** met theorie, oefeningen en mini-projecten per onderwerp. Alles is **chronologisch** opgebouwd: elk hoofdstuk gebruikt alleen wat je op dat moment al geleerd hebt.

> 🎯 **Waarvoor dient dit?** Dit is jouw leeromgeving om Python te leren zoals het in het echte leven gebruikt wordt. Geen droge theorie, maar moderne, herkenbare scenario's — van crypto-portfolio's en streamer-uitbetalingen tot wachtwoordgenerators en data-analyse. Je leert door te **doen**: eerst theorie lezen, dan oefenen, en tot slot een écht programma bouwen.

## 🚀 Aan de slag

1. **Installeer Python** (3.10 of hoger) van [python.org](https://python.org) — vink op Windows **"Add Python to PATH"** aan.
2. **Kloon of download** deze repository en open de map in je editor (bv. VS Code).
3. **Installeer de pakketten** die je nodig hebt:
   ```bash
   pip install jupyter pandas matplotlib seaborn
   ```
4. **Open de mappen in volgorde** (01 → 07) en start met het theorie-notebook:
   ```bash
   jupyter notebook
   ```

## 🧭 Hoe pak je dit aan?

Elk hoofdstuk volgt dezelfde drie stappen — doe ze **in deze volgorde**:

1. **📖 Lees de theorie** en voer de voorbeeldcellen zelf uit.
2. **✏️ Maak de oefeningen** in het `oefeningen.ipynb`-notebook.
3. **🛠️ Bouw de projecten** in `projecten/`: los de TODO's op in `main.py` en check daarna je werk met `oplossing.py`.

> ⚠️ **Belangrijk**: de volgorde is geen toeval. Alles bouwt op elkaar voort — sla geen hoofdstukken over, en gebruik in je oplossing geen concepten die je nog niet gezien hebt.

## 📚 Onderwerpen & projecten

| # | Onderwerp | Map | Projecten |
|---|-----------|-----|-----------|
| 1 | Getting Started | [`01-getting-started`](01-getting-started) | `hallo-app` |
| 2 | Python Basics | [`02-python-basics`](02-python-basics) | `crypto-calculator`, `streamer-payout`, `rekening-splitter` |
| 3 | Controlestructuren | [`03-controlestructuren`](03-controlestructuren) | `atm-simulator`, `casino-age-gate`, `gok-odds-calculator` |
| 4 | Containers | [`04-containers`](04-containers) | `playlist-manager`, `crypto-portfolio-tracker`, `follower-analyzer` |
| 5 | Functies | [`05-functies`](05-functies) | `creator-commissie`, `meme-generator`, `bestelsysteem`, `ascii-naamkaart` |
| 6 | Modules | [`06-modules`](06-modules) | `wachtwoordgenerator`, `quiz-game`, `json-todo`, `dev-check` |
| 7 | Data Manipulatie | [`07-data-manipulatie`](07-data-manipulatie) | `streaming-analyzer`, `budget-tracker`, `crypto-plotter` |

### 🔍 De projecten in één oogopslag

| Project | Hoofdstuk | Wat bouw je? |
|---------|-----------|--------------|
| `hallo-app` | 1 | Je eerste programma: tekst samenvoegen + rekenen |
| `crypto-calculator` | 2 | De waarde van je crypto-portfolio |
| `streamer-payout` | 2 | Bruto → netto inkomsten van een streamer |
| `rekening-splitter` | 2 | De rekening eerlijk verdelen onder vrienden |
| `atm-simulator` | 3 | Een geldautomaat met PIN en menu |
| `casino-age-gate` | 3 | Een toegangscheck op leeftijd + zelfuitsluiting |
| `gok-odds-calculator` | 3 | Kans en uitbetaling uit bookmaker-odds |
| `playlist-manager` | 4 | Je eigen playlist beheren |
| `crypto-portfolio-tracker` | 4 | Je munten bijhouden in een dictionary |
| `follower-analyzer` | 4 | Volgers op twee platformen vergelijken |
| `creator-commissie` | 5 | Netto inkomsten per platform |
| `meme-generator` | 5 | ASCII-memes maken |
| `bestelsysteem` | 5 | Een mini-webshop met validatie |
| `ascii-naamkaart` | 5 | Een kader rond je profiel |
| `wachtwoordgenerator` | 6 | Veilige wachtwoorden genereren |
| `quiz-game` | 6 | Een quiz met score en timer |
| `json-todo` | 6 | Taken bewaren in een JSON-bestand |
| `dev-check` | 6 | Je Python-omgeving controleren |
| `streaming-analyzer` | 7 | Streamer-data doorgronden met pandas |
| `budget-tracker` | 7 | Je uitgaven visualiseren |
| `crypto-plotter` | 7 | Een prijsgrafiek tekenen |

## 📁 Projecten (mini-apps)

Elke topic-map bevat een `projecten/`-map met **zelfstandige mini-programma's** — geen notebooks, maar echte `.py`-apps met een moderne use case.

> 🖥️ **Alles draait in de terminal.** Je start een project met `python main.py`; het programma leest invoer met `input()` en toont uitvoer met `print()`. Er komt **geen** grafische interface (GUI) aan te pas — bewust zo, om de focus op de code zelf te houden.

Elk project heeft:

```
<onderwerp>/projecten/<naam>/
    info.md       ← opdracht, "waarom", tips en uitdaging
    main.py       ← starter met TODO-stubs (vul zelf in)
    oplossing.py  ← volledige uitwerking (om te checken)
```

Voorbeeld: `python 03-controlestructuren/projecten/atm-simulator/oplossing.py`.

> 🔒 De oplossingen staan apart, zodat je eerst zelf kan proberen en daarna pas spiekt.

## 📊 Dataset

In [`07-data-manipulatie/data/streams.csv`](07-data-manipulatie/data) staat een fictieve dataset van streamers (naam, maand, views, abonnees, donaties) voor de oefeningen en projecten van hoofdstuk 7.

## 📝 Notities

- De `_generators/`-map bevat de scripts waarmee alle notebooks gegenereerd zijn. Wil je iets aanpassen, pas je de generator aan en voer je hem opnieuw uit (bv. `python _generators/gen_04_containers.py`).
- Vereist **Python 3.10+** (voor `match`-`case` in hoofdstuk 3).
- Installeer de nodige pakketten: `pip install jupyter pandas matplotlib seaborn`.
