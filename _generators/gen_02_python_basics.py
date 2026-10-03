import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import make_nb

theorie = [
    ("md", """# 02. Python Basics

Dit hoofdstuk legt de fundering: **syntax**, **invoer/uitvoer**, **variabelen**, **datatypes**, **operatoren** en **f-strings**. Alles wat volgt in dit semester bouwt hierop verder.

> 🎯 **Doel**: na dit hoofdstuk kan je een klein script schrijven dat data inleest, verwerkt en netjes afdrukt.
"""),
    ("md", """## 1. Syntax, statements, comments & docstring

### 1.1 Statements
Python voert je code **regel per regel uit**, van boven naar onder. Eén instructie = één statement. In tegenstelling tot bv. Java heb je **geen puntkomma** nodig aan het einde.
"""),
    ("code", """print("Eerste regel")
print("Tweede regel")"""),
    ("md", """### 1.2 Comments
Een **comment** is tekst die Python negeert. Je gebruikt `#` om code uit te leggen — niet om uit te zetten wat je niet wil. Comments zijn voor **mensen**, niet voor de computer.
"""),
    ("code", """# Dit is een comment — Python negeert deze regel volledig
x = 10  # een comment kan ook achter code staan
# x = 20  # deze regel is 'uitgecomment' en wordt niet uitgevoerd"""),
    ("md", """### 1.3 Docstrings
Een **docstring** is een speciale string met drie quotes die je gebruikt om code te documenteren. Je zet ze bovenaan een bestand of cel. Bij de functies komt een docstring later óók bovenaan elke functie te staan.
"""),
    ("code", """'''Dit script begroet een gebruiker.

Een docstring documenteert wat de code doet.
Docstrings komen later ook bij functies terug.
'''

print("Hallo, wereld!")"""),
    ("md", """### 1.4 Indentatie = codeblokken

In Python bepaalt **inspringing (indentatie)** welke code bij elkaar hoort. Er zijn geen accolades `{}` zoals in andere talen. Een codeblok wordt voorafgegaan door een `:` en is **4 spaties** ingesprongen.
"""),
    ("code", """if True:
    print("Deze regel hoort bij de if")
    print("Deze ook")
print("Deze staat erbuiten")"""),
    ("md", """> ⚠️ **Veelgemaakte fout**: spaties en tabs door elkaar gebruiken geeft `IndentationError`. Stel je editor in om tabs automatisch om te zetten naar 4 spaties.
"""),
    ("md", """## 2. Invoer & uitvoer

### 2.1 Uitvoer met `print()`
"""),
    ("code", """print("Hallo")
print(42)
print(3.14, "is pi")  # meerdere argumenten, gescheiden door spatie"""),
    ("md", """### 2.2 Invoer met `input()`
`input()` leest een lijn tekst van de gebruiker en geeft die **altijd terug als string**.
"""),
    ("code", """naam = input("Wat is je naam? ")
print("Hoi", naam)"""),
    ("md", """> ⚠️ **De grote gotcha**: `input()` geeft altijd een `str`. Wil je rekenen met de invoer, dan moet je **expliciet converteren**.
"""),
    ("code", """leeftijd = input("Leeftijd? ")
# print(leeftijd + 1)  # ❌ TypeError: can only concatenate str

leeftijd = int(input("Leeftijd? "))
print(leeftijd + 1)  # ✅ werkt nu"""),
    ("md", """## 3. Variabelen & toekenningen

Een **variabele** is een naam die naar een waarde verwijst. Je maakt er één met `=`.
"""),
    ("code", """naam = "Lotte"
leeftijd = 21
is_student = True

print(naam, leeftijd, is_student)"""),
    ("md", """### 3.1 Naamgevingsregels
- Moet starten met een **letter** of `_` (niet met een cijfer).
- Mag letters, cijfers en `_` bevatten (geen spaties of `-`).
- Is **hoofdlettergevoelig**: `leeftijd` ≠ `Leeftijd`.
- Mag **geen gereserveerd keyword** zijn (`for`, `if`, `class`, ...).
- **Stijlregel (PEP 8)**: gebruik `snake_case` voor variabelen.
"""),
    ("code", """# ❌ fout of slechte stijl
# 1ste_getal = 7     # start met cijfer
# for = 2            # keyword
# MAX-waarde = 100   # streepje is niet toegelaten
# voorNaam = "Alice" # camelCase, geen snake_case

# ✅ correct
eerste_getal = 7
max_waarde = 100
voornaam = "Alice"
"""),
    ("md", """### 3.2 Dynamisch typen
Python bepaalt het type **automatisch** bij toekenning. Je kan een variabele later zelfs een ander type geven (al is dat meestal geen goed idee).
"""),
    ("code", """x = 10          # int
x = "tekst"     # nu een str — Python vindt dit ok
print(x)"""),
    ("md", """### 3.3 Meervoudige toekenning
"""),
    ("code", """a, b, c = 1, 2, 3
x = y = 0  # beide worden 0
print(a, b, c, x, y)"""),
    ("md", """## 4. Datatypes

De vier belangrijkste types in dit hoofdstuk:

| Type | Python | Voorbeeld | Gebruik |
|------|--------|-----------|---------|
| Tekst | `str` | `"Hallo"` | namen, tekst, URL's |
| Geheel getal | `int` | `42` | aantallen, tellers |
| Kommagetal | `float` | `3.14` | prijzen, metingen |
| Booleaans | `bool` | `True` / `False` | voorwaarden |

### 4.1 Strings
"""),
    ("code", """naam = "Lotte"
print(len(naam))        # lengte
print(naam.upper())     # HOOFDLETTERS
print(naam.lower())     # kleine letters
print("tt" in naam)     # zit 'tt' in de string?"""),
    ("md", """**Indexering & slicing** — je telt vanaf **0**:
"""),
    ("code", """woord = "Python"
print(woord[0])     # 'P'
print(woord[-1])    # 'n' (laatste)
print(woord[0:3])   # 'Pyt' (van 0 tot 3, 3 niet inbegrepen)
print(woord[2:])    # 'thon'"""),
    ("md", """### 4.2 Numerieke types
"""),
    ("code", """a = 10      # int
b = 2.5     # float
c = 1 + 2j  # complex (zeldzaam, voor wiskunde)

print(type(a), type(b), type(c))"""),
    ("md", """### 4.3 Booleans
Een `bool` is ofwel `True` ofwel `False` — het resultaat van vergelijkingen.
"""),
    ("code", """print(10 > 5)    # True
print(10 == 5)   # False
print(bool(0))   # False — 0 is 'falsy'
print(bool("x")) # True — niet-lege string is 'truthy'"""),
    ("md", """### 4.4 Type controleren & converteren
"""),
    ("code", """x = "42"
print(type(x))      # <class 'str'>

n = int(x)          # naar int
f = float(x)        # naar float
s = str(42)         # naar str
b = bool(1)         # naar bool (True)

print(n, f, s, b)"""),
    ("md", """> ⚠️ **Gotcha**: `int("4.2")` geeft een fout, want "4.2" is geen geheel getal. Eerst `float("4.2")` en dan pas eventueel `int(...)`.
"""),
    ("md", """## 5. Operatoren & berekeningen

### 5.1 Rekenkundige operatoren
"""),
    ("code", """print(7 + 2)    # 9  optellen
print(7 - 2)    # 5  aftrekken
print(7 * 2)    # 14 vermenigvuldigen
print(7 / 2)    # 3.5  gewone deling (altijd float!)
print(7 // 2)   # 3  gehele deling
print(7 % 2)    # 1  modulo (rest)
print(7 ** 2)   # 49 machtsverheffing"""),
    ("md", """> ⚠️ **Gotcha**: `/` geeft **altijd een float**, ook als het "mooi" uitkomt (`10 / 2` → `5.0`). Voor een `int`-resultaat gebruik je `//`.
"""),
    ("md", """### 5.2 Vergelijkingsoperatoren
Gelijke resultaten altijd in een `bool` (`True` / `False`):
"""),
    ("code", """print(5 == 5)  # True   gelijk aan
print(5 != 5)  # False  niet gelijk
print(5 < 3)   # False
print(5 >= 5)  # True"""),
    ("md", """### 5.3 Logische operatoren
`and`, `or` en `not` combineren booleaanse waarden:
"""),
    ("code", """leeftijd = 20
heeft_lidkaart = True

print(leeftijd > 18 and heeft_lidkaart)  # True
print(leeftijd > 21 or heeft_lidkaart)   # True
print(not heeft_lidkaart)                 # False"""),
    ("md", """### 5.4 Toekenningsoperatoren
Snelkoppelingen voor `x = x + ...`:
"""),
    ("code", """saldo = 100
saldo += 25   # saldo = saldo + 25
saldo -= 10   # saldo = saldo - 10
saldo *= 2    # verdubbel
saldo //= 3   # gehele deling
print(saldo)"""),
    ("md", """### 5.5 Operatorprecedentie
Python volgt de wiskundige volgorde: **haakjes → macht → × en / // % → + - → vergelijkingen → not → and → or**.
"""),
    ("code", """print(2 + 3 * 4)     # 14  (niet 20!)
print((2 + 3) * 4)   # 20"""),
    ("md", """## 6. F-strings

Een **f-string** (formatted string) laat je toe variabelen rechtstreeks in tekst te steken. Zet een `f` vóór de string en gebruik `{variabele}`.
"""),
    ("code", """naam = "Anissa"
aantal = 3
prijs = 2.5

print(f"{naam} koopt {aantal} stuks.")"""),
    ("md", """### 6.1 Getallen formatteren
"""),
    ("code", """prijs = 2.5
print(f"Prijs: {prijs:.2f}")   # 2 decimalen → 2.50
print(f"Score: {85:.1f}%")     # 1 decimaal

groot = 1234567
print(f"{groot:,}")            # duizendtallen → 1,234,567"""),
    ("md", """### 6.2 Uitlijning & breedte
"""),
    ("code", """naam = "Lotte"
print(f"{naam:>10}")   # rechts uitgelijnd, breedte 10
print(f"{naam:<10}")   # links uitgelijnd
print(f"{naam:^10}")   # gecentreerd"""),
    ("md", """### 6.3 Expressies in een f-string
Tussen de accolades mag je ook **uitdrukkingen** plaatsen:
"""),
    ("code", """aantal = 3
prijs = 2.5
print(f"Totaal: {aantal * prijs:.2f} euro")"""),
    ("md", """## 7. Samenvatting

- **Comment** = `#`, **docstring** = `'''...'''`, **indentatie** = codeblokken.
- **`input()` geeft altijd een string** — converteer met `int()`, `float()`.
- **Datatypes**: `str`, `int`, `float`, `bool` — controleer met `type()`, converteer met `int()/float()/str()`.
- **`/`** is gewone deling (float), **`//`** is gehele deling, **`%`** is rest.
- **F-strings** (`f"..."`) zijn de moderne, leesbare manier om tekst op te maken.
"""),
]

