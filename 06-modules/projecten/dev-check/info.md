# dev-check — Je omgeving checken

> 🎯 **Waarom?** Elke developer checkt eerst of z'n omgeving klopt. Dit script doet dat automatisch — alsof je een health-check bouwt voor je eigen machine.

## Wat je leert
- Modules importeren (`sys`, `importlib.util`)
- Werken met lijsten en een `for`-lus
- Nette output met f-strings

## De opdracht
Schrijf een programma dat:
1. De huidige **Python-versie** afdrukt.
2. Voor een vaste lijst pakketten (`jupyter`, `pandas`, `matplotlib`, `seaborn`) controleert of ze geïnstalleerd zijn.
3. Per pakket `✅` of `❌` afdrukt, netjes uitgelijnd.

## Starten
```bash
python main.py
```

## Tips
- `importlib.util.find_spec("pandas")` geeft `None` terug als het pakket ontbreekt.
- Gebruik een f-string om de kolommen uit te lijnen (bv. `{pakket:<12}`).

## Uitdaging
Tel het aantal ontbrekende pakketten en druk een "rapportcijfer" af (bv. `3/4 geïnstalleerd`).
