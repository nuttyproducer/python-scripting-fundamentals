"""ascii-naamkaart — teken een kader rond jouw profiel."""


def kaart(lijnen):
    # 2 spaties marge langs elke kant
    breedte = max([len(lijn) for lijn in lijnen]) + 4
    rand = "-" * breedte

    print(rand)
    for lijn in lijnen:
        print(f"| {lijn:<{breedte - 2}} |")
    print(rand)


def main():
    profiel = [
        "Lotte Peeters",
        "21 · Brussel",
    ]
    kaart(profiel)


if __name__ == "__main__":
    main()
