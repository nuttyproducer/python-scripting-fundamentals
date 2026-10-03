# streaming-analyzer — Data doorgronden met pandas

> 🎯 **Waarom?** Een creator-agency analyseert constant cijfers van streamers. Dit script leest een CSV en trekt er de belangrijkste inzichten uit met pandas.

## Wat je leert
- `pd.read_csv()`
- `groupby`, `agg`, `sort_values`
- `mean`, `max`, `describe`

## De opdracht
Schrijf een programma dat de dataset `../../data/streams.csv` inlaadt en:
1. De **top 3 streamers** toont op totale views.
2. De **gemiddelde** en **maximale** views over alle rijen berekent.
3. Een samenvatting toont met `describe()`.

## Starten
```bash
python main.py
```

> ⚠️ Voer het script uit **vanuit deze project-map** (de CSV staat twee mappen hoger).

## Tips
- `df.groupby("naam")["views"].sum().sort_values(ascending=False)`.
- `df["views"].mean()` en `df["views"].max()`.

## Uitdaging
Toon ook per streamer de gemiddelde donaties.
