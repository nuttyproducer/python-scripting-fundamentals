"""streamer-payout — bereken bruto en netto inkomsten van een streamer."""

PER_1000_VIEWS = 3.0   # € per 1000 views
PLATFORM_CUT = 0.30     # 30% voor het platform
BELASTING = 0.25        # 25% belasting

views = int(input("Hoeveel views had de streamer deze maand? "))

bruto = views / 1000 * PER_1000_VIEWS
netto = bruto * (1 - PLATFORM_CUT) * (1 - BELASTING)

print(f"Bruto inkomsten: €{bruto:,.2f}")
print(f"Netto inkomsten: €{netto:,.2f}")
