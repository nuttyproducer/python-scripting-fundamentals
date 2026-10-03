# crypto-plotter — Prijsgeschiedenis plotten

> 🎯 **Waarom?** Elke exchange toont een prijsgrafiek. Dit script leest een prijsreeks en tekent er een lijngrafiek van — de basis van elke "chart".

## Wat je leert
- `pd.read_csv()`
- `matplotlib` lijngrafiek
- `min` / `max`

## De opdracht
Schrijf een programma dat `prijzen.csv` inlaadt en:
1. De **hoogste** en **laagste** prijs afdrukt.
2. Een **lijngrafiek** tekent van prijs tegen dag (met marker).
3. Een titel en as-labels toevoegt.

## Starten
```bash
python main.py
```

## Tips
- `plt.plot(df["dag"], df["prijs"], marker="o")`.

## Uitdaging
Markeer het hoogste punt met een rode stip.
