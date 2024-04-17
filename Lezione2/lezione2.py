#Lorenzo Colitto
#17/04/2024

print("Hello World")

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

name: str = "Angelo"
message: str = f"{name} hai capito qualcosa di Python?"
print(message)

#2-4. Name Cases: Use a variable to represent a person’s name. 
#Then print that person’s name in lowercase, uppercase, and title case.

print(name.upper())
print(name.lower())
print(name.title())

#2-5. Famous Quote: Find a quote from a famous person you admire. 
#Print the quote and the name of its author. 
#Your output should look something like the following, 
#including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”

print(f"Rocco Siffredi once said: \"Io di patatine ne ho provate tante!\"")

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person.
#Then compose your message and represent it with a new variable called message. Print your message. 

author: str = "Rocco Siffredi"
quote: str = "Io di patatine ne ho provate tante!"
message = f"{author} once said: \"{quote}\""
print(message)

#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
#Assign the value 'python_notes.txt' to a variable called filename. 
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename: str = "python_notes.txt"
message = filename.removesuffix(".txt")
print(message)

#3-1. Names: Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list, one at a time.

names: list = ["Lorenzo", "Leonardo", "Valerio", "Giuseppe", "Antonio"]
for i in range(len(names)):
    print(names[i])

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.

for i in range(len(names)):
    message: str = f"{names[i]} hai capito qualcosa di Python?"
    print(message)

#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

cars: list = ["Alfa Romeo", "FIAT", "BMW", "Ferrari"]
message = f"I would like to own an {cars[0]}"
print(message)