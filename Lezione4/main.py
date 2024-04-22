import lezione4

es = 1
while es != 0:
    print("Che esercizio vuoi eseguire?")
    print("8.1 - 8.2 - 8.3 - 8.4 - 8.5 - 8.6 - 8.7 - 8.8 - 8.9 - 8.101 - 8.11 - 8.12 - 8.14 - 8.15")
    print("Inserisci 0 per uscire")
    es: float = float(input("inserisci l'esercizio: \n"))

    if es == 8.1:
        lezione4.display_message()
    elif es == 8.2:
        lezione4.fav_book(title = "Il signore degli anelli")
    elif es == 8.3:
        taglia: str = "XXL"
        testo: str = "DAJE ROMA DAJE"
        lezione4.make_shirt(taglia, testo)
        lezione4.make_shirt(size = taglia, text = testo)
    elif es == 8.4:
        taglia: str = "XXL"
        testo: str = "DAJE ROMA DAJE"
        lezione4.make_shirt_1(taglia, testo)
        lezione4.make_shirt_1()
        lezione4.make_shirt_1("M")
    elif es == 8.5:
        lezione4.describe_city("Roma")
        lezione4.describe_city("Milano")
        lezione4.describe_city("Miami", "USA")
    elif es == 8.6:
        citta: str = "Roma"
        paese: str = "Italia"
        print(lezione4.city_country(citta,paese))
        citta: str = "Parigi"
        paese: str = "Francia"
        print(lezione4.city_country(citta,paese))
        citta: str = "Londra"
        paese: str = "Regno Unito"
        print(lezione4.city_country(citta,paese))
