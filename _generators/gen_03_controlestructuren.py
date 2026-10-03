import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import make_nb

selecties = [
    ("md", """# 03. Controlestructuren: Selecties

Controlestructuren sturen de loop van je programma. We onderscheiden twee soorten: **selecties** (beslissingen) en **iteraties** (herhalingen). Dit notebook behandelt de **selecties**.

> 🎯 **Waarom?** Elke app ter wereld zit vol beslissingen: "Is de gebruiker oud genoeg?", "Is het wachtwoord correct?", "Heeft de betaling succes?". Selecties zijn de `if`-logica achter al die keuzes.
"""),
    ("md", """## 1. Het `if`-statement

Een `if` voert een blok code enkel uit **als een voorwaarde `True` is**.
"""),
    ("code", """leeftijd = 20

if leeftijd > 18:
    print("Je mag stemmen")"""),
    ("md", """**Wat gebeurt hier?**
- Het keyword `if` zegt tegen Python: hier komt een voorwaarde.
- Daarna volgt een **booleaanse uitdrukking** (iets dat `True` of `False` is), gevolgd door een `:`.
- Is de uitdrukking `True`, dan wordt het **ingesprongen** blok uitgevoerd. Is ze `False`, dan wordt het overgeslagen.
- **Indentatie is verplicht** in Python (4 spaties).

Algemene vorm:

```python
if <<booleaanse uitdrukking>>:
    <<actie>>
```
"""),
    ("md", """## 2. Het `if-else`-statement

Met `else` voer je één blok uit als de voorwaarde `True` is, en een ander blok als ze `False` is. **Exact één** van beide wordt uitgevoerd.
"""),
    ("code", """leeftijd = 17

if leeftijd > 18:
    print("Je mag stemmen")
else:
    print("Je mag nog niet stemmen")
    print("Nog even geduld...")"""),
    ("md", """## 3. Het `if-elif-else`-statement

Voor **meer dan twee mogelijkheden** gebruik je `elif` (= "else if").
"""),
    ("code", """score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Niet geslaagd")"""),
    ("md", """- Python test de voorwaarden **van boven naar onder** en voert **alleen het eerste `True`-blok** uit.
- `elif` test een nieuwe voorwaarde; `else` vangt al de rest op.

> ⚠️ **Gotcha**: onderstaande versie lijkt op bovenstaande, maar werkt anders — elke `if` wordt *onafhankelijk* getest.
"""),
    ("code", """score = 85

if score >= 90:
    print("A")
if score >= 80:
    print("B")
if score >= 70:
    print("C")
else:
    print("Niet geslaagd")
#  → drukt "B" én "C" af!"""),
    ("md", """## 4. Geneste `if`-statements

Je kan `if` binnen `if` plaatsen. Let goed op de indentatie: die geldt steeds t.o.v. de `if` waarop je test.
"""),
    ("code", """leeftijd = 20
heeft_strafblad = False

if leeftijd > 18:
    if not heeft_strafblad:
        print("Je mag stemmen")
    else:
        print("Je mag niet stemmen (strafblad)")
else:
    print("Je mag niet stemmen (te jong)")"""),
    ("md", """## 5. Het `pass`-keyword

`pass` doet **niets**, maar voldoet aan de syntax. Handig als je de logica later nog schrijft.
"""),
    ("code", """leeftijd = 20

if leeftijd > 18:
    pass  # TODO: hier komt nog logica"""),
    ("md", """## 6. De ternaire operator

Een **compacte** `if-else` in één regel, handig voor toekenningen.
"""),
    ("code", """is_logged_in = True

# lange vorm
if is_logged_in:
    message = "Welkom"
else:
    message = "Log eerst in"

# korte vorm (ternair)
message = "Welkom" if is_logged_in else "Log eerst in"

print(message)"""),
    ("md", """## 7. `match`-`case` (Python 3.10+)

Voor een keuze op basis van de **waarde** van één variabele is `match`-`case` vaak leesbaarder dan een lange `if-elif`-ketting.
"""),
    ("code", """status = 200

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown")"""),
    ("md", """- `case _` is de "vang-alles", vergelijkbaar met `else` of `default` in C#.
- > ⚠️ **Opgelet**: `match` bestaat pas sinds **Python 3.10**. Controleer je versie met `python --version`.
"""),
    ("md", """## 8. Samenvatting

- `if` → voer uit **als** de voorwaarde waar is.
- `else` → het **alternatief**.
- `elif` → **extra voorwaarden** tussen `if` en `else`.
- **Indentatie** bepaalt het blok; `:` sluit de voorwaarde af.
- Ternaire operator → `waarde_if_true if conditie else waarde_if_false`.
- `match`-`case` → keuze op basis van een waarde (Python 3.10+).
"""),
]

