"""crypto-calculator — bereken de totale waarde van je portfolio."""

# BTC
btc_aantal = float(input("Hoeveel BTC heb je? "))
btc_prijs = float(input("Wat is de huidige prijs van BTC (€)? "))
btc_waarde = btc_aantal * btc_prijs

# ETH
eth_aantal = float(input("Hoeveel ETH heb je? "))
eth_prijs = float(input("Wat is de huidige prijs van ETH (€)? "))
eth_waarde = eth_aantal * eth_prijs

# DOGE
doge_aantal = float(input("Hoeveel DOGE heb je? "))
doge_prijs = float(input("Wat is de huidige prijs van DOGE (€)? "))
doge_waarde = doge_aantal * doge_prijs

totaal = btc_waarde + eth_waarde + doge_waarde

print(f"\nBTC: €{btc_waarde:,.2f}")
print(f"ETH: €{eth_waarde:,.2f}")
print(f"DOGE: €{doge_waarde:,.2f}")
print(f"\nTotale portfoliowaarde: €{totaal:,.2f}")

investering = float(input("\nHoeveel heb je in totaal geïnvesteerd (€)? "))
winst = totaal - investering
pct = winst / investering * 100
print(f"Winst/verlies: €{winst:,.2f} ({pct:+.2f}%)")
