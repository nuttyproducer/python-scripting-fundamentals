"""wachtwoordgenerator — genereer een wachtwoord en beoordeel de sterkte."""

import random
import string

KARAKTERS = string.ascii_letters + string.digits + string.punctuation


def genereer(lengte):
    """Geeft een willekeurig wachtwoord van de gegeven lengte terug."""
    # TODO: bouw een string van `lengte` willekeurige karakters
    ...


def sterkte(wachtwoord):
    """Geeft 'zwak', 'matig' of 'sterk' terug op basis van de lengte."""
    # TODO: < 8 → zwak, < 12 → matig, anders sterk
    ...


def main():
    # TODO: lees de lengte in, controleer min 4
    # TODO: genereer en print het wachtwoord + sterkte
    ...


if __name__ == "__main__":
    main()
