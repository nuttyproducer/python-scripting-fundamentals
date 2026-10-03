# casino-age-gate — De toegangspoort

> 🎯 **Waarom?** Elke goksite en app met een leeftijdsgrens heeft een toegangscheck. Dit script bouwt zo'n gate: leeftijd + zelfuitsluiting.

## Wat je leert
- `if` / `elif` / `else`
- Geneste `if`
- `input()` met typeconversie

## De opdracht
Schrijf een programma dat:
1. De leeftijd van de gebruiker inleest (int).
2. Controleert of die **minstens 21** is.
3. Vraagt of de gebruiker zichzelf heeft uitgesloten (`j`/`n`).
4. Print `Toegang toegestaan` of een duidelijke weigering (te jong / uitgesloten).

## Starten
```bash
python main.py
```

## Tips
- Geneste `if`: eerst de leeftijd checken, pas daarna de zelfuitsluiting.
- Test minstens 3 scenario's (21+ én niet uitgesloten, te jong, uitgesloten).

## Uitdaging
Laat de gebruiker 3 keer proberen en blokkeer daarna.
