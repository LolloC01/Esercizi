
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


#9-11. Imported Admin: Start with your work from Exercise 9-8. 
#Store the classes User, Privileges, and Admin in one module. 
#Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
