'''Crea un context manager usando una classe

Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')'''
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"an error occurred: {exc_value}")
        return True
    

path = "Lezione15/provaclassi.txt"
with FileManager(path, "w") as f:
    for x in range(100):
        s = f"{x} ciao \n"
        f.write(s)

'''Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with

with Timer():

    time.sleep(1)

time elapsed: 1.00000

in questo esempio il tempo passato non sarà mai uguale a 1'''
import time

class Timer:

    def __init__(self) -> None:
        self.t1 = 0
        self.t2 = 0

    def __enter__(self):
        self.t1 = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        self.t2 = time.time()
        print(f"{(self.t2-self.t1):.3f}")
        
with Timer():
    time.sleep(10)