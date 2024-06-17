'''Personalized math library: Create a Python library that provides functions for handling fractions, with built-in error handling. 
The library must include functions for the following operations:

    Create a fraction from the numerator and denominator.
    Collect the numerator and denominator of a fraction.
    Simplify a fraction.
    Add, subtract, multiply and divide fractions.
    Check whether one fraction is equivalent to another. 

    All library functions must use the try-except block to handle potential errors, such as null denominators, unsupported operations, or division by zero. 
    The library must raise custom exceptions to indicate specific errors to the user.

'''
from math import gcd

class QError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Fraction:
    def __init__(self, num, denom) -> None:
        self.numerator: int = num
        self.denominator: int = denom

    def simplify(self):
        pass

    def add(self, other: "Fraction") -> "Fraction":
        mcm = self.mcm(other)
        num1 = self.numerator*(mcm/self.denominator)
        num2 = other.numerator*(mcm/other.denominator) 
        num = num1 + num2
        return Fraction(num, mcm)

    def subtract(self):
        pass

    def multiply(self):
        pass

    def divide(self):
        pass

    def __eq__(self, other: "Fraction") -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def mcm(self, other: "Fraction"):
        mcd = gcd(self.denominator, other.denominator)
        return self.denominator*other.denominator/mcd