"""json-todo — een takenlijst die bewaard wordt in een JSON-bestand."""

import json
import os

BESTAND = "taken.json"


def laden():
    if not os.path.exists(BESTAND):
        return []
    with open(BESTAND, "r", encoding="utf-8") as f:
        return json.load(f)


def opslaan(taken):
    with open(BESTAND, "w", encoding="utf-8") as f:
        json.dump(taken, f, indent=2)


def main():
    taken = laden()

    while True:
        print("\n--- Taken ---")
        print("1) Tonen  2) Toevoegen  3) Verwijderen  4) Stoppen")

        keuze = input("Kies een optie: ")

        if keuze == "1":
            if not taken:
                print("Geen taken.")
            for index, taak in enumerate(taken, start=1):
                print(f"  {index}. {taak}")
        elif keuze == "2":
            taak = input("Welke taak wil je toevoegen? ")
            taken.append(taak)
            opslaan(taken)
            print("Taak toegevoegd.")
        elif keuze == "3":
            index = int(input("Welk nummer wil je verwijderen? "))
            if 1 <= index <= len(taken):
                verwijderd = taken.pop(index - 1)
                opslaan(taken)
                print(f"'{verwijderd}' verwijderd.")
            else:
                print("Ongeldig nummer.")
        elif keuze == "4":
            opslaan(taken)
            print("Taken opgeslagen. Tot ziens!")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")


if __name__ == "__main__":
    main()
