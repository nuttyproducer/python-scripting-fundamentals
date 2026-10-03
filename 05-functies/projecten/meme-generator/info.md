# meme-generator — ASCII-memes maken

> 🎯 **Waarom?** Memes zijn de taal van het internet. Deze generator bouwt klassieke "top text / bottom text"-memes in ASCII — dezelfde structuur als echte meme-generators, maar dan in de terminal.

## Wat je leert
- Functies met parameters en `return`
- Strings manipuleren (`upper`, `center`)
- Functies die samenwerken

## De opdracht
Schrijf functies waarmee je een meme bouwt:
1. `meme(boven, onder, breedte=32)` die een kader tekent met de **boven-tekst**, een lege "image"-regel (met een ASCII-gezichtje), en de **onder-tekst**, alles in HOOFDLETTERS en gecentreerd.
2. Vraag in `main` de twee teksten op en roep `meme` aan.

## Starten
```bash
python main.py
```

## Tips
- `tekst.upper()` zet om naar hoofdletters, `tekst.center(breedte)` centreert.
- `"=" * breedte` maakt een horizontale rand.

## Uitdaging
Laat de gebruiker de breedte kiezen en toon een fout als de tekst te lang is.
