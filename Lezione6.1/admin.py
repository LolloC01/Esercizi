from user import User
#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
#In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

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