iteraties = [
    ("md", """# 03. Controlestructuren: Iteraties

Een **iteratie** (of lus/loop) herhaalt een blok code. Python kent twee soorten: de **`for`-lus** en de **`while`-lus**.

> 🎯 **Waarom?** Zonder lussen zou je voor elke TikTok-video, elke rij in een spreadsheet of elke volger van een account handmatig code moeten schrijven. Lussen zijn dé motor van automatisering.
"""),
    ("md", """## 1. De `for`-lus

Een `for`-lus doorloopt een **reeks waarden** (zoals een `range` of een string) en voert het blok uit voor elk element.
"""),
    ("code", """for i in range(3):
    print("Hallo, bezoeker", i + 1)"""),
    ("md", """## 2. `range()`

`range(start, stop, stap)` genereert een reeks getallen. Handig om een lus een **vast aantal keer** te herhalen.
"""),
    ("code", """for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):     # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)"""),
    ("md", """> ⚠️ **Gotcha**: `range(stop)` **stopt vóór** `stop`. `range(5)` geeft 0–4, niet 5.
"""),
    ("md", """## 3. De `while`-lus

Een `while`-lus herhaalt **zolang een voorwaarde `True` is**. Gebruik hem wanneer je *op voorhand niet weet* hoe vaak je moet herhalen.
"""),
    ("code", """saldo = 100
maanden = 0

while saldo < 200:      # blijf sparen tot 200
    saldo += 25
    maanden += 1

print(f"Na {maanden} maanden heb je {saldo} euro")"""),
    ("md", """> ⚠️ **Gotcha**: zorg dat de voorwaarde ooit `False` wordt, anders krijg je een **oneindige lus**. In Jupyter: stop die met de stopknop ⏹ of `Ctrl + C`.
"""),
    ("md", """## 4. `break` en `continue`

- `break` → stop de lus **onmiddellijk**.
- `continue` → spring naar de **volgende iteratie**.
"""),
    ("code", """for i in range(10):
    if i == 3:
        continue   # sla 3 over
    if i == 7:
        break      # stop bij 7
    print(i)"""),
    ("md", """## 5. `else` bij een lus

Python laat toe een `else` achter een lus te zetten. Die wordt enkel uitgevoerd **als de lus normaal eindigt** (dus niet via `break`).
"""),
    ("code", """for i in range(5):
    print(i)
else:
    print("Lus normaal afgelopen")

# klassieke use case: "zoek iets, en als je het niet vindt..."
for letter in "Python":
    if letter == "z":
        print("Gevonden!")
        break
else:
    print("Niet gevonden")"""),
    ("md", """## 6. Geneste lussen

Een lus **binnen** een lus. Perfect voor tabellen en roosters.
"""),
    ("code", """for rij in range(1, 4):
    for kolom in range(1, 4):
        print(f"({rij},{kolom})", end=" ")
    print()  # nieuwe lijn na elke rij"""),
    ("md", """## 7. Lus over een string

Een string is eigenlijk een verzameling karakters — je kan er dus over lussen.
"""),
    ("code", """for letter in "Python":
    print(letter)"""),
    ("md", """## 8. Samenvatting

- **`for`** → herhaal over een collectie of `range()`.
- **`while`** → herhaal zolang een voorwaarde waar is.
- **`break`** stopt, **`continue`** slaat één iteratie over.
- **`range(stop)`** telt tot (maar niet inclusief) `stop`.
- **`else` na een lus** → enkel als de lus niet via `break` stopte.
"""),
]

