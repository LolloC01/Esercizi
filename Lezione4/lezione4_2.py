'''School Grading System:

     Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam 
    (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.'''

def average_score(student: str, vote: list) -> None:
    c: int = 0
    media: float = 0
    for x in vote:
        c += 1
        media += x
    media = media/c
    if media >= 6.0:
        print(f"Studente {student}, media: {media}, PROMOSSO")
    else:
        print(f"Studente {student}, media: {media}, BOCCIATO")
    
    
'''2. Guess the Number Game:

    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is too high, 
    too low, or correct.
    Terminate the loop when the user guesses the number correctly or reaches 
    the maximum number of attempts.'''
import random
def rand(min: int, max: int) -> int:
    x: int = random.randint(min,max)    
    return x

def game(guess: int, attempts: int) -> int:
    if attempts > 0:
        print("Indovina il numero")
        x: int = int(input(f"Tentativo {attempts}:"))
        if x > guess:
            print("Prova con un numero piu piccolo")
        elif x < guess:
            print("Prova con un numero piu grande")
        else:
            print("HAI INDOVINATO")
            return 0
        return game(guess, attempts-1)
    else:
        print("HAI PERSO")
        print("NON HAI INDOVINATO IL NUMERO")
        return 0


'''3. E-commerce Shopping Cart:

    Create a function that defines a product with a name, price, and quantity.
     Create a function that manages the shopping cart, allowing the user 
     to add, remove, and view products in the cart.
    The function should calculate the cart total and apply any discounts or taxes.
     Implement a for loop to iterate over the items in the cart and print detailed 
     information about each product and the total.'''

def product() -> dict:
    nome: str = input("Inserisci il nome del prodotto: ")
    prezzo: float = float(input("Inserisci il prezzo del prodotto: "))
    quantita: int = int(input("Inserisci la quantità del prodotto: "))
    prod: dict = {
        "name" : nome,
        "price" : prezzo,
        "quantity" : quantita
    }
    return prod

def cart(carrello: list, oper: int, discount: float = 0, taxes: float = 22) -> list:
    if oper == 1:
        prod: dict = product()
        carrello.append(prod)
    elif oper == 2:
        for x in carrello:
            print(x["name"])
        eliminate: str = input("Inserisci il nome del prodotto da eliminare: ")
        for x in carrello:
            if eliminate == x["name"]:
                carrello.remove(x)
                print("PRODOTTO ELIMINATO")
                break
    elif oper == 3:
        total: float = 0.00
        for x in carrello:
            total = total + x["price"]*x["quantity"]
        print(f"Totale senza sconto e tasse: {total}")
        sconto: float = total/100*taxes
        total = total + sconto
        if discount != 0:
            total = total-(total/100*discount)
        print(f"TOTALE: {total}")
    else:
        for x in carrello:
            print(f'{x["name"]}\nquantità: {x["quantity"]}\ncosto: {x["quantity"]*x["price"]}')



'''4. Text Analysis:

     Create a function that reads a text file and counts the number of occurrences of each word.
    The function should print a report showing the most frequent words and their number of occurrences.
    You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
    Implement error handling to handle missing files or other input issues.'''


import os

def analysis(file: str) -> None:
    text: list = [] 
    word: dict = {}
    if os.path.exists(file):
        f = open(file, "r")
    else: 
        print("Il fiile non esiste")
        return 0
    for x in f:
        x = x.lower().strip(",")
        x = x.split()
        text.append(x)
    f.close()
    for x in text:
        for y in x:
            if y in word:
                word[y] += 1
            else:
                word[y] = 1 
    max_n: int = 0
    max_w: str
    for x in word:
        if word[x] > max_n:
            max_n = word[x]
            max_w = x
    print(f"Most used word:{max_w} --- repeated {max_n} times")



'''5. Inventory Management System:

     Create a function that defines an item with a code, name, quantity, and price.
     Create a database or dictionary to store the items in inventory.
    Implement functions to add, remove, search, and update items in the inventory.
    Use for loops and conditional statements to manage the various inventory operations.
'''
def item(code: str, name: str, quantity: int, price: float) -> dict:
    item: dict ={"code" : code,
                 "name" : name,
                 "quantity" : quantity,
                 "price" : price}
    return item

def add_item(item: dict, inventory: list):
    if len(inventory) > 0:
        for x in range(len(inventory)):
            if inventory[x]["code"] == item["code"]:
                print("item gia in inventario")
                inventory[x]["quantity"] += item["quantity"]
            else:
                print("APPEND")
                inventory.append(item)   
    else:
        inventory.append(item)
    print(inventory)

def show_inventory(inventory: list):
    for x in inventory:
        print(x)

def remove_item(item: str, inventory: list):
    for x in inventory:
        if x["code"] == item or x["name"] == item:
            inventory.remove(x)
            print("ELEMENTO RIMOSSO")
    
