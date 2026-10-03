"""crypto-portfolio-tracker — beheer je munten in een dictionary."""

portfolio = {}  # munt -> aantal

while True:
    print("\n--- Portfolio Tracker ---")
    print("1) Munt toevoegen  2) Munt verwijderen")
    print("3) Portfolio tonen 4) Totale waarde  5) Stoppen")

    keuze = input("Kies een optie: ")

    if keuze == "1":
        munt = input("Welke munt? (bv. BTC) ").upper()
        aantal = float(input(f"Hoeveel {munt} heb je? "))
        portfolio[munt] = aantal
        print(f"{aantal} {munt} toegevoegd.")
    elif keuze == "2":
        munt = input("Welke munt wil je verwijderen? ").upper()
        if munt in portfolio:
            del portfolio[munt]
            print(f"{munt} verwijderd.")
        else:
            print(f"{munt} staat niet in je portfolio.")
    elif keuze == "3":
        if not portfolio:
            print("Je portfolio is leeg.")
        else:
            for munt, aantal in portfolio.items():
                print(f"  {munt}: {aantal}")
    elif keuze == "4":
        totaal = 0.0
        for munt, aantal in portfolio.items():
            prijs = float(input(f"Wat is de huidige prijs van {munt} (€)? "))
            totaal += aantal * prijs
        print(f"Totale waarde: €{totaal:,.2f}")
    elif keuze == "5":
        print("Tot ziens!")
        break
    else:
        print("Ongeldige keuze, probeer opnieuw.")
