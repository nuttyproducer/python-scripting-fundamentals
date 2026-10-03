"""creator-commissie — bereken netto inkomsten per platform."""

YOUTUBE_CUT = 0.45
TWITCH_CUT = 0.50
TIKTOK_CUT = 0.50


def netto(bruto, cut):
    """Geeft het netto bedrag terug na aftrek van de cut."""
    # TODO: return bruto * (1 - cut)
    ...


def youtube(bruto):
    # TODO: return netto(bruto, YOUTUBE_CUT)
    ...


def twitch(bruto):
    # TODO: return netto(bruto, TWITCH_CUT)
    ...


def tiktok(bruto):
    # TODO: return netto(bruto, TIKTOK_CUT)
    ...


def main():
    # TODO: lees de bruto inkomsten per platform in
    # TODO: tel alle netto bedragen op en print het totaal
    ...


if __name__ == "__main__":
    main()
