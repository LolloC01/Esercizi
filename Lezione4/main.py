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
    elif es == 8.7:
        print(lezione4.make_album("Ultimo", "Peter Pan"))
        print(lezione4.make_album("Pignuini Tattici Nucleari", "Scooby Doo"))
        print(lezione4.make_album("Eminem", "Marshall Mother LP", 10))
    elif es == 8.8:
        x: bool = True
        dischi: list =[] 
        while x:
            artist: str = input("inserisci l'artista: ")
            album: str = input("inserisci l'album: ")
            dischi.append(lezione4.make_album(artist, album))
            if input("Inserisci 0 per coninuare o 1 per finire: ") == "0":
                continue
            else:
                break
        print(dischi)
    elif es == 8.9:
        message: list =["ciao", "Hello","Hola"]
        lezione4.show_message(message) 
    elif es == 8.101:
        message: list =["ciao", "Hello","Hola"]
        msg: list =[] 
        msg = lezione4.send_message(message)
        print(msg)
    elif es == 8.11:
        message: list =["ciao", "Hello","Hola"]
        mess_1: list = message
        msg: list =[] 
        msg = lezione4.send_message(mess_1)
        print(msg)
        print(mess_1)
        print(message)
    elif es == 8.12:
        pass
    elif es == 8.13:
        first_name: str = "Lorenzo"
        last_name: str = "Colitto"
        age: int = 23
        weight: int = 90
        height: int = 175
        info: str
        info = lezione4.build_profiler(first_name,last_name,age,weight,height)
        print(info)
    elif es == 8.14:
        pass
    elif es == 8.15:
        pass
    elif es == 8.16:
        pass
    elif es == 8.17:
        pass
