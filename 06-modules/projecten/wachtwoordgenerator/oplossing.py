"""wachtwoordgenerator — genereer een wachtwoord en beoordeel de sterkte."""

import random
import string

KARAKTERS = string.ascii_letters + string.digits + string.punctuation


def genereer(lengte):
    return "".join(random.choice(KARAKTERS) for _ in range(lengte))


def sterkte(wachtwoord):
    if len(wachtwoord) < 8:
        return "zwak"
    elif len(wachtwoord) < 12:
        return "matig"
    return "sterk"


def main():
    lengte = int(input("Hoe lang moet het wachtwoord zijn? "))
    if lengte < 4:
        print("Te kort. Gebruik minstens 4 karakters.")
        return

    wachtwoord = genereer(lengte)
    print(f"Wachtwoord: {wachtwoord}")
    print(f"Sterkte: {sterkte(wachtwoord)}")


if __name__ == "__main__":
    main()
