# atm-simulator — Een geldautomaat

> 🎯 **Waarom?** Elke geldautomaat is een state-machine met lussen en keuzes. Dit script simuleert er één: PIN-check, saldo, storten en afhalen.

## Wat je leert
- `while`-lus (menu blijft draaien)
- `if` / `elif` (keuzes)
- `break` en `continue`

## De opdracht
Schrijf een programma dat:
1. Een PIN vraagt (max **3 pogingen**, daarna stopt het).
2. Bij correcte PIN een menu toont: `1) saldo`, `2) storten`, `3) afhalen`, `4) stoppen`.
3. Saldo toont, storten verhoogt het saldo, afhalen verlaagt het (weiger als saldo te laag is).
4. Blijft draaien tot de gebruiker kiest voor stoppen.

## Starten
```bash
python main.py
```

## Tips
- Gebruik een `while True:` met een `break` voor het menu.
- Start met een vast saldo van bv. `1000`.

## Uitdaging
Sta bij afhalen enkel veelvouden van 10 toe.