oef = [
    ("md", """# 03 - Oefeningen (Selecties & Iteraties)

* Maak deze oefeningen zelfstandig; ze worden klassikaal behandeld.
* 🔥 Elke oefening komt uit een herkenbare, moderne context.
"""),
    ("md", """#### Oefening 1 — Age gate voor de "Members Only"-club
Een exclusieve club laat enkel leden toe die **minstens 18** én **geen 3 strikes** hebben. Lees leeftijd en strikes in en print `Toegang geweigerd` of `Welkom in de club`.
"""),
    ("code", """# lees leeftijd en strikes in, gebruik if met and
"""),
    ("md", """#### Oefening 2 — Tier-lijst van een streamer
Een streamer verdeelt zijn kijkers in tiers op basis van maandelijkse donaties: `<5` = "Lurker", `5–19` = "Supporter", `20–99` = "VIP", `>=100` = "Legend". Schrijf dit met `if-elif-else`.
"""),
    ("code", """donatie = 25  # verander om te testen
"""),
    ("md", """#### Oefening 3 — Gok-site odds (leeftijd + status)
Een bettingsite controleert: gebruiker moet **21+** zijn én **geen zelfuitsluiting** hebben. Gebruik een **geneste if**. Test met minstens 3 scenario's.
"""),
    ("code", """leeftijd = 22
uitgesloten = False
"""),
    ("md", """#### Oefening 4 — HTTP-status met `match`
Schrijf met `match`-`case` een vertaling van HTTP-codes: `200` → "OK", `404` → "Not Found", `500` → "Server Error", anders → "Onbekend". (Vergeet niet: dit vereist Python 3.10+.)
"""),
    ("code", """code = 404
"""),
    ("md", """#### Oefening 5 — Ternaire shortcut
Herschrijf deze code naar één regel met de ternaire operator:
"""),
    ("code", """saldi = 50
# if saldi > 0: status = "positief" else: status = "negatief"
"""),
    ("md", """#### Oefening 6 — Abonnee-teller (for + range)
Een creator heeft 12 maanden om van 1000 naar 5000 abonnees te groeien. Print voor elke maand de groei als hij er telkens 350 bij krijgt, en print na afloop zijn totaal.
"""),
    ("code", """abonnees = 1000
# for maand in range(...):
"""),
    ("md", """#### Oefening 7 — Spaardoel (while)
Je spaart voor een nieuwe telefoon van **€899**. Je start met **€120** en legt elke maand **€65** opzij. Gebruik een `while`-lus om te tellen hoeveel maanden je nodig hebt.
"""),
    ("code", """saldo = 120
doel = 899
maanden = 0
"""),
    ("md", """#### Oefening 8 — Filter de tekst (break + continue)
Je doorloopt de string `"abcXdefYghi"`. Sla de letter `"X"` over met `continue`, en stop volledig bij `"Y"` met `break`. Print elke andere letter.
"""),
    ("code", """for letter in "abcXdefYghi":
    # sla "X" over met continue, stop bij "Y" met break
    pass
"""),
    ("md", """#### Oefening 9 — Leaderboard-tabel (geneste lus)
Print een simpele leaderboard-tabel: plaats 1 tot en met 3, en voor elke plaats een rij met "naam" en "score" die je zelf invult. Gebruik een geneste `for`-lus.
"""),
    ("code", """# for plaats in range(1, 4): ...
"""),
    ("md", """#### Oefening 10 — Wachtwoord-retry (while + break)
Een app laat max. 3 pogingen toe om in te loggen. Gebruik een `while`-lus die stopt bij het juiste wachtwoord (`"geheim"`) of na 3 foute pogingen, en print het resultaat.
"""),
    ("code", """juist_wachtwoord = "geheim"
pogingen = 0
"""),
    ("md", """#### Oefening 11 — FizzBuzz, maar dan "Creator edition"
Loop van 1 tot 20. Print `"Fizz"` voor veelvouden van 3, `"Buzz"` voor veelvouden van 5, `"FizzBuzz"` voor veelvouden van beide, anders het getal. (Een legendarisch sollicitatie-vraagstuk.)
"""),
    ("code", """for i in range(1, 21):
    pass  # vervang door je logica
"""),
    ("md", """#### Oefening 12 — Totaal & gemiddelde van een reeks
Gebruik een `for`-lus om de **som** en het **gemiddelde** te berekenen van de getallen 1 tot en met 10 (met `range`).
"""),
    ("code", """totaal = 0
for i in range(1, 11):
    totaal += i

gemiddelde = totaal / 10
"""),
]

make_nb("03-controlestructuren/theorie-selecties.ipynb", selecties)
make_nb("03-controlestructuren/theorie-iteraties.ipynb", iteraties)
make_nb("03-controlestructuren/oefeningen.ipynb", oef)
