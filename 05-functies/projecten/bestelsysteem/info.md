# bestelsysteem — Mini-webshop

> 🎯 **Waarom?** Elke webshop draait op kleine functies: valideren, subtotaal berekenen, verzendkosten bepalen. Dit script bouwt die bouwstenen los van elkaar.

## Wat je leert
- Functies met parameters en `return`
- Validatie-logica
- Functies combineren in een grotere flow

## De opdracht
Schrijf drie functies:
1. `valideer_aantal(aantal)` → `True` als het aantal groter is dan 0, anders `False`.
2. `bereken_subtotaal(prijs, aantal)` → `prijs * aantal`.
3. `bereken_verzendkosten(subtotaal)` → `0` als het subtotaal ≥ 50 is, anders `5.99`.

Laat `main` de prijs en het aantal inlezen, valideren, en het subtotaal, de verzendkosten en het totaal afdrukken.

## Starten
```bash
python main.py
```

## Tips
- Gebruik een ternaire operator voor de verzendkosten: `0 if subtotaal >= 50 else 5.99`.

## Uitdaging
Vraag meerdere producten op (met een lus) en tel alle subtotalen op.
