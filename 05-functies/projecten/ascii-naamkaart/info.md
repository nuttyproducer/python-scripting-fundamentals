# ascii-naamkaart — Jouw digitale visitekaart

> 🎯 **Waarom?** ASCII-art is de oervorm van "cool" in de terminal. Dit script tekent een kader rond tekst — dezelfde techniek zit achter talloze terminal-tools en generators.

## Wat je leert
- Functies schrijven en aanroepen
- Strings vermenigvuldigen (`"-" * 20`)
- Tekst uitlijnen met f-strings

## De opdracht
Schrijf een functie `kaart(lijnen)` die een tekstkader rond een lijst van lijnen tekent, bijvoorbeeld:

```
------------------
| Lotte Peeters  |
| 21 · Brussel   |
------------------
```

## Tips
- Bereken de breedte op basis van de **langste** lijn.
- `"-" * breedte` maakt een horizontale lijn.
- Gebruik `{lijn:<breedte}` om tekst links uit te lijnen.

## Uitdaging
Zorg dat het kader automatisch breder wordt dan de langste regel (marge inbouwen).
