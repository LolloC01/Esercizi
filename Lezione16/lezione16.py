class Media:
    def __init__(self) -> None:
        self.title = None
        self.reviews = []

    def set_title(self, title):
        self.title = title
    def get_title(self):
        return self.title
    def aggiungiValutazione(self, voto):
        if 1 <= voto <= 5:
            self.reviews.append(voto)
    def getMedia(self):
        media = 0
        for x in self.reviews:
            media += x
        media /= len(self.reviews)
        return media
    def getRate(self):
        if self.getMedia() <= 1:
            return "Terribile"
        elif self.getMedia() <= 2:
            return "Brutto"
        elif self.getMedia() <= 3:
            return "Normale"
        elif self.getMedia() <= 4:
            return "Bello"
        elif self.getMedia() <= 5:
            return "Grandioso"
    def ratePercentage(self, voto):
        count = 0
        for x in self.reviews:
            if x == voto:
                count += 1
        return count/len(self.reviews)*100
    def recensione(self):
        s =  f"""Titolo del Film: {self.get_title()}\n\
Voto Medio: {self.getMedia()}\n\
Giudizio: {self.getRate()}\n\
Terribile: {self.ratePercentage(1)}%\n\
Brutto: {self.ratePercentage(2)}%\n\
Normale: {self.ratePercentage(3)}%\n\
Bello: {self.ratePercentage(4)}%\n\
Grandioso: {self.ratePercentage(5)}%"""
        return s


film1 = Media()
film1.set_title("IRON MAN")
film1.aggiungiValutazione(1)
film1.aggiungiValutazione(2)
film1.aggiungiValutazione(3)
film1.aggiungiValutazione(4)
film1.aggiungiValutazione(4)
film1.aggiungiValutazione(4)
film1.aggiungiValutazione(5)
film1.aggiungiValutazione(5)
film1.aggiungiValutazione(5)
film1.aggiungiValutazione(5)

print(film1.recensione())
film2 = Media()
film2.set_title("SUPER MAN")
film2.aggiungiValutazione(1)
film2.aggiungiValutazione(2)
film2.aggiungiValutazione(5)
film2.aggiungiValutazione(4)
film2.aggiungiValutazione(2)
film2.aggiungiValutazione(2)
film2.aggiungiValutazione(3)
film2.aggiungiValutazione(1)
film2.aggiungiValutazione(2)
film2.aggiungiValutazione(5)

print(film2.recensione())