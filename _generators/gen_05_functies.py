import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import make_nb

theorie = [
    ("md", """# 05. Functies

Een **functie** is een herbruikbaar blok code dat je één naam geeft en kan aanroepen. In plaats van dezelfde code 10 keer te kopiëren, schrijf je hem één keer en roep je hem 10 keer aan.

> 🎯 **Waarom?** Functies zijn de bouwstenen van élk serieus programma. Discord-bots, prijscalculators, validatiechecks — alles is opgebouwd uit kleine functies die samenwerken.
"""),
    ("md", """## 1. Wat zijn functies?

Een functie is als een **recept**: je geeft er invoer (ingrediënten) aan, ze voert een reeks stappen uit, en geeft (meestal) een resultaat terug.

**Waarom functies gebruiken?**
- **DRY** (Don't Repeat Yourself): één keer schrijven, overal gebruiken.
- **Leesbaarheid**: een naam zoals `bereken_btw()` zegt meer dan 5 losse regels code.
- **Testbaarheid**: je kan een functie los van de rest testen.
"""),
    ("md", """## 2. Aanroepen van functies

**Ingebouwde functies** bestaan al: `print()`, `len()`, `input()`, `type()`, `sum()`, `max()`, ... Je roept ze aan met hun naam, gevolgd door haakjes, en geeft argumenten mee.
"""),
    ("code", """print(len("Python"))   # 6
print(max(3, 7, 1))    # 7
print(sum([1, 2, 3]))  # 6"""),
    ("md", """De **retourwaarde** van een functie kan je opslaan in een variabele:
"""),
    ("code", """lengte = len("Hallo")
print(lengte)  # 5"""),
    ("md", """## 3. Eigen functies definiëren

Je definieert een functie met het keyword `def`, een naam, haakjes en een `:`.
"""),
    ("code", """def begroet():
    print("Hallo daar!")

begroet()  # aanroepen"""),
    ("md", """### 3.1 Een waarde teruggeven met `return`

Zonder `return` geeft een functie `None` terug. Met `return` stuurt ze een resultaat naar de aanroeper.
"""),
    ("code", """def verdubbel(n):
    return n * 2

resultaat = verdubbel(5)
print(resultaat)  # 10"""),
    ("md", """> ⚠️ **Gotcha**: `return` stopt de functie **onmiddellijk**. Code na de `return` wordt niet uitgevoerd.
"""),
    ("code", """def demo():
    return "Klaar"
    print("Dit wordt nooit afgedrukt!")

print(demo())"""),
    ("md", """## 4. Argumenten & parameters

- **Parameters** zijn de namen in de functie-definitie.
- **Argumenten** zijn de werkelijke waarden die je meegeeft bij de aanroep.
"""),
    ("code", """def begroet(naam):      # 'naam' is de parameter
    print(f"Hallo {naam}")

begroet("Lotte")        # "Lotte" is het argument"""),
    ("md", """### 4.1 Meerdere parameters
"""),
    ("code", """def stel_voor(naam, leeftijd):
    print(f"{naam} is {leeftijd} jaar oud.")

stel_voor("Youssef", 24)"""),
    ("md", """### 4.2 Standaardwaarden (default parameters)
"""),
    ("code", """def begroet(naam, taal="nl"):
    if taal == "nl":
        print(f"Hallo {naam}")
    else:
        print(f"Hello {naam}")

begroet("Lotte")          # gebruikt default 'nl'
begroet("Lotte", "en")    # overschrijft"""),
    ("md", """### 4.3 Keyword arguments

Je kan argumenten **bij naam** doorgeven. De volgorde maakt dan niet meer uit.
"""),
    ("code", """def stel_voor(naam, leeftijd):
    print(f"{naam} is {leeftijd} jaar.")

stel_voor(leeftijd=24, naam="Youssef")  # volgorde maakt niet uit"""),
    ("md", """> ⚠️ **Gotcha**: **positionele** argumenten moeten vóór **keyword** argumenten komen. `f(naam="Lotte", 21)` is een syntaxfout.
"""),
    ("md", """### 4.4 `*args` en `**kwargs`

Voor een variabel aantal argumenten:
"""),
    ("code", """def som(*getallen):
    return sum(getallen)

print(som(1, 2))       # 3
print(som(1, 2, 3, 4)) # 10"""),
    ("code", """def toon_profiel(**eigenschappen):
    for sleutel, waarde in eigenschappen.items():
        print(f"{sleutel}: {waarde}")

toon_profiel(naam="Lotte", leeftijd=21, stad="Brussel")"""),
    ("md", """## 5. Scope

**Scope** bepaalt waar een variabele zichtbaar is.

- Een variabele **binnen** een functie is **lokaal** — alleen zichtbaar in die functie.
- Een variabele **buiten** alle functies is **globaal** — overal leesbaar, maar je kan ze in een functie niet zomaar wijzigen.
"""),
    ("code", """x = 10  # globale variabele

def toon():
    print(x)   # leesbaar vanuit de functie

def wijzig():
    x = 20     # maakt een NIEUWE lokale variabele, wijzigt de globale NIET
    print(x)   # 20

toon()   # 10
wijzig() # 20
print(x) # 10  (ongewijzigd!)"""),
    ("md", """> ⚠️ **Gotcha**: binnen een functie een globale variabele toekennen (`x = 20`) maakt een **lokale** variabele. Wil je de globale écht wijzigen, gebruik dan `global x` — maar dat doe je bij voorkeur zo weinig mogelijk.
"""),
    ("code", """teller = 0

def verhoog():
    global teller
    teller += 1

verhoog()
print(teller)  # 1"""),
    ("md", """## 6. Lambdas

Een **lambda** is een anonieme functie in één regel. Handig voor korte, eenmalige bewerkingen.
"""),
    ("code", """verdubbel = lambda n: n * 2
print(verdubbel(5))  # 10"""),
    ("md", """### 6.1 Lambdas met `map`, `filter`, `sorted`
"""),
    ("code", """cijfers = [1, 2, 3, 4, 5]

kwadraten = list(map(lambda x: x ** 2, cijfers))
print(kwadraten)  # [1, 4, 9, 16, 25]

even = list(filter(lambda x: x % 2 == 0, cijfers))
print(even)  # [2, 4]"""),
    ("code", """namen = [("Lotte", 21), ("Ana", 30), ("Youssef", 24)]

# sorteer op leeftijd (tweede element van elke tuple)
namen.sort(key=lambda x: x[1])
print(namen)"""),
    ("md", """> 💡 **Vuistregel**: gebruik een `lambda` voor één regel. Wordt de logica langer of minder duidelijk, schrijf dan gewoon een `def`-functie.
"""),
    ("md", """## 7. Samenvatting

- **`def naam(params):`** definieert, **`naam(args)`** roept aan.
- **`return`** geeft een waarde terug én stopt de functie.
- **Parameters** = namen in de definitie, **argumenten** = waarden bij aanroep.
- **Default** parameters: `def f(x=1)`.
- **Keyword args**: `f(leeftijd=24)` — positionele eerst.
- **Scope**: lokaal binnen functies, globaal daarbuiten.
- **`lambda`** = anonieme éénregel-functie.
"""),
]

