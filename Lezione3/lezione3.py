#Lorenzo Colitto
#19/04/2024
es = 1
while es != 0:
    print("Che esercizio vuoi eseguire?")
    print("4.1 - 4.2 - 4.3 - 4.4 - 4.5 - 4.6 - 4.7 - 4.8 - 4.9 - 4.101 - 4.11 - 4.12 - 4.14 - 4.15")
    print("5.1 - 5.2 - 5.3 - 5.4 - 5.5 - 5.6 - 5.7 - 5.8 - 5.9 - 5.101 - 5.11")
    print("Inserisci 0 per uscire")
    es: float = float(input("inserisci l'esercizio: \n"))

#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
#For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
#The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

    if es==4.1:
        pizza: list = ["Margherita", "Capricciosa", "Funghi e salsiccia"]
        for p in pizza:
            message: str = f"I like {p}"
            print(message)
        print(f"I always choose {pizza[1]}\n I can eat {pizza[0]} all day long \n My dad makes a great {pizza[2]} \n I really love pizzas!")


#4-2. Animals: Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. 
#You could print a sentence, such as Any of these animals would make a great pet!
    elif es == 4.2:
        animal: list = ["lion", "pantehr", "tiger"]
        for a in animal:
            message: str = f"A {a} would easely eat a person"
            print(message)
        print("Each of this animals can eat a person without much efforts")

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

    elif es == 4.3:
        for i in range (1,21):
            print(i)

#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
#(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

    elif es == 4.4:
        n: list = []
        for i in range(1, 1000001):
            n.append(i)
        for i in n:
            print(i)

#4-5. Summing a Million: Make a list of the numbers from one to one million, 
#and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.

    elif es == 4.5:
        n: list = []
        for i in range(1, 1000001):
            n.append(i)
        message: str = f"Il minimo è : {min(n)}"
        print(message)
        message: str = f"Il massimo è : {max(n)}"
        print(message)
        message: str = f"La somma è : {sum(n)}"
        print(message)

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

    elif es == 4.6:
        odd_num: list = []
        for i in range(1,20,2):
            odd_num.append(i)
        for i in odd_num:
            print(i)

#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

    elif es == 4.7:
        multiple: list = []
        for i in range(3,31,3):
            multiple.append(i)
        for i in multiple:
            print(i)

#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

    elif es == 4.8:
        cube: list = []
        for i in range(1,11):
            x: int = i**3
            cube.append(x)
        for i in cube:
            print(i)


#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

    elif es == 4.9:
         cube = [x**3 for x in range(1,11)]
         for i in cube:
             print(i)

#
#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
#• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

    elif es == 4.101:
        cube: list = [1,2,3,4,5,6,7,8,9,10]
        message: str = f"First three items: {cube[:3]}"
        print(message)
        x: int = int(len(cube)/2)
        message: str = f"middle three items: {cube[x-1:x+2]}"
        print(message)
        message: str = f"Last three items: {cube[-3:]}"
        print(message)


#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
#Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
#Make sure each new pizza is stored in the appropriate list.

    elif es == 4.11:
        pizza: list = ["Margherita", "Capricciosa", "Funghi e salsiccia"]
        pizza.append("Bufala e pachino")
        friend_pizza: list = [x for x in pizza]
        friend_pizza.append("patate e salsiccia")
        print("My favourite pizzas are:")
        for i in pizza:
            print(i)
        print("My friend favourite pizzas are:")
        for i in friend_pizza:
            print(i)


###########################
#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test. Your code
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#• Look closely at your results, and make sure you understand why each line
#evaluates to True or False.
#• Create at least 10 tests. Have at least 5 tests evaluate to True and another
#5 tests evaluate to False.
    elif es == 5.1:
        car = 'subaru'
        print("Is car == 'subaru'? I predict True.")
        print(car == 'subaru')
        print("\nIs car == 'audi'? I predict False.")
        print(car == 'audi')
        car = 'ferrari'
        print("Is car == 'ferrari'? I predict True.")
        print(car == 'ferrari')
        print("\nIs car == 'mercedes'? I predict False.")
        print(car == 'mercedes')
        car = 'alfa romeo'
        print("Is car == 'alfa romeo'? I predict True.")
        print(car == 'alfa romeo')
        print("\nIs car == 'bmw'? I predict False.")
        print(car == 'bmw')
        car = 'FIAT'
        print("Is car == 'FIAT'? I predict True.")
        print(car == 'FIAT')
        print("\nIs car == 'audi'? I predict False.")
        print(car == 'audi')
        car = 'lamborghini'
        print("Is car == 'lamborghini'? I predict True.")
        print(car == 'lamborghini')
        print("\nIs car == 'bugatti'? I predict False.")
        print(car == 'bugatti')

