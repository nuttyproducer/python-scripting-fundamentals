import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import make_nb

theorie = [
    ("md", """# 04. Werken met Containers / Collecties

Een **container** (of collectie) bewaart **meerdere waarden** in één variabele. Python heeft vier hoofdtypes: **lists**, **tuples**, **dictionaries** en **sets**. Elk heeft zijn eigen sterktes.

> 🎯 **Waarom?** Een playlist, een winkelmandje, een cryptoportfolio, een volgerslijst — dat zijn allemaal collecties. Wie data wil manipuleren, moet containers beheersen.
"""),
    ("md", """## 1. Lists

Een **list** is een **geordende, aanpasbare** verzameling. Je maakt ze met vierkante haken `[]`. Elementen mogen van elk type zijn en mogen dubbel voorkomen.
"""),
    ("code", """playlist = ["Blinding Lights", "As It Was", "Flowers"]

print(playlist[0])       # eerste element (index 0)
print(playlist[-1])      # laatste element
print(len(playlist))     # aantal elementen"""),
    ("md", """### 1.1 Aanpassen (muteren)
"""),
    ("code", """playlist = ["A", "B", "C"]

playlist.append("D")       # achteraan toevoegen
playlist.insert(1, "X")    # invoegen op index 1
playlist.remove("B")       # op waarde verwijderen
verwijderd = playlist.pop()  # laatste verwijderen én teruggeven
playlist[0] = "Z"          # element vervangen

print(playlist, "| verwijderd:", verwijderd)"""),
    ("md", """### 1.2 Slicing
"""),
    ("code", """cijfers = [0, 1, 2, 3, 4, 5]
print(cijfers[1:4])   # [1, 2, 3]
print(cijfers[:3])    # eerste drie
print(cijfers[::2])   # elke tweede"""),
    ("md", """### 1.3 Handige methodes
"""),
    ("code", """cijfers = [3, 1, 4, 1, 5, 9, 2]
cijfers.sort()          # sorteer in-place
print(cijfers)
print(min(cijfers), max(cijfers), sum(cijfers))
print(cijfers.count(1))   # hoe vaak komt 1 voor"""),
    ("md", """> ⚠️ **Gotcha**: `sort()` past de lijst **in-place** aan en geeft `None` terug. Wil je een nieuwe, gesorteerde kopie, gebruik dan `sorted(lijst)`.
"""),
    ("md", """## 2. Tuples

Een **tuple** is een **geordende, onveranderlijke** verzameling. Je maakt ze met ronde haken `()`. Eens gemaakt, kan je ze niet meer wijzigen.
"""),
    ("code", """punt = (4, 2)          # x, y-coördinaat
rgb = (255, 87, 51)     # een kleur

print(punt[0])
# punt[0] = 5  # ❌ TypeError: 'tuple' object does not support item assignment"""),
    ("md", """**Waarom een tuple i.p.v. een list?** Voor data die niet mag veranderen (coördinaten, config-waarden, RGB-kleuren) en als sleutel in een dictionary. Ze zijn ook iets sneller.

**Unpacking** — tuples (en lists) kan je elegant uit elkaar trekken:
"""),
    ("code", """x, y = (4, 2)
print(x, y)

naam, leeftijd, stad = "Lotte", 21, "Brussel"
print(naam, leeftijd, stad)"""),
    ("md", """## 3. Dictionaries

Een **dict** bewaart **sleutel-waarde paren** (`key → value`). Je maakt ze met accolades `{}`. Opzoeken gaat via de sleutel, niet via een index.
"""),
    ("code", """gebruiker = {
    "naam": "Lotte",
    "leeftijd": 21,
    "is_premium": True,
}

print(gebruiker["naam"])          # Lotte
print(gebruiker.get("bio", "geen"))  # veilige lookup met default"""),
    ("md", """### 3.1 Toevoegen, wijzigen, verwijderen
"""),
    ("code", """gebruiker = {"naam": "Lotte"}

gebruiker["leeftijd"] = 21      # toevoegen
gebruiker["naam"] = "L. Peeters"  # wijzigen
del gebruiker["leeftijd"]       # verwijderen

print(gebruiker)"""),
    ("md", """### 3.2 Loopen over een dict
"""),
    ("code", """scores = {"Ana": 95, "Youssef": 88, "Lotte": 91}

for naam, score in scores.items():
    print(f"{naam}: {score}")"""),
    ("md", """> ⚠️ **Gotcha**: `dict["onbekende_sleutel"]` geeft een `KeyError`. Gebruik `dict.get(sleutel, default)` als de sleutel misschien niet bestaat.
"""),
    ("md", """## 4. Sets

Een **set** is een **ongeordende** verzameling van **unieke** elementen (geen dubbels). Handig om duplicaten te verwijderen en om verzamelingenleer te doen.
"""),
    ("code", """volgers = {"alice", "bob", "alice", "carol"}
print(volgers)          # {'alice', 'bob', 'carol'} — dubbels weg!

volgers.add("dave")
volgers.discard("bob")
print(volgers)"""),
    ("md", """### 4.1 Verzamelingenleer
"""),
    ("code", """a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # unie
print(a & b)   # doorsnede
print(a - b)   # verschil
print(a ^ b)   # symmetrisch verschil"""),
    ("md", """> ⚠️ **Gotcha**: sets zijn **ongeordend** — de volgorde is niet gegarandeerd en kan veranderen. Ze kunnen ook geen lists/dicts bevatten (die zijn niet "hashable").
"""),
    ("md", """## 5. List comprehensions

Een **list comprehension** bouwt een nieuwe lijst in één compacte regel. Ze is vaak leesbaarder én sneller dan een gewone `for`-lus.
"""),
    ("code", """# klassieke lus
kwadraten = []
for i in range(5):
    kwadraten.append(i ** 2)

# list comprehension
kwadraten = [i ** 2 for i in range(5)]

print(kwadraten)  # [0, 1, 4, 9, 16]"""),
    ("md", """### 5.1 Met een voorwaarde
"""),
    ("code", """# alleen even getallen
even = [i for i in range(10) if i % 2 == 0]
print(even)  # [0, 2, 4, 6, 8]

# transformeer én filter
namen = ["ana", "BOB", "carol", "DAVE"]
grote_namen = [n.upper() for n in namen if len(n) > 3]
print(grote_namen)"""),
    ("md", """> 💡 **Pro-tip**: dezelfde syntaxis werkt ook voor **dicts** (`{k: v for ...}`) en **sets** (`{x for ...}`).
"""),
    ("md", """## 6. Welke container wanneer?

| Container | Geordend? | Aanpasbaar? | Dubbels? | Typisch gebruik |
|-----------|-----------|-------------|----------|------------------|
| `list` | ✅ | ✅ | ✅ | playlist, winkelmand, reeks |
| `tuple` | ✅ | ❌ | ✅ | coördinaat, vaste config |
| `dict` | ✅ (sinds 3.7) | ✅ | sleutels uniek | gebruiker, instellingen |
| `set` | ❌ | ✅ | ❌ | unieke waarden, lidmaatschap |

## 7. Samenvatting

- **list** → geordend & aanpasbaar (`[]`).
- **tuple** → geordend & onveranderlijk (`()`).
- **dict** → sleutel-waarde paren (`{}`, `{"k": v}`).
- **set** → ongeordend & uniek (`{}`).
- **list comprehension** → compacte lijst-bouw: `[expr for x in ... if ...]`.
"""),
]

