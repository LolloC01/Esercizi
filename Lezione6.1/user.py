
##9-3. Users: Make a class called User. 
#Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 
#Make a method called describe_user() that prints a summary of the user’s information. 
#Make another method called greet_user() that prints a personalized greeting to the user. 
#Create several instances representing different users, and call both methods for each user.

class User:

    def __init__(self, name: str, surname: str, age: int, gender: int, phone: int ) -> None:
        self.firs_name: str = name
        self.last_name: str = surname
        self.age: int = age
        self.gender: int = gender
        self.telephone: int = phone 
        self.login_attempts: int = 0


    def describe_user(self) -> None:
        print(f"Name:\t{self.firs_name}\nSurname:\t{self.last_name}\nage:\t{self.age}\ntelephone:\t{self.telephone}\nLogin attempts:\t{self.login_attempts}")

    def greet_user(self) -> None:
        print(f"Goodmorning {self.firs_name} {self.last_name}")

    def increment_login_attempts(self) -> None:
        self.login_attempts += 1

    def reset_login_attempts(self) -> None:
        self.login_attempts = 0

#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
#Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
#Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
#Make an instance of the User class and call increment_login_attempts() several times. 
#Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
#Print login_attempts again to make sure it was reset to 0.

#9-7. Admin: An administrator is a special kind of user. 
#Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. 
#Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 
#Write a method called show_privileges() that lists the administrator’s set of privileges. 
#Create an instance of Admin, and call your method. 

class Admin (User):

    def __init__(self, name: str, surname: str, age: int, gender: int, phone: int, privs) -> None:
        super().__init__(name, surname, age, gender, phone)
        self.priv = Privileges(privs)

    

#9-8. Privileges: Write a separate Privileges class. 
#The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
#Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
#Create a new instance of Admin and use your method to show its privileges.

class Privileges:

    def __init__(self, privileges: list = []) -> None:
        self.privileges: list = privileges

    def show_privileges(self) -> None:
        print("PRIVILEGES: ")
        for x in self.privileges:
            print(x, end = "\t")



#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
#9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
#9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
#9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
#9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.