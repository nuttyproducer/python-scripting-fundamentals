"""rekening-splitter — verdeel de rekening eerlijk onder vrienden."""

rekening = float(input("Hoeveel bedraagt de rekening (€)? "))
personen = int(input("Met hoeveel personen zijn jullie? "))
fooi_pct = float(input("Hoeveel fooi wil je geven (%)? "))

totaal = rekening + rekening * fooi_pct / 100
per_persoon = totaal / personen
rest = totaal - (per_persoon * personen)

print(f"\nTotaal (incl. fooi): €{totaal:.2f}")
print(f"Per persoon: €{per_persoon:.2f}")
print(f"Restje dat overblijft: €{rest:.2f}")
