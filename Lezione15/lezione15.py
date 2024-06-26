'''Crea un context manager usando una classe

Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')'''
from contextlib import contextmanager

@contextmanager
def FileManager(path):
    f = open(path, "w")
    yield f
    f.close()

with FileManager("Lezione15/prova.txt") as f:
    for x in range(100):
        y = f"{x}\n"
        f.write(y)

'''Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with

with Timer():

    time.sleep(1)

time elapsed: 1.00000

in questo esempio il tempo passato non sarà mai uguale a 1'''
import time
@contextmanager
def Timer():
    t1 = time.time()
    yield
    t2 = time.time()
    print(f"{(t2-t1):.3f}")

with Timer():
    time.sleep(5)