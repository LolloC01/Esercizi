class Film:

    def __init__(self, titolo, durata) -> None:
        self.titolo: str = titolo
        self.durata: int = durata

    def __str__(self) -> str:
        return f"Titolo: {self.titolo}\n\tDurata: {self.durata}"

class Sala:

    def __init__(self, id_num, film, posti_tot) -> None:
        self.id: int = id_num
        self.film: Film = film
        self.posti_tot: int = posti_tot
        self.posti_prenotati = 0

    def prenota_posti(self, num_prenotati) -> str:
        if num_prenotati <= self.posti_disponibili():
            self.posti_prenotati += num_prenotati
            return "POSTI PRENOTATI CORRETTAMENTE"
        return "NUMERO DI POSTI NON DISPONIBILE"

    def posti_disponibili(self) -> int:
        return self.posti_tot - self.posti_prenotati
    
    def __str__(self) -> str:
        return f"Sala: {self.id}\nPosti: {self.posti_disponibili()}\nFILM:\n\t{self.film.__str__()}"


class Cinema:

    def __init__(self) -> None:
        self.sale: list[Sala] = []
    
    def aggiungi_sala(self, sala) -> None:
        self.sale.append(sala)

    def prenota_film(self, titolo_film, num_posti) -> str:
        for x in self.sale:
            if x.film.titolo == titolo_film:
                return x.prenota_posti(num_posti)
        return "FILM NON PRESENTE"

    def cinema_view(self) -> None:
        for x in self.sale:
            print(x.__str__())