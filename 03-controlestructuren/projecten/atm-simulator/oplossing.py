"""atm-simulator — een eenvoudige geldautomaat."""

PIN = "1234"
SALDO = 1000

saldo = SALDO
geblokkeerd = False

# PIN-check met maximaal 3 pogingen
for poging in range(3):
    ingevoerd = input("Geef je PIN: ")
    if ingevoerd == PIN:
        break
    print(f"Foute PIN. Nog {2 - poging} pogingen.")
else:
    print("Te veel foute pogingen. Kaart geblokkeerd.")
    geblokkeerd = True

# Hoofdmenu
if not geblokkeerd:
    while True:
        print("\n--- Menu ---")
        print("1) Saldo")
        print("2) Storten")
        print("3) Afhalen")
        print("4) Stoppen")

        keuze = input("Kies een optie: ")

        if keuze == "1":
            print(f"Je saldo is €{saldo:.2f}")
        elif keuze == "2":
            bedrag = float(input("Hoeveel wil je storten (€)? "))
            saldo += bedrag
            print(f"Nieuw saldo: €{saldo:.2f}")
        elif keuze == "3":
            bedrag = float(input("Hoeveel wil je afhalen (€)? "))
            if bedrag > saldo:
                print("Saldo ontoereikend.")
            else:
                saldo -= bedrag
                print(f"Nieuw saldo: €{saldo:.2f}")
        elif keuze == "4":
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")