oef = [
    ("md", """# 05 - Oefeningen (Functies)

* Maak deze oefeningen zelfstandig; ze worden klassikaal behandeld.
* 🔥 Functies die je hier schrijft, zou je zó in een echte app hergebruiken.
"""),
    ("md", """#### Oefening 1 — BTW-calculator
Schrijf een functie `btw(bedrag, tarief=21)` die het BTW-bedrag teruggeeft. Roep hem aan met en zonder expliciet tarief.
"""),
    ("code", """def btw(bedrag, tarief=21):
    return bedrag * tarief / 100

# test met 100 en 6% tarief
"""),
    ("md", """#### Oefening 2 — Creator-commissie
Een platform neemt **20%** commissie op elke donatie. Schrijf `netto(bruto)` die het bedrag na commissie teruggeeft, en test met €50 en €123.45.
"""),
    ("code", """def netto(bruto):
    pass  # vul in
"""),
    ("md", """#### Oefening 3 — Welkomstfunctie met default
Schrijf `welkom(naam, taal="nl")` die in het Nederlands of Engels begroet. Test beide talen.
"""),
    ("code", """def welkom(naam, taal="nl"):
    pass  # vul in
"""),
    ("md", """#### Oefening 4 — Return vs. None
Schrijf een functie `toon(x)` die alleen `print` doet (zonder `return`), en een functie `geef(x)` die `return` gebruikt. Toon het verschil door het resultaat op te slaan en af te drukken.
"""),
    ("code", """def toon(x):
    print(x)

def geef(x):
    return x
"""),
    ("md", """#### Oefening 5 — Keyword arguments
Schrijf `bestelling(product, aantal, prijs)` en roep hem aan met **keyword arguments** in willekeurige volgorde, zodat hij een f-string afdrukt met het totaal.
"""),
    ("code", """def bestelling(product, aantal, prijs):
    pass  # vul in
"""),
    ("md", """#### Oefening 6 — Variabel aantal argumenten
Schrijf `gemiddelde(*getallen)` die het gemiddelde teruggeeft van een willekeurig aantal getallen. Test met 2, 3 en 10 argumenten.
"""),
    ("code", """def gemiddelde(*getallen):
    pass  # vul in
"""),
    ("md", """#### Oefening 7 — Scope-detective
Voorspel de output van deze code. Voer daarna uit en leg uit wat er met de globale variabele gebeurt.
"""),
    ("code", """x = 100

def verander():
    x = 5
    print("binnen:", x)

verander()
print("buiten:", x)
"""),
    ("md", """#### Oefening 8 — Teller met `global`
Schrijf een functie `verhoog()` die een globale `teller` met 1 verhoogt. Roep hem 5 keer aan en print de teller.
"""),
    ("code", """teller = 0

def verhoog():
    pass  # vul in
"""),
    ("md", """#### Oefening 9 — Lambda + sort
Sorteer een lijst van streamers `(naam, abonnees)` van meest naar minst abonnees, met een `lambda`.
"""),
    ("code", """streamers = [("Nora", 850_000), ("Piet", 12_000), ("Zoe", 2_400_000)]
"""),
    ("md", """#### Oefening 10 — Lambda + map
Gebruik `map` met een `lambda` om een lijst van prijzen met 15% korting te berekenen. Zet het resultaat om naar een list.
"""),
    ("code", """prijzen = [10, 25, 40, 100]
"""),
    ("md", """#### Oefening 11 — Validatiefunctie
Schrijf een functie `is_geldig_gebruikersnaam(naam)` die `True` teruggeeft als de naam minstens 3 karakters heeft en geen spatie bevat, anders `False`. Test met goede en foute namen.
"""),
    ("code", """def is_geldig_gebruikersnaam(naam):
    pass  # vul in
"""),
    ("md", """#### Oefening 12 — Functie die een functie gebruikt
Schrijf `sorteer_prijzen(lijst, dalend=False)` die een gesorteerde kopie teruggeeft (gebruik `sorted`). Test oplopend en dalend, en toon dat de oorspronkelijke lijst ongewijzigd blijft.
"""),
    ("code", """def sorteer_prijzen(lijst, dalend=False):
    pass  # vul in
"""),
]

make_nb("05-functies/theorie.ipynb", theorie)
make_nb("05-functies/oefeningen.ipynb", oef)
