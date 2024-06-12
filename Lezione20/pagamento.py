class Pagamento:
    def __init__(self) -> None:
        self.importo: float = None

    def get(self):
        return self.importo
    
    def set(self, value: float) -> None:
        self.importo = value

    def dettagliPagamento(self) -> str:
        return f"Importo del pagamento: €{self.importo}"
    
class PagamentoContanti(Pagamento):
    def __init__(self, value) -> None:
        self.set(value)

    def dettagliPagamento(self) -> str:
        return f"Pagamento in contanti di: €{self.get()}" 
    
    def inPezziDa(self):
        valuta = {
            "500 euro": 0,
            "200 euro": 0,
            "100 euro": 0,
            "50 euro": 0,
            "20 euro": 0,
            "10 euro": 0,
            "5 euro": 0,
            "2 euro": 0,
            "1 euro": 0,
            "0,50 euro": 0,
            "0,20 euro": 0,
            "0,10 euro": 0,
            "0,05 euro": 0
        }
        x = self.get()
        while x > 0:
            x = round(x,2)
            if x>=500:
                x-=500
                valuta["500 euro"]+=1
            elif x>=200:
                x-=200
                valuta["200 euro"]+=1
            elif x>=100:
                x-=100
                valuta["100 euro"]+=1
            elif x>=50:
                x-=50
                valuta["50 euro"]+=1
            elif x>=20:
                x-=20
                valuta["20 euro"]+=1
            elif x>=10:
                x-=10
                valuta["10 euro"]+=1
            elif x>=5:
                x-=5
                valuta["5 euro"]+=1
            elif x>=2:
                x-=2
                valuta["2 euro"]+=1
            elif x>=1:
                x-=1
                valuta["1 euro"]+=1
            elif x>=0.5:
                x-=0.5
                valuta["0,50 euro"]+=1
            elif x>=0.2:
                x-=0.2
                valuta["0,20 euro"]+=1
            elif x>=0.1:
                x-=0.1
                valuta["0,10 euro"]+=1
            elif x>=0.05:
                x-=0.05
                valuta["0,05 euro"]+=1
        for i in valuta:
            if valuta[i] != 0:
                print(f"{valuta[i]} banconota da {i}")

class PagamentoCarta(Pagamento):
    def __init__(self, value, nome, cognome, data_scad, nome_carta) -> None:
        self.set(value)
        self.nome = nome
        self.cognome = cognome
        self.data = data_scad
        self.num_carta = nome_carta

    def __str__(self):
        return f"Nome sulla carta: {self.nome} {self.cognome}\nData di scadenza: {self.data}\nNumero della carta: {self.num_carta}"
    
    def dettagliPagamento(self) -> str:
        return f"Pagamento con carta di: €{self.get()}\n{self}"
    


x= PagamentoContanti(150.00)
x1 = PagamentoContanti (95.25)
y = PagamentoCarta(200,"Mario", "Rossi","12/24",1234567890123456)
y1 = PagamentoCarta(500,"Luigi", "Bianchi","01/25",10987565432112345)

print(x.dettagliPagamento())
x.inPezziDa()
print(x1.dettagliPagamento())
x1.inPezziDa()
print(y.dettagliPagamento())
print(y1.dettagliPagamento())