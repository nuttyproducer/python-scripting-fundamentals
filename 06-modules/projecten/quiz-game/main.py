"""quiz-game — een quiz met score en timer."""

import random
import time

VRAGEN = [
    ("Wat is de hoofdstad van België?", "brussel"),
    ("Hoeveel is 7 * 8?", "56"),
    ("Welke programmeertaal leren we hier?", "python"),
]


def stel_vraag(vraag, antwoord):
    """Stelt de vraag en geeft True terug bij een correct antwoord."""
    # TODO: lees het antwoord in, strip en lowercase het, en vergelijk
    ...


def main():
    # TODO: shuffle de vragen
    # TODO: onthoud de starttijd (time.time())
    # TODO: loop over de vragen, hou de score bij
    # TODO: print score en verstreken tijd
    ...


if __name__ == "__main__":
    main()