#5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. 
#If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
#Have at least one True and one False result for each of the following:
#• Tests for equality and inequality with strings
#• Tests using the lower() method
#• Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
#• Tests using the and keyword and the or keyword
#• Test whether an item is in a list
#• Test whether an item is not in a list
    elif es == 5.2:
        car: str = "FERRARI"
        cars: list = ["audi", "bmw", "ferrari"]
        print("is your car a audi?")
        print(car == cars[1])
        print("is your car a ferrari?")
        print(car.lower() == cars[1])
        n1: int = 123
        n2: int = 54
        print(f"{n1} è maggiore? di {n2}")
        print(n1 > n2)
        print(f"{n1} è minore? di {n2}")
        print(n1 < n2)
        print(f"{n1} è maggiore o uguale? di {n2}")
        print(n1 >= n2)
        print(f"{n1} è minore o uguale? di {n2}")
        print(n1 <= n2)
        print(f"{n1} è uguale a {n2}")
        print(n1 == n2)
        print("l'audi è nella lista?")
        print("audi" in cars)
        print("l'alfa romeo è nella lista?")
        print("alfa romeo" in cars)
        print("l'audi è fuori dalla lista?")
        print("audi" not in cars)
        print("l'alfa romeo è fuori dalla lista?")
        print("alfa romeo" not in cars)
        
#5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
#

    elif es == 5.3:
        color: str = input("inerisci un colore tra green, rede yellow: ")
        if color == "green":
            print("you just earn 5 points")
        elif color == "red":
            pass
        elif color == "yellow":
            pass

#
#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#• Write one version of this program that runs the if block and another that runs the else block.
    elif es == 5.4:
        color: str = input("inerisci un colore tra green, rede yellow: ")
        if color == "green":
            print("you just earn 5 points")
        else:
            print("You just earned 10 points")
#
#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#
#• If the alien is green, print a message that the player earned 5 points.
#• If the alien is yellow, print a message that the player earned 10 points.
#• If the alien is red, print a message that the player earned 15 points.
#• Write three versions of this program, making sure each message is printed for the appropriate color alien.
    elif es == 5.5:
        color: str = input("inerisci un colore tra green, rede yellow: ")
        if color == "green":
            print("you just earn 5 points")
        elif color == "red":
            print("you just earn 10 points")
        elif color == "yellow":
            print("you just earn 15 points")
#
#
#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
#• If the person is less than 2 years old, print a message that the person is a baby.
#• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#• If the person is age 65 or older, print a message that the person is an elder.

    elif es == 5.6:
        age: int = int(input("Insert the age you want to check: "))
        if age < 2:
            print("the person is a baby")
        elif age < 4:
            print("the person is a toddler")
        elif age < 13:
            print("the person is a kid")
        elif age < 20:
            print("the person is a teenager")
        elif age < 65:
            print("the person is an adult")
        else:
            print("the person is an elder")

#
#5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
#• Make a list of your three favorite fruits and call it favorite_fruits.
#• Write five if statements. Each should check whether a certain kind of fruit is in your list. 
#If the fruit is in your list, the if block should print a statement, such as You really like Apples!
#

    elif es == 5.7:
        fav_fruit: list = ["mela", "pera", "banana", "pesca", "albicocca", "mango", "kiwi"]
        if "mela" in fav_fruit:
            print("La mela c'è")
        if "kiwi" in fav_fruit:
            print("il kiwi mi piace")
        if "cocco" in fav_fruit:
            print("viva il cocco")
        if "mango" in fav_fruit:
            print("Mi piace il mango")
        if "fragola" not in fav_fruit:
            print("non mi piace la fragola")

#5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user 
#after they log in to a website. Loop through the list, and print a greeting to each user.
#• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
#• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
#

    elif es == 5.8:
        username: list = ["admin", "user1", "user2", "user3", "user4"]
        for i in username:
            if i == "admin":
                message: str = f"Hello {i}, would you like to see a status report?"
                print(message)
            else:
                message: str = f"Hello {i}"
                print(message)
#
#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
#• If the list is empty, print the message We need to find some users!
#• Remove all of the usernames from your list, and make sure the correct message is printed.
#

    elif es == 5.9:
        username: list = []
        x: int = int(input("Inserisci il numero di username: "))
        for i in x:
            y: str = input("Inserisci gli username: ")
            username.append(y)  
        if len(username) == 0:
            print("We need to find some users!")
        else:
            for i in username:
                if i == "admin":
                    message: str = f"Hello {i}, would you like to see a status report?"
                    print(message)
                else:
                    message: str = f"Hello {i}"
                    print(message)

#5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#• Make a list of five or more usernames called current_users.
#• Make another list of five usernames called new_users. 
#      Make sure one or two of the new usernames are also in the current_users list.
#• Loop through the new_users list to see if each new username has already been used. 
#      If it has, print a message that the person will need to enter a new username. 
#      If a username has not been used, print a message saying that the username is available.
#• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
#      (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
#

    elif es == 5.101:
        current_users: list = ["user", "admin", "guest", "John", "Jim"]
        new_users: list = ["Jake", "Luca", "lorenzo", "UsEr", "Kim"]
        current_lower: list = []
        for x in current_users:
            current_lower.append(x.lower())
        for i in range(len(new_users)):
            print(new_users[i])
            used: bool = True
            while used:
                if new_users[i].lower() in current_lower:
                    print("USERNAME GIA USATO, INSERIRNE UN ALTRO")
                    new_users[i] = input("Inserisci un nuovo username: ")
                    used = True
                else:
                    print("USERNAME DISPONIBILE")
                    used = False
        


#
#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#• Store the numbers 1 through 9 in a list.
#• Loop through the list.
#• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
#   Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
#

