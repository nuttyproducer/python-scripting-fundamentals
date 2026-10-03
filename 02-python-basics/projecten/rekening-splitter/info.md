# rekening-splitter — Eerlijk de rekening delen

> 🎯 **Waarom?** Wie betaalt wat als je met vrienden uit eten gaat? Dit script lost de klassieke "split the bill"-discussie voor je op.

## Wat je leert
- `//` (gehele deling) en `%` (rest)
- F-strings en floats

## De opdracht
Schrijf een programma dat:
1. De rekening (float) en het aantal personen (int) inleest.
2. Optioneel een fooi-percentage inleest en bij de rekening telt.
3. Bereken wat ieder betaalt (2 decimalen).
4. Toon ook het "oneerlijke" restje dat overblijft als het bedrag niet exact deelbaar is.

## Starten
```bash
python main.py
```

## Tips
- `fooi = rekening * fooi_pct / 100`.
- `rest = totaal - (per_persoon * personen)`.

## Uitdaging
Rond het bedrag per persoon naar boven af naar de dichtste 10 cent.
