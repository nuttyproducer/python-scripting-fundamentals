"""json-todo — een takenlijst die bewaard wordt in een JSON-bestand."""

import json
import os

BESTAND = "taken.json"


def laden():
    """Geeft de lijst taken terug (of een lege lijst als het bestand er niet is)."""
    # TODO: als het bestand niet bestaat, geef [] terug
    # TODO: anders lees en return json.load(f)
    ...


def opslaan(taken):
    """Schrijft de taken weg naar het JSON-bestand."""
    # TODO: open het bestand in 'w'-modus en json.dump de taken
    ...


def main():
    taken = laden()

    while True:
        print("\n--- Taken ---")
        print("1) Tonen  2) Toevoegen  3) Verwijderen  4) Stoppen")

        keuze = input("Kies een optie: ")

        # TODO: verwerk elke keuze en roep opslaan(taken) aan waar nodig
        ...


if __name__ == "__main__":
    main()
