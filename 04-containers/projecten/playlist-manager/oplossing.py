"""playlist-manager — beheer je eigen playlist."""

playlist = []

while True:
    print("\n--- Playlist Manager ---")
    print("1) Toevoegen  2) Verwijderen  3) Tonen")
    print("4) Sorteren   5) Omkeren     6) Stoppen")

    keuze = input("Kies een optie: ")

    if keuze == "1":
        nummer = input("Welk nummer wil je toevoegen? ")
        if nummer not in playlist:
            playlist.append(nummer)
            print(f"'{nummer}' toegevoegd.")
        else:
            print(f"'{nummer}' staat er al in.")
    elif keuze == "2":
        nummer = input("Welk nummer wil je verwijderen? ")
        if nummer in playlist:
            playlist.remove(nummer)
            print(f"'{nummer}' verwijderd.")
        else:
            print(f"'{nummer}' staat niet in de playlist.")
    elif keuze == "3":
        if not playlist:
            print("De playlist is leeg.")
        else:
            for index, nummer in enumerate(playlist, start=1):
                print(f"  {index}. {nummer}")
    elif keuze == "4":
        playlist.sort()
        print("Playlist gesorteerd.")
    elif keuze == "5":
        playlist.reverse()
        print("Playlist omgekeerd.")
    elif keuze == "6":
        print("Tot ziens!")
        break
    else:
        print("Ongeldige keuze, probeer opnieuw.")
