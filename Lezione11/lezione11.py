'''Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. 
Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.

Classi:
- Film: Rappresenta un film con titolo e durata.
- Sala: Rappresenta una sala con numero identificativo, 
film attualmente in programmazione, posti totali, posti prenotati.

    Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti 
    nella sala, se disponibili. 
    Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora 
    disponibili nella sala.
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

    Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato 
    e tenta di prenotare posti. 
    Restituisce un messaggio di stato.

Test case:
- Un gestore del cinema configura le sale aggiungendo i 
film e i dettagli dei posti.'''
from cinema import Film, Sala, Cinema
film = []
film1 = Film("Iron Man", 126)
film2 = Film("Matrix", 136)
film3 = Film("Man in Black", 98)
film4 = Film("Top Gun", 109)
film5 = Film("Hunger Games", 142)
film.append(film1)
film.append(film2)
film.append(film3)
film.append(film4)
film.append(film5)
lux = Cinema()
for x in range(5):
    sala = Sala(x,film[x],50)
    lux.aggiungi_sala(sala)
lux.cinema_view()
'''
- Un cliente sceglie un film e prenota un certo numero di posti.
'''
print(lux.prenota_film("Top Gun", 23))
print(lux.prenota_film("Top Gun", 50))

lux.cinema_view()
"""
- Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione."""