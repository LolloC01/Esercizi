import lezione4_2 as es


############        ESERCIZIO 1


'''students: list = []
while True:
    s: str = input("Inserisci il nome dello studente (premi 0 per terminare): ")
    if s == "0":
        break
    else:
        students.append(s)
for s in students:
    votes: list = []
    while True:
        x: int = int(input(f"Inserisci i voti dello studente {s}(premi 0 per terminare): "))
        if x == 0:
            break
        else:
            votes.append(x)
    es.average_score(s,votes)'''


############        ESERCIZIO 2


'''es.game(es.rand(1,10),10)'''


############        ESERCIZIO 3


'''
carrello: list = []
while True:
    print("Cosa vuoi fare? \
          \n(1 per inserire un prodotto nel carrello)\
          \n(2 per eliminare il prodotto)\
          \n(3 per visualizzare il totale)\
          \n(4 per visualizzare il carrello\
          \n(0 per terminare)")
    x: int = int(input())
    if x == 0:
        break
    elif x == 3:
        disc: float = float(input("inserisci la percentuale di sconto: "))
        es.cart(carrello, x, disc)
    else: 
        es.cart(carrello, x)
'''


############        ESERCIZIO 4


file: str = 'Lezione4/text.txt'
es.analysis(file)


############        ESERCIZIO 5

inventario: list = []
while True:
    print("Cosa vuoi fare? \
          \n(1 per inserire un item nell'inventario)\
          \n(2 per eliminare un item)\
          \n(3 per visualizzare l'inventario)\
          \n(4 per cercare elementi nell'inventario)\
          \n(5 per update l'inventario)\
          \n(0 per terminare)")
    x: int = int(input())
    if x == 0:
        break
    elif x == 1:
        codice: str = input("Inserisci il codice dell'item: ")
        nome: str = input("Inserisci il nome del'item': ")
        prezzo: float = float(input("Inserisci il prezzo dell'item: "))
        quantita: int = int(input("Inserisci la quantità dell'item: "))
        item: dict = es.item(codice,nome, quantita, prezzo)
        es.add_item(item, inventario)
        print(inventario)
    elif x == 2:
        pass
    elif x == 3:
        pass
    elif x == 4:
        pass
    elif x == 5:
        pass


############        ESERCIZIO 6
############        ESERCIZIO 7
############        ESERCIZIO 8
############        ESERCIZIO 9
############        ESERCIZIO 10
############        ESERCIZIO 11
############        ESERCIZIO 12
############        ESERCIZIO 13
############        ESERCIZIO 14
############        ESERCIZIO 15