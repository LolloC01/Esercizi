'''Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). 
Handle ValueError if the input is negative by returning an informative message.'''
from math import sqrt
def safe_sqrt(number: int):
    if number < 0:
        raise ValueError("Negative input not allowed")
    else: 
        return sqrt(number)

'''Password Validation: Write a function validate_password(password) that checks if a password meets certain criteria 
(i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters).  
Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.'''
import string

class ShortPassword(Exception):
    "Short password"
    def __init__(self, message): 
        super().__init__(message) 

class NoUppercasePassword(Exception):
    "Not enought uppercase letter in password"
    def __init__(self, message): 
        super().__init__(message) 
    def error() -> str:
        return "Not enought uppercase letter in password"

class NoSpecialCharPassword(Exception):
    "Not enought Special Char in password"
    def __init__(self, message): 
        super().__init__(message) 

    

def validate_password(password: str):
    upper = string.ascii_uppercase
    special = string.punctuation
    try:
        if len(password) < 20:
            raise ShortPassword("Password Troppo Corta")
        x = 0
        for char in password:
            if char in upper:
                x += 1
        if x < 3:
            raise NoUppercasePassword("Non presenti 3 caratteri maiuscoli")
        x = 0
        for char in password:
            if char in special:
                x += 1
        if x < 4:
            raise NoSpecialCharPassword("Non presenti 4 caratteri speciali")
    except ShortPassword:
        return "Password Troppo Corta"
    except NoUppercasePassword:
        return NoUppercasePassword.error()
    except NoSpecialCharPassword as e:
        return e
    else:
        return "PASSWORD VALIDA"

print(validate_password("1234abcAssdsdsdmmmm,,mmm"))

'''Context Managers for File Handling: Use the with statement and context managers to open and close a file. 
Handle potential IOError within the with block for clean resource management.'''

try:
    # Tentativo di apertura di un file inesistente
    with open('file_inesistente.txt', 'r') as file:
        contenuto = file.read()
except FileNotFoundError as e:
    print(f"File non trovato: {e}")
except PermissionError as e:
    print(f"Permesso negato: {e}")
except IOError as e:
    print(f"Errore di I/O: {e}")


'''Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa 
implementing methods to add a new date, delete a given date, modify a date, and perform a query on a given date is required.  
A query on a given date allows for retrieving a given new date. 
Note that a date is an object for your database; it must be instantiated from a string.'''

import datetime

class dates:
    def __init__(self) -> None:
        self.date = []
    
    def add_date(self, year: int, month: int, day: int) -> None:
        x = datetime.datetime(year,month,day)
        self.date.append(x)
    
    def delete_date(self,year,month,day):
        x = datetime.datetime(year,month,day)
        if x in self.date:
            self.date.remove(x)
    
    def modify_date(self,year,month,day,new_year,new_month,new_day):
        x = datetime.datetime(year,month,day)
        y = datetime.datetime(new_year,new_month,new_day)
        if x in self.date:
            r = self.date.index(x)
            self.date.remove(x)
            self.date.insert(r,y)

    def get_date(self):
        return self.date


'''An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases 
using UnitTest trying to (possibly) cover all execution paths! User input is assumed to be a formula that consists of 
a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). 
Split user input using str.split(), and check whether the resulting list is valid:

     If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
        Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). 
    Catch any ValueError that occurs, and instead raise a FormulaError.
        If the second input is not '+' or '-', again raise a FormulaError.
    If the input is valid, perform the calculation and print out the result. 
        The user is then prompted to provide new input, and so on, until the user enters quit.'''

class Calculator:
    def __init__(self) -> None:
        pass 

    @staticmethod
    def operation(operation: str) -> float:
        op = operation.split(sep = " ")
        if op[1] == "+":
            return int(op[0])+int(op[2])
        elif op[1] == "-":
            return int(op[0])-int(op[2])
        elif op[1] == "*":
            return int(op[0])*int(op[2])
        elif op[1] == "/":
            if int(op[2]) == 0:
                raise ZeroDivisionError
            return int(op[0])/int(op[2])


print(Calculator.operation("10 / 0"))