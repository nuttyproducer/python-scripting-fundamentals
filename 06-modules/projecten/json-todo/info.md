# json-todo — Taken opslaan in JSON

> 🎯 **Waarom?** Elke app moet data onthouden, ook na het afsluiten. Dit script bewaart jouw taken in een JSON-bestand — precies zoals een echte to-do app dat doet.

## Wat je leert
- `json` (lezen en schrijven)
- `os` (controleren of een bestand bestaat)
- Bestanden lezen/schrijven met `with open(...)`

## De opdracht
Schrijf een programma met een menu waarmee je:
1. Taken **toont**.
2. Een taak **toevoegt**.
3. Een taak **verwijdert**.
4. Stopt — en de taken **opslaat in `taken.json`**.
5. Bij het opstarten de taken **terug inlaadt** als het bestand bestaat.

## Starten
```bash
python main.py
```

## Tips
- `os.path.exists("taken.json")` checkt of het bestand er is.
- `json.dump(taken, f, indent=2)` schrijft, `json.load(f)` leest.

## Uitdaging
Geef elke taak ook een status (open/gedaan) en sla die mee op.
