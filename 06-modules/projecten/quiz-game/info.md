# quiz-game — Een quiz met score en timer

> 🎯 **Waarom?** Quiz-apps en gamification zitten overal (denk Kahoot, Duolingo). Dit script bouwt een mini-versie: willekeurige vragen, een score en een timer.

## Wat je leert
- `random` (vragen shufflen)
- `time` (timer)
- Lussen en functies

## De opdracht
Schrijf een programma dat:
1. Een lijst met vragen + antwoorden heeft.
2. De vragen **shufflet**.
3. Elke vraag stelt, het antwoord controleert en de score bijhoudt.
4. Aan het einde de score en de verstreken tijd afdrukt.

## Starten
```bash
python main.py
```

## Tips
- Bewaar vragen als tuples: `("Vraag?", "antwoord")`.
- `random.shuffle(vragen)` schudt in-place.
- Meet de tijd met `time.time()` (begin en einde) of `datetime`.

## Uitdaging
Voeg minstens 5 eigen vragen toe en tel het aantal "correct op eerste poging".
