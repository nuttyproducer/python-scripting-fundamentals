"""ascii-naamkaart — teken een kader rond jouw profiel."""


def kaart(lijnen):
    """Tekent een kader rond de gegeven tekstlijnen."""
    # TODO: bereken de breedte (langste lijn + wat marge)
    # TODO: print de bovenrand, elke lijn met "|  |" eromheen, en de onderrand
    ...


def main():
    profiel = [
        "Lotte Peeters",
        "21 · Brussel",
    ]
    kaart(profiel)


if __name__ == "__main__":
    main()