def update_items(item: dict, inventory: list):
    for x in range(len(inventory)):
        if inventory[x]["code"] == item["code"] or inventory[x]["name"] == item["name"]:
            inventory[x]["price"] = item["price"]
            inventory[x]["quantity"] += item["quantity"]
            print("ELEMENTO RIMOSSO")
    return

def search_item(item: str, inventory: list):
    for x in inventory:
        if x["code"] == item or x["name"] == item:
            print(x)


'''6. Password Generator:

    Create a function that generates a random password with a specified length and desired character types 
    (lowercase letters, uppercase letters, numbers, symbols).
    Allow the user to specify the password length and desired character types.
    Generate and return a random password that meets the user's criteria.'''

def password(lenght: int, char: list) -> str:
    password: str = ""
    while lenght > 0:
        lenght -= 1
        password += random.choice(char)
    return password



'''7. Roman Numeral Conversion:

    Create a function that converts a given integer to its Roman numeral representation.
    Handle numbers from 1 to 3999.
    Use a combination of string manipulation and conditional statements to build the Roman numeral.'''

    
def roman_number(arab_num: int) -> str:
    roman_num: str = ""
    roman_alph: list = ["M", "D", "C", "L", "X", "V", "I"] 
    letter: str = ""
    num_l: list = forma_polin(arab_num)
    for x in range(len(num_l)):
        if x == 0:
             # print(f"migliaia -- {num_l[x]}")
            if num_l[x] == 1 or num_l[x] == 2 or num_l[x] == 3:
                roman_num += ("M"*num_l[x])
        elif x == 1:
              # print(f"centinaia -- {num_l[x]}")
            if num_l[x] == 1 or num_l[x] == 2 or num_l[x] == 3:
                roman_num += ("C"*num_l[x])
            elif num_l[x] == 4:
                roman_num += ("CD")
            elif num_l[x] == 5:
                roman_num += ("D")
            elif num_l[x] == 6:
                roman_num += ("DC")
            elif num_l[x] == 7:
                roman_num += ("DCC")
            elif num_l[x] == 8:
                roman_num += ("DCCC")
            elif num_l[x] == 9: 
                roman_num += ("CM")
        elif x == 2:
              # print(f"decine -- {num_l[x]}")
            if num_l[x] == 1 or num_l[x] == 2 or num_l[x] == 3:
                roman_num += ("X"*num_l[x])
            elif num_l[x] == 4:
                roman_num += ("XL")
            elif num_l[x] == 5:
                roman_num += ("L")
            elif num_l[x] == 6:
                roman_num += ("LX")
            elif num_l[x] == 7:
                roman_num += ("LXX")
            elif num_l[x] == 8:
                roman_num += ("LXXX")
            elif num_l[x] == 9: 
                roman_num += ("XC")
        elif x == 3:
             # print(f"unita -- {num_l[x]}")
            if num_l[x] == 1 or num_l[x] == 2 or num_l[x] == 3:
                roman_num += ("I"*num_l[x])
            elif num_l[x] == 4:
                roman_num += ("IV")
            elif num_l[x] == 5:
                roman_num += ("V")
            elif num_l[x] == 6:
                roman_num += ("VI")
            elif num_l[x] == 7:
                roman_num += ("VII")
            elif num_l[x] == 8:
                roman_num += ("VIII")
            elif num_l[x] == 9: 
                roman_num += ("IX")

        
 #     print(num_l)
    
    return roman_num

def forma_polin(arab_num: int) -> list:
    num_s: str = str(arab_num)
    num_l: list = [] 
    for i in range(len(num_s)):
        num_l.append(int(num_s[i] ))
    while len(num_l) < 4:
        num_l.insert(0,0)
    return num_l


'''8. ATM Machine Simulator:

    Create a function that simulates an ATM machine.
    Initialize an account with a starting balance.
    Allow the user to perform transactions such as deposit, withdraw, and check balance.
     Validate transactions against the account balance and available funds.
    Provide appropriate feedback to the user for each transaction.'''

def atm(account: dict):
    while True:    
        print("Select operation: \
          \n(1 to deposit)\
          \n(2 to withdraw)\
          \n(3 to check Balance)\
          \n(0 to terminate)")
        operation: int = int(input("Inserisci l'operazione da eseguire: "))
        if operation == 1:
            deposit: float = int(input("Inserisci la cifra da depositare: "))
            account["Balance"] += deposit
            x = account["Balance"]
            print(f"New Balance: {x}")
        elif operation == 2: 
            print(account["Balance"])
            withdraw: int = int(input("inserici la cifra da prelevare: "))
            if withdraw > account["Balance"]:
                print("CIFRA NON DISPONIBILE")
            else:
                print(f"Prelevati: {withdraw}")
                account["Balance"] -= withdraw
                x = account["Balance"]
                print(f"New Balance: {x}")     
        elif operation == 3:
            print(account)
        else:
            return