oef = [
    ("md", """# 04 - Oefeningen (Containers)

* Maak deze oefeningen zelfstandig; ze worden klassikaal behandeld.
* 🔥 Van playlists tot cryptoportfolio's: dit is waar het écht mee gebeurt.
"""),
    ("md", """#### Oefening 1 — Spotify-playlist beheren
Maak een list `playlist` met 5 favoriete nummers. Voer daarna uit: voeg een nummer toe, vervang het tweede nummer, verwijder het laatste, en sorteer alfabetisch. Print elke stap.
"""),
    ("code", """playlist = ["...", "...", "...", "...", "..."]
"""),
    ("md", """#### Oefening 2 — Cryptoportfolio als dict
Bewaar je munten in een dict: `{"BTC": 0.5, "ETH": 12, "DOGE": 2500}`. Print voor elke munt "Je hebt X BTC". Voeg daarna een nieuwe munt toe en verwijder DOGE.
"""),
    ("code", """portfolio = {"BTC": 0.5, "ETH": 12, "DOGE": 2500}
"""),
    ("md", """#### Oefening 3 — Duplicaten uit een volgerslijst (set)
Je exporteert je volgers van twee platformen en hebt dubbels. Verwijder de duplicaten met een `set` en toon het aantal unieke volgers.
"""),
    ("code", """platform_a = ["alice", "bob", "carol", "dave"]
platform_b = ["carol", "dave", "erin", "frank"]
"""),
    ("md", """#### Oefening 4 — Gedeelde volgers (set-operaties)
Gebruik dezelfde twee lijsten. Wie volgt jou op **beide** platformen (doorsnede)? En wie volgt je maar op één platform (symmetrisch verschil)?
"""),
    ("code", """a = set(platform_a)
b = set(platform_b)
"""),
    ("md", """#### Oefening 5 — Tuple voor een profiel
Bewaar een streamer-profiel als **tuple**: `(naam, leeftijd, aantal_abonnees)`. Unpack de tuple in drie variabelen en print ze netjes. Leg uit waarom een tuple hier logisch is.
"""),
    ("code", """profiel = ("NoraPlays", 24, 850_000)
"""),
    ("md", """#### Oefening 6 — Winkelmandje totaal (list + loop)
Je hebt een winkelmandje met prijzen. Bereken het totaal met `sum()`, en print daarnaast het duurste en goedkoopste item.
"""),
    ("code", """winkelmand = [12.50, 3.99, 27.00, 8.75, 15.20]
"""),
    ("md", """#### Oefening 7 — Slicing van een leaderboard
Gegeven een gesorteerd leaderboard (beste eerst). Print met slicing: de **top 3**, de **plaatsen 4 tot 6**, en de **laatste 3**.
"""),
    ("code", """leaderboard = ["Zoe", "Yassine", "Wout", "Vera", "Umut", "Tess", "Sam", "Rik", "Quinn", "Pia"]
"""),
    ("md", """#### Oefening 8 — List comprehension: prijzen met korting
Gegeven `prijzen = [10, 25, 40, 55, 100]`, maak met een **list comprehension** een nieuwe lijst met alle prijzen boven 30, verminderd met 10% korting.
"""),
    ("code", """prijzen = [10, 25, 40, 55, 100]
"""),
    ("md", """#### Oefening 9 — Dict comprehension: score-parsen
Gegeven `scores = {"Ana": "95", "Youssef": "88", "Lotte": "91"}` (strings!), maak met een **dict comprehension** een nieuwe dict met de scores als `int`.
"""),
    ("code", """scores = {"Ana": "95", "Youssef": "88", "Lotte": "91"}
"""),
    ("md", """#### Oefening 10 — Veilig opzoeken (get)
Schrijf code die de waarde van een (mogelijk ontbrekende) sleutel veilig ophaalt met `get()`. Test het met een bestaande én een niet-bestaande sleutel.
"""),
    ("code", """gebruiker = {"naam": "Lotte", "leeftijd": 21}
# print(gebruiker.get("bio", ...))
"""),
    ("md", """#### Oefening 11 — In-place vs. kopie (gotcha)
Toon met code het verschil tussen `lijst.sort()` (in-place) en `sorted(lijst)` (nieuwe lijst). Print beide resultaten én de oorspronkelijke lijst.
"""),
    ("code", """lijst = [5, 2, 8, 1]
"""),
    ("md", """#### Oefening 12 — Combinatie-opdracht: NFT-tracker
Maak een dict die van 3 "NFT's" de naam en prijs (float) bijhoudt. Gebruik een list comprehension om de **totale waarde** en de **gemiddelde prijs** te berekenen, en print de duurste.
"""),
    ("code", """nfts = {"BoredApe": 84.5, "CryptoPunk": 120.0, "Doodle": 12.3}
"""),
]

make_nb("04-containers/theorie.ipynb", theorie)
make_nb("04-containers/oefeningen.ipynb", oef)
