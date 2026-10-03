# creator-commissie — Netto per platform

> 🎯 **Waarom?** Creators verdienen op YouTube, Twitch én TikTok, maar elk platform neemt een andere cut. Dit script bouwt de "engine" die netto per platform uitrekent — volledig met functies.

## Wat je leert
- Eigen functies schrijven en aanroepen
- Functies die andere functies gebruiken
- Parameters en `return`

## De opdracht
Schrijf functies waarmee je per platform de netto inkomsten berekent:
1. `netto(bruto, cut)` → `bruto * (1 - cut)`.
2. `youtube(bruto)`, `twitch(bruto)` en `tiktok(bruto)` — elk roept `netto` aan met zijn eigen cut (YouTube 45%, Twitch 50%, TikTok 50%).
3. Vraag in `main` de bruto inkomsten per platform op en print het **totale netto**.

## Starten
```bash
python main.py
```

## Tips
- Definieer de cuts als constanten bovenaan (hoofdletters).
- Een functie die `netto` aanroept = **hergebruik**, de kern van dit hoofdstuk.

## Uitdaging
Laat de gebruiker zelf een extra platform (naam + cut) toevoegen.
