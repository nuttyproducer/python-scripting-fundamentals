# gok-odds-calculator — Kans en uitbetaling

> 🎯 **Waarom?** Bookmakers tonen odds, geen percentages. Wie wil wedden, rekent eerst de "implied probability" en de mogelijke uitbetaling uit.

## Wat je leert
- `if` / `elif` (verschillende gevallen afhandelen)
- Float-berekeningen en f-strings

## De opdracht
Schrijf een programma dat:
1. De odds (kommagetal, bv. `2.50`) inleest.
2. De **implied probability** berekent: `1 / odds × 100` (in %).
3. De inzet (float) inleest en de mogelijke **uitbetaling** berekent: `inzet × odds`.
4. Kans (%) en uitbetaling netjes afdrukt.

## Starten
```bash
python main.py
```

## Tips
- Bij odds `2.00` is de kans 50% — gebruik dat om je formule te testen.

## Uitdaging
Ondersteun ook "fractional" odds zoals `5/1`: parse de breuk en reken er dezelfde waarden mee uit.
