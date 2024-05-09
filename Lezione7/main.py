from src.Animal import Animal
from src.Food import Food
from src.Menu import Menu

#######ANIMAL
lion = Animal("Lion", 4)

print(lion.get_legs())
#######FOOD
mela = Food("Mela", 1.2, "frutto")
pera = Food("Pera", 1.3, "frutto")
banana = Food("Banana", 1.4, "frutto")
cibo = [mela,pera,banana]
menu = Menu(cibo)

pesca = Food("Pesca", 1.2, "frutto")
ananas = Food("Ananas", 2.2, "frutto")
ciliegia = Food("Ciliegia", 3.2, "frutto")

menu.addFood(pesca)
menu.addFood(ananas)
menu.addFood(ciliegia)

for x in menu.foods:
    print(x.get_name())

menu.printPrices()

print(f"Average price of menu = {menu.avgPrice()}")