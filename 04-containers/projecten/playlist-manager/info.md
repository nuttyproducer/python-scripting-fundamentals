# playlist-manager — Beheer je muziek

> 🎯 **Waarom?** Spotify, Apple Music, YouTube — allemaal draaien ze op lijsten van nummers. Dit script is jouw eigen playlist-beheerder in de terminal.

## Wat je leert
- Werken met `list` (add, remove, sort, reverse)
- `while`-lus met een menu
- List-methodes zoals `append`, `remove`, `sort`, `reverse`

## De opdracht
Schrijf een programma met een menu waarmee je:
1. Een nummer **toevoegt** aan de playlist.
2. Een nummer **verwijdert**.
3. De playlist **toont** (met nummers).
4. De playlist **sorteert** (alfabetisch).
5. De playlist **omkeert** (gebruik `reverse`).
6. Stopt.

## Starten
```bash
python main.py
```

## Tips
- `reverse()` keert de volgorde van de lijst **in-place** om.
- Toon de playlist telkens met een `for`-lus en `enumerate`.

## Uitdaging
Zorg dat je geen dubbels kan toevoegen (check eerst met `in`).
