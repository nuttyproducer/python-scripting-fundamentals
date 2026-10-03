# budget-tracker — Je uitgaven visualiseren

> 🎯 **Waarom?** Budget-apps (denk YNAB) tonen je inkomsten en uitgaven in grafieken. Dit script leest een CSV en tekent een staafdiagram.

## Wat je leert
- `pd.read_csv()`
- Een nieuwe kolom berekenen (`netto = inkomsten − uitgaven`)
- `matplotlib` staafdiagram

## De opdracht
Schrijf een programma dat `budget.csv` inlaadt en:
1. Per maand de **netto** = inkomsten − uitgaven berekent.
2. De netto per maand afdrukt.
3. Een **staafdiagram** tekent van de netto per maand (met titel en as-labels).

## Starten
```bash
python main.py
```

## Tips
- `df["netto"] = df["inkomsten"] - df["uitgaven"]`.
- `plt.bar(df["maand"], df["netto"])`.

## Uitdaging
Kleur de maanden met een negatieve netto rood.
