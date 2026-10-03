"""bestelsysteem — een mini-webshop met validatie en berekeningen."""

GRATIS_VERZENDING_VANAF = 50
VERZENDKOSTEN = 5.99


def valideer_aantal(aantal):
    """Geeft True als het aantal groter is dan 0."""
    return aantal > 0


def bereken_subtotaal(prijs, aantal):
    return prijs * aantal


def bereken_verzendkosten(subtotaal):
    return 0 if subtotaal >= GRATIS_VERZENDING_VANAF else VERZENDKOSTEN


def main():
    prijs = float(input("Prijs van het product (€)? "))
    aantal = int(input("Aantal? "))

    if not valideer_aantal(aantal):
        print("Ongeldig aantal. Het aantal moet groter zijn dan 0.")
        return

    subtotaal = bereken_subtotaal(prijs, aantal)
    verzending = bereken_verzendkosten(subtotaal)
    totaal = subtotaal + verzending

    print(f"Subtotaal: €{subtotaal:.2f}")
    print(f"Verzendkosten: €{verzending:.2f}")
    print(f"Totaal: €{totaal:.2f}")


if __name__ == "__main__":
    main()
