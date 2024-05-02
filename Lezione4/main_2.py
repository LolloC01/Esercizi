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
    elif x == 2:
        ogg: str = input("Inserisci l'item da eliminare: ")
        es.remove_item(ogg, inventario)
    elif x == 3:
        es.show_inventory(inventario)
    elif x == 4:
        ogg: str = input("Inserisci l'item da ricercare: ")
        es.search_item(ogg, inventario)
    elif x == 5:
        codice: str = input("Inserisci il codice dell'item: ")
        nome: str = input("Inserisci il nome del'item': ")
        prezzo: float = float(input("Inserisci il prezzo dell'item: "))
        quantita: int = int(input("Inserisci la quantità dell'item: "))
        item: dict = es.item(codice,nome, quantita, prezzo)
        es.update_items(item, inventario)



############        ESERCIZIO 6

import string

'''
    alfabeto_minuscolo = string.ascii_lowercase
    alfabeto_maiuscolo = string.ascii_uppercase
    numeri = string.digits
    speciali = string.punctuation
    caratteri = alfabeto_minuscolo + alfabeto_maiuscolo + numeri + speciali
    print(caratteri)
    print("Sceglli i caratteri da usare nella password")
    char: str = input("Caratteri alfabeto minuscoli?  Y/N: ")
    if  char == "n" or char == "N":
        caratteri = caratteri.replace(alfabeto_minuscolo,"")
    char = input("Caratteri alfabeto maiuscoli?  Y/N: ")
    if char == "n" or char == "N":
        caratteri = caratteri.replace(alfabeto_maiuscolo,"")
    char = input("Numeri?  Y/N: ")
    if char == "n" or char == "N":
        caratteri = caratteri.replace(numeri,"")
    char = input("Caratteri speciali?  Y/N: ")
    if char == "n" or char == "N":
        caratteri = caratteri.replace(speciali,"")
    lenght: int = int(input("Inserisci la lunghezza della password: "))
    print(es.password(lenght, caratteri))
'''


############        ESERCIZIO 7


print(es.roman_number(853))



############        ESERCIZIO 8

account: dict = {"Card" : 98104735,
                 "Name" : "Lorenzo",
                 "Surname" : "Colitto",
                 "Balance" : 387.89}
es.atm(account)




############        ESERCIZIO 9

print(es.caesar_cipher("Cartine carenti recanti cernita incerta ", 15, "crypt"))

############        ESERCIZIO 10


print(es.anagram("Incerta", "cretina"))


############        ESERCIZIO 11




############        ESERCIZIO 12

numeri_primi: int = 10
print(es.sieve_eratosthenes(numeri_primi))


############        ESERCIZIO 13



# es.prova()
import turtle

t = turtle.Turtle()
t.speed(0)
t.left(90)
    
es.fractal_tree(t, 50, 10, 100)
turtle.mainloop()
############        ESERCIZIO 14



############        ESERCIZIO 15



