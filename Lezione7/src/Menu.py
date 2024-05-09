from src.Food import Food

class Menu:
    foods: list[Food] = []
    def __init__(self, foods: list[Food] = []) -> None:
        self.foods = foods

    def addFood(self, f: Food) -> None:
        self.foods.append(f)

    def removeFood(self, f: Food) -> None:
        if f in self.foods:
            self.foods.remove(f)
        else:
            raise Exception("NON PUOI ELMINARE UN CIBO NON PRESENTE NELLA LISTA")
    
    def printPrices(self) -> None:
        for x in self.foods:
            print(f"{x.get_name()} = {x.get_price()}")
            
    def avgPrice(self) -> float:
        avg = 0
        for x in self.foods:
            avg += x.get_price()
        avg /= len(self.foods)
        return avg
