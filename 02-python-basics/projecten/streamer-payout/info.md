# streamer-payout — Bruto → netto inkomsten

> 🎯 **Waarom?** Creators verdienen bruto, maar krijgen netto. Het platform neemt een cut, de fiscus neemt een deel. Dit script rekent uit wat er écht overblijft.

## Wat je leert
- Percentages en floats
- F-strings met 2 decimalen

## De opdracht
Schrijf een programma dat:
1. Het aantal views van een streamer inleest (int).
2. De **bruto** inkomsten berekent: €3 per 1000 views.
3. De **platform-cut van 30%** aftrekt.
4. Van wat overblijft nog eens **25% belasting** aftrekt.
5. Bruto én netto afdrukt met 2 decimalen.

## Starten
```bash
python main.py
```

## Tips
- `netto = bruto * (1 - 0.30) * (1 - 0.25)`.

## Uitdaging
Vraag de platform-cut en het belastingtarief als invoer i.p.v. vaste waarden.
