from abc import ABC

class Forma(ABC):
    def __init__(self, nome) -> None:
        self.nome = nome

    def getArea(self):
        pass
    
    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato) -> None:
        super().__init__("Quadrato")
        self.lato = lato

    def getArea(self):
        return self.lato*self.lato
    
    def render(self):
        for x in range(self.lato):
            if x == 0 or x == self.lato-1:
                print("*"*self.lato)
            else:
                print("*"+" "*(self.lato-2)+"*")

class Rettangolo(Forma):
    def __init__(self, base, altezza) -> None:
        super().__init__("Rettangolo")
        self.base = base
        self.altezza = altezza

    def getArea(self):
        return self.base*self.altezza
    
    def render(self):
        for x in range(self.altezza):
            if x == 0 or x == self.altezza-1:
                print("* "*self.base)
            else:
                print("*"+" "*(self.base-2)+"*")

class Triangolo(Forma):
    def __init__(self, base, altezza) -> None:
        super().__init__("Triangolo")
        self.base = base
        self.altezza = altezza

    def getArea(self):
        return self.base*self.altezza/2
    
    def render(self):
        for x in range(self.altezza):
            ll = ""
            for y in range(self.base):
                if y == x or y == 0:
                    ll+="*"
                elif x == self.altezza-1:
                    ll="* "*(self.base)
                    break
                else:
                    ll+=" "
            print(ll)



x = Triangolo(12,8)
x.render()