"""bestelsysteem — een mini-webshop met validatie en berekeningen."""

GRATIS_VERZENDING_VANAF = 50
VERZENDKOSTEN = 5.99


def valideer_aantal(aantal):
    """Geeft True als het aantal groter is dan 0."""
    # TODO: return aantal > 0
    ...


def bereken_subtotaal(prijs, aantal):
    # TODO: return prijs * aantal
    ...


def bereken_verzendkosten(subtotaal):
    # TODO: 0 als subtotaal >= GRATIS_VERZENDING_VANAF, anders VERZENDKOSTEN
    ...


def main():
    # TODO: lees prijs en aantal in
    # TODO: valideer het aantal en reken subtotaal, verzendkosten en totaal uit
    # TODO: print alles netjes
    ...


if __name__ == "__main__":
    main()
