# crypto-calculator — Portfolio-waarde berekenen

> 🎯 **Waarom?** Crypto- en beleggings-apps tonen constant je portfoliowaarde. Dit script doet exact hetzelfde: bezit × prijs = waarde.

## Wat je leert
- `input()` en typeconversies (`float`)
- Rekenen en f-strings met duizendtallen (`{x:,.2f}`)

## De opdracht
Schrijf een programma dat voor 3 munten (BTC, ETH, DOGE):
1. Het aantal (float) en de huidige prijs (float) inleest.
2. De waarde per munt berekent en het **totaal** afdrukt.
3. Vraagt wat je **in totaal geïnvesteerd** hebt en de winst/verlies afdrukt (in € én %).

## Starten
```bash
python main.py
```

## Tips
- `{waarde:,.2f}` geeft duizendtallen en 2 decimalen.
- Winst% = (huidig − investering) / investering × 100.

## Uitdaging
Laat de gebruiker ook per munt het geïnvesteerde bedrag invullen en bereken de winst/verlies per munt apart.