oef = [
    ("md", """# 02 - Oefeningen

* Deze oefeningen maak je zelfstandig; ze worden klassikaal behandeld.
* 🔥 Elke oefening heeft een modern "waarom". Zo oefen je op scenario's die je écht tegenkomt.
* Schrijf je oplossing telkens in het codevak onder de opgave.
"""),
    ("md", """#### Oefening 1 — Crypto-portfolio tracker (deel 1)
Je houdt 3 munten bij: **0.5 BTC**, **12 ETH** en **2500 DOGE**. Ken aan elke munt een waarde toe in euro en druk je totale portfolio af met een duidelijke f-string.
"""),
    ("code", """# prijzen per munt (in euro)
btc = 0.5 * 61000
eth = 12 * 3100
doge = 2500 * 0.12

# bereken hier het totaal en print het
"""),
    ("md", """#### Oefening 2 — Streaming payout
Een streamer verdient **€0.0034 per view**. Hij haalde vorige maand **1.2 miljoen views**. Bereken zijn maandinkomen en druk het af met **2 decimalen** en duizendtallen-scheiding.
"""),
    ("code", """views = 1_200_000
per_view = 0.0034

# bereken en print het maandinkomen
"""),
    ("md", """#### Oefening 3 — Leeftijdscheck (invoer + conversie)
Lees met `input()` de leeftijd van de gebruiker in. Zorg dat het een **geheel getal** wordt en print: `Over 5 jaar ben je <leeftijd+5>.`
"""),
    ("code", """# lees leeftijd in en converteer naar int
"""),
    ("md", """#### Oefening 4 — Splits de rekening
Vier vrienden gaan uit eten. De rekening is **€87.60**. Bereken met een f-string hoeveel ieder betaalt (2 decimalen), **en** wat de "oneerlijke" rest is als je het bedrag niet exact kan delen.
"""),
    ("code", """rekening = 87.60
vrienden = 4

# per persoon + rest via // en %
"""),
    ("md", """#### Oefening 5 — Sneaker resale
Je kocht een paar sneakers voor **€120** en verkoopt ze door voor **€210**. Bereken je **winst** en je **winstpercentage** (winst / aankoop * 100) en print beide netjes.
"""),
    ("code", """aankoop = 120
verkoop = 210

# winst + winstpercentage
"""),
    ("md", """#### Oefening 6 — Type-detective
Voorspel het type van elke variabele, en controleer daarna met `type()`. Welke verrassen je?
"""),
    ("code", """a = 5
b = 5.0
c = "5"
d = True
e = 10 / 2
f = 10 // 2

# print het type van elke variabele
"""),
    ("md", """#### Oefening 7 — Naam-stijl politie
Onderstaande variabelenamen zijn fout of slecht gestijld. Herschrijf ze correct (geldig + `snake_case`) met dezelfde waarden.
"""),
    ("code", """# 1steGetal = 7
# for = 2
# MAX-waarde = 100
# NaamStudent = "Maya"
# totaal bedrag = 19.99
"""),
    ("md", """#### Oefening 8 — BMI van de gym-goer
Lees gewicht (kg, `float`) en lengte (m, `float`) in. Bereken de **BMI** = gewicht / lengte² en print hem af met 1 decimaal.
"""),
    ("code", """# gewicht = float(input(...))
# lengte = float(input(...))
# bmi = ...
"""),
    ("md", """#### Oefening 9 — F-string meesterwerk
Je hebt `naam = "Youssef"`, `aantal = 12` en `prijs = 19.99`. Druk **op drie manieren** exact dezelfde zin af (concatenatie, `.format()`, f-string): `Youssef koopt 12 stuks aan 19.99 euro per stuk.`
"""),
    ("code", """naam = "Youssef"
aantal = 12
prijs = 19.99

# 1) concatenatie
# 2) .format()
# 3) f-string
"""),
    ("md", """#### Oefening 10 — Operator-puzzel
Bereken zonder de computer: wat is `(2 + 3 * 4) ** 2 % 10`? Verklaar de volgorde, en controleer daarna in code.
"""),
    ("code", """# schrijf je redenering in een comment, en controleer dan
"""),
    ("md", """#### Oefening 11 — Even of oneven (operator + f-string)
Lees een getal in en print `"<getal> is even"` of `"<getal> is oneven"` met behulp van de modulo-operator.
"""),
    ("code", """getal = int(input("Geef een getal: "))

# gebruik % om even/oneven te bepalen
"""),
    ("md", """#### Oefening 12 — Docstring & comment
Schrijf bovenaan de cel een **docstring** (tussen drie quotes) die uitlegt wat je mini-programma doet, en daaronder een **comment** (met `#`). Leg in je eigen woorden het verschil uit.
"""),
    ("code", """'''Dit is een docstring: ze documenteert het hele programma.'''

# Dit is een comment: uitleg voor één regel of een klein stukje code.
print("Hallo, wereld!")
"""),
]

make_nb("02-python-basics/theorie.ipynb", theorie)
make_nb("02-python-basics/oefeningen.ipynb", oef)