'''9. Caesar Cipher Encryption/Decryption

    Create functions for encrypting and decrypting a message using the Caesar cipher.
    Allow the user to specify the shift value (number of positions to shift each letter).
     Handle both encryption and decryption using the same function with appropriate adjustments.
    Encrypt and decrypt the given message using the specified shift value.'''
import string

def caesar_cipher(message: str, shift: int, oper: str) -> str:
    alfabeto_minuscolo = string.ascii_lowercase
    alfabeto_maiuscolo = string.ascii_uppercase
    numeri = string.digits
    speciali = string.punctuation
    alphabet: str =  alfabeto_maiuscolo + alfabeto_minuscolo + numeri + speciali
    crypted: dict = {}
    final_message: str = ""
    index: int = 0 
    for x in range(len(alphabet)):
        if (x+shift) < len(alphabet):
            crypted[alphabet[x]] = alphabet[x+shift] 
        else:
            crypted[alphabet[x]] =  alphabet[index]
            index += 1
    for s in message:
        if s == " ":
            final_message = final_message + " "
            continue
        for x, y in crypted.items():
            if oper == "crypt":
                if s == x:
                    final_message = final_message + y
            else:
                if s == y:
                    final_message = final_message + x
    return final_message
    


'''10. Anagram Checker:

    Create a function that checks whether two given strings are anagrams of each other.
    Convert both strings to lowercase and remove any non-alphabetic characters.
    Sort the characters of each string and compare the sorted strings for equality.
    Indicate whether the strings are anagrams or not.'''
import string

def anagram(string_1: str, string_2: str) -> bool:
    remove: str = string.punctuation + string.digits
    storage: list = [] 
    for x in range(len(string_2)):
        print(string_2[x] )
        s: str = string_2[x].lower()
        if s not in remove:
            storage.append(s)
    print(storage)
    for x in string_1.lower().lstrip(remove):
        print(f"{x}   -----    {storage} ")
        if x in storage:
            storage.remove(x)
        
    if len(storage) > 0:
        return False
    return True



'''11. Word Search Puzzle Solver:  --------       DIFFICILE

    Create a function that solves a word search puzzle.
    Provide a 2D grid representing the puzzle and a list of words to find.
    Implement a backtracking algorithm to search for the words in the grid, marking visited cells to avoid repetition.
    Output the locations of the found words within the grid.'''


'''12. Sieve of Eratosthenes Prime Number Generator:

    Create a function that generates a list of prime numbers up to a specified limit using the Sieve of Eratosthenes algorithm.
    Initialize an array of all numbers up to the limit, marking each number as prime initially.
    Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime.
    The remaining unmarked numbers are the prime numbers within the limit.
    Return the list of prime numbers.'''



def sieve_eratosthenes(num: int) -> list:
    primi: list =[x for x in range(num)]
    non_primi: list = []  
    molt: int = 2
    for x in range(2, len(primi)):
        print(x)
        molt = 2
        if x not in non_primi:
            n: int = molt*primi[x] 
            print(f"{n}  ----  {x} ")
            while n < primi[-1]:
                n: int = molt*primi[x] 
                if n not in non_primi:
                    non_primi.append(n)
                molt += 1
    for x in non_primi:
        if x <= primi[-1]: 
            primi.remove(x)     
    return primi


'''13. Fractal Tree Generator:

    Create a function that generates a fractal tree using recursion.
    Specify the starting trunk length and branching angle.
    Draw the trunk and then recursively call the function to draw two branches at the specified angle, each with a shorter length.
    Repeat the branching process until a desired level of detail is reached.'''
import turtle


def fractal_tree(t: turtle, lenght: int, angle: int, line: int) -> None:
    if lenght <= 3:
        return
    t.forward(line)
    t.right(angle)
    fractal_tree(t, lenght-5, angle, line-5)
    t.left(angle*2)
    fractal_tree(t, lenght-5, angle, line-5)
    t.right(angle)
    t.backward(line)

'''14. Sudoku Solver:

    Create a function that solves a Sudoku puzzle using backtracking.
    Provide a 9x9 grid representing the puzzle with some numbers filled in and others left blank.
    Implement a backtracking algorithm to check for valid placements in empty cells,
    ensuring no row, column, or 3x3 subgrid contains duplicates.
    Solve the puzzle by filling in the remaining empty cells with valid numbers.

15. Text Editor with Basic Functionality:

    Create a simple text editor that allows the user to open, edit, and save text files.
    Implement basic functionality such as inserting, deleting, and copying text.
    Provide undo/redo functionality to allow users to reverse actions.
    Save the edited text to a file when the user chooses to save.'''
