"""casino-age-gate — controleer leeftijd en zelfuitsluiting."""

MIN_LEEFTIJD = 21

leeftijd = int(input("Hoe oud ben je? "))

if leeftijd < MIN_LEEFTIJD:
    print("Toegang geweigerd: je bent te jong.")
else:
    uitgesloten = input("Heb je jezelf uitgesloten van gokken? (j/n) ").lower()

    if uitgesloten == "j":
        print("Toegang geweigerd: je staat op de zelfuitsluitingslijst.")
    else:
        print("Toegang toegestaan. Speel verantwoord.")
