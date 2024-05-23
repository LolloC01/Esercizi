#9-1. Restaurant: Make a class called Restaurant. 
#The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() 
#that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. 
#Print the two attributes individually, and then call both methods.

class Restaurant:
    
    def __init__(self, nome: str, tipo: str) -> None:
        self.restaurant_name: str = nome
        self.cuisine_type: str = tipo
        self.number_served: int = 0

    # Getter for restaurant_name
    def restaurant_name(self) -> str:
        return self._restaurant_name

    # Setter for restaurant_name
    def restaurant_name(self, nome: str) -> None:
        self._restaurant_name = nome

    # Getter for cuisine_type
    def cuisine_type(self) -> str:
        return self._cuisine_type

    # Setter for cuisine_type
    def cuisine_type(self, tipo: str) -> None:
        self._cuisine_type = tipo

    def set_number_served(self, n: int) -> None:
        self.number_served = n

    def increment_number_served(self, n: int) -> None:
        self.number_served += n

    def describe_restaurant(self) -> None:
        print(f"Restaurant name:\t{self.restaurant_name}\nCusine type:\t{self.cuisine_type}\nClient served:\t{self.number_served}")

    def open_restaurant(self) -> None:
        print("RESTAURANT OPENED")

#9-4. Number Served: Start with your program from Exercise 9-1. 
#Add an attribute called number_served with a default value of 0. 
#Create an instance called restaurant from this class. 
#Print the number of customers the restaurant has served, and then change this value and print it again. 
#Add a method called set_number_served() that lets you set the number of customers that have been served. 
#Call this method with a new number and print the value again. 
#Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
#Call this method with any number you like that could represent how many customers were served in, say, a day of business. 


#9-2. Three Restaurants: Start with your class from Exercise 9-1.  
#Create three different instances from the class, and call describe_restaurant() for each instance.

                                        #VEDI lezione6.1


#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
#Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. 
#Either version of the class will work; just pick the one you like better. 
#Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. 
#Create an instance of IceCreamStand, and call this method. 


class IceCreamStand (Restaurant):
    def __init__(self, name: str, tipo: str, flavours: list = []) -> None:
        super().__init__(name, tipo)
        self.flavours: list = flavours

    def describe_restaurant(self) -> None:
        print("Avalaible flavours:")
        for x in self.flavours:
            print(x, end = "\t")
        print("")
        return super().describe_restaurant()
    

#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. 
#Make a separate file that imports Restaurant. 
#Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
