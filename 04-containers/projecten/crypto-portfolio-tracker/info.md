# crypto-portfolio-tracker — Je munten beheren

> 🎯 **Waarom?** Elke crypto-app houdt een portefeuille bij als een lijst van "munt → aantal". Dit script is jouw eigen tracker, gebouwd op een dictionary.

## Wat je leert
- Werken met `dict` (toevoegen, verwijderen, doorlopen)
- `while`-lus met een menu
- `dict.items()` doorlopen

## De opdracht
Schrijf een programma met een menu waarmee je:
1. Een munt **toevoegt** (naam + aantal).
2. Een munt **verwijdert**.
3. Het volledige **portfolio toont**.
4. De **totale waarde** berekent: vraag per munt de prijs op en tel alles op.
5. Stopt.

## Starten
```bash
python main.py
```

## Tips
- Bewaar het portfolio als een `dict`: `{"BTC": 0.5, ...}`.
- Gebruik `dict.get(naam)` of `if naam in portfolio` om veilig te checken.

## Uitdaging
Vraag bij het toevoegen ook de aankoopprijs en toon per munt de winst/verlies.
