# follower-analyzer — Wie volgt jou waar?

> 🎯 **Waarom?** Creators willen weten wie hen op meerdere platformen volgt. Met set-operaties vind je in één klap de overlappende én unieke volgers.

## Wat je leert
- Werken met `set` en verzamelingenleer
- Unie (`|`), doorsnede (`&`), verschil (`-`)

## De opdracht
Schrijf een programma dat met twee lijsten volgers (TikTok en Instagram):
1. Beide lijsten omzet naar een `set` (duplicaten verdwijnen vanzelf).
2. De **gedeelde** volgers toont (doorsnede).
3. De volgers toont die **maar op één** platform zitten (symmetrisch verschil `^`).
4. Het **totaal aantal unieke** volgers toont (unie).

## Starten
```bash
python main.py
```

## Tips
- `a & b` → doorsnede, `a | b` → unie, `a ^ b` → symmetrisch verschil.

## Uitdaging
Laat de gebruiker zelf de twee lijsten invullen (één naam per regel, stop met een lege regel).
