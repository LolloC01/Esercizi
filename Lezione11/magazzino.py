
'''Scrivi un programma in Python che gestisca un magazzino. 
Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.'''

class Prodotto:

    def __init__(self, nome, quantita) -> None:
        self.nome = nome
        self.quantita = quantita


class Magazzino:

    def __init__(self) -> None:
        self.prodotti: list[Prodotto] = []

    def aggiungi_prodotto(self, prodotto: Prodotto) -> None:
        self.prodotti.append(prodotto)

    def cerca_prodotto(self, nome: str) -> Prodotto:
        for x in self.prodotti:
            if x.nome == nome:
                return x

    def verifica_disponibilita(self, nome: str) -> str:
        x = self.cerca_prodotto(nome)
        if x.quantita != 0:
            return "PRODOTTO DISPONIBILE"
        return "PRODOTTO NON DiSPONIBILE"
    