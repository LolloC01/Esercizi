#9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. 
#Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
#Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Dice:

    def __init__(self, n_side) -> None:
        self.sides = n_side
    
    def roll_dice(self) -> int:
        return randint(1,self.sides)
    
#9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
#Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.

class Lottery:

    def __init__(self) -> None:
        self.tickets = ["a","b","c","d","e",1,2,3,4,5,6,7,8,9,0]
    
    def winners(self) -> None:
        x = 4
        win = []
        while x > 0:
            n = randint(0, len(self.tickets)-1)
            win.append(self.tickets[n])
            x -= 1
        print("any ticket matching these 4 numbers or letters wins a prize.")
        for y in win:
            print(y, end="\t")
        print("")

#9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
#Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. 
#Print a message reporting how many times the loop had to run to give you a winning ticket.