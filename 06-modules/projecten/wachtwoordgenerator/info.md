# wachtwoordgenerator — Veilige wachtwoorden

> 🎯 **Waarom?** Iedereen heeft sterke wachtwoorden nodig. Dit script genereert ze én beoordeelt de sterkte — net zoals een wachtwoordmanager.

## Wat je leert
- `random` en `string`
- Functies
- `if` / `elif` (sterkte bepalen)

## De opdracht
Schrijf een programma dat:
1. Een lengte inleest (minstens 4).
2. Een wachtwoord genereert met letters (hoofd + klein), cijfers en symbolen.
3. De sterkte beoordeelt: `zwak` (< 8), `matig` (8–11), `sterk` (≥ 12).
4. Het wachtwoord én de sterkte afdrukt.

## Starten
```bash
python main.py
```

## Tips
- `string.ascii_letters`, `string.digits`, `string.punctuation`.
- `random.choice(karakters)` in een lus.

## Uitdaging
Zorg dat het wachtwoord gegarandeerd minstens één cijfer en één symbool bevat.
