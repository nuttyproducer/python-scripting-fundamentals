"""quiz-game — een quiz met score en timer."""

import random
import time

VRAGEN = [
    ("Wat is de hoofdstad van België?", "brussel"),
    ("Hoeveel is 7 * 8?", "56"),
    ("Welke programmeertaal leren we hier?", "python"),
]


def stel_vraag(vraag, antwoord):
    invoer = input(vraag + " ").strip().lower()
    return invoer == antwoord


def main():
    random.shuffle(VRAGEN)
    score = 0
    start = time.time()

    for vraag, antwoord in VRAGEN:
        if stel_vraag(vraag, antwoord):
            print("Correct!\n")
            score += 1
        else:
            print(f"Fout! Het antwoord was '{antwoord}'.\n")

    verstreken = time.time() - start
    print(f"Score: {score}/{len(VRAGEN)} in {verstreken:.1f} seconden.")


if __name__ == "__main__":
    main()
