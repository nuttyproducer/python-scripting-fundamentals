"""gok-odds-calculator — bereken kans en uitbetaling op basis van odds."""

odds = float(input("Wat zijn de odds? (bv. 2.50) "))
inzet = float(input("Hoeveel wil je inzetten (€)? "))

kans = (1 / odds) * 100
uitbetaling = inzet * odds

print(f"Implied probability: {kans:.1f}%")
print(f"Mogelijke uitbetaling: €{uitbetaling:.2f}")
