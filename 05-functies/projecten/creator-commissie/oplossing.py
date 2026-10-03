"""creator-commissie — bereken netto inkomsten per platform."""

YOUTUBE_CUT = 0.45
TWITCH_CUT = 0.50
TIKTOK_CUT = 0.50


def netto(bruto, cut):
    """Geeft het netto bedrag terug na aftrek van de cut."""
    return bruto * (1 - cut)


def youtube(bruto):
    return netto(bruto, YOUTUBE_CUT)


def twitch(bruto):
    return netto(bruto, TWITCH_CUT)


def tiktok(bruto):
    return netto(bruto, TIKTOK_CUT)


def main():
    bruto_yt = float(input("Bruto inkomsten YouTube (€)? "))
    bruto_tw = float(input("Bruto inkomsten Twitch (€)? "))
    bruto_tk = float(input("Bruto inkomsten TikTok (€)? "))

    totaal = youtube(bruto_yt) + twitch(bruto_tw) + tiktok(bruto_tk)

    print(f"Totale netto inkomsten: €{totaal:,.2f}")


if __name__ == "__main__":
    main()
