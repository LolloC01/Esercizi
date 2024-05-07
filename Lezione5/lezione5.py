'''1. Create a Playlist:

Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
The function should return a dictionary with the playlist name and a set of songs. Call the function with different numbers of songs to demonstrate flexibility.
Example: create_playlist("Road Trip", {"Song 1", "Song 2"})

Write a function called add_like() that accepts a dictionary, the name of a playlist, and a boolean value indicating whether it is liked (True or False). 
This function should return an updated dictionary.

Example: add_like(dictionary, “Road Trip”, liked=True)'''

def create_playlist(name: str, titles: list):
    album = {name: titles}
    return album
def add_like(album: dict, title: str, like: bool):
    liked = {}
    for x in album:
        print(x)
        if album[x][title]:
            liked[title] = like
    return liked


#album0 = create_playlist("RoadTrip", {"Song 1", "Song 2", "Song 3"})
#album1 = create_playlist("Road", {"Song 1", "Song 2", "Song "})
#album2 = create_playlist("Trip", {"Song 1"})
#album3 = create_playlist("Roip", {"Song 1", "Song 2", "Song 3", "song 4"})





'''2. Book Collection:

Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. 
This function should return a dictionary where the author's name is the key and the value is a list of their books. Demonstrate this function by adding books for different authors.

Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. This function should return an updated dictionary.

Example: delete_book(dictionary, “Mark Twain”)'''

def add_book(author: str, titles: list) -> dict:
    books: dict = {}
    books["author"] = author
    books["books"] = titles
    return books


author: dict = add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])
author2: dict = add_book("J. k. Rowling", ["Harry Potter e la pietra filosofale", "Harry potter e il principe mezzosangue"])
library: dict = {"author1" : author,
                 "author2" : author2}
print(library)

def del_book(library: dict, del_author: str):
    for x, y in library.items():
        if y["author"] == del_author:
            del library[x]
            break

del_book(library, "Mark Twain")

print(library)

'''3. Personal Info:

Write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. 
Make occupation, location, and age optional parameters. Use this function to create profiles for different people, demonstrating how it handles these optional parameters.

Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)'''

def build_profile(name: str, surname: str, occupation: str = None, location: str = None, age: int = None):
    person: dict = {
        "name" : name,
        "surname" : surname,
        "occupation" : occupation,
        "location" : location,
        "age" : age
    }
    return person


print(build_profile("John", "Doe", occupation="Developer", location="USA", age=30))





'''4. Event Organizer:

Write a function called plan_event() that accepts an event name, a list of participants, and an hour. 
The function should return a dictionary that includes the event name and a list of the participants. Call this function with varying numbers of participants to plan different events.

Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)

Write a function called modify_event() that accepts a dictionary, an event name, and new details to modify an already planned event.

Example: modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)'''


def plan_event(name_event: str, list_partecipants: list, time: str):
    planner: dict = {
        "event" : name_event,
        "partecipants" : list_partecipants,
        "hour" : time
    }
    return planner
event1 = plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],"4pm")
event2 = plan_event("writing Workshop", ["Angela", "Bill", "Chiara"],"3pm")
event3 = plan_event("HTML Workshop", ["Anna", "Ben", "Carmelo"],"3pm")
planner = {
    "E1" : event1,
    "E2" : event2,
    "E3" : event3,
}
print(planner)

def modify_event(planner: dict, event_name: str, new_part: list, new_time: str):
    for x in planner.values():
        if x["event"] == event_name:
            x["partecipants"] = new_part
            x["hour"] = new_time
            break

modify_event(planner, "HTML Workshop", ["Alice", "Bob", "Charlie"], "5pm")

print(planner)

'''5. Shopping List:

Write a function called create_shopping_list() that accepts a store name and any number of items as arguments. It should return a dictionary with the store name and a set of items to buy there. Test the function with different stores and item lists.

Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})

Write a function called print_shopping_list() that accepts a dictionary and a store name, then prints each item from that store's shopping list.

Example: print_shopping_list(dictionary, "Grocery Store")'''