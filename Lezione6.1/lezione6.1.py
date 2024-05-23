from ristorante import Restaurant
from ristorante import IceCreamStand

abc: Restaurant = Restaurant("ABC", "Aperitivi")

abc.describe_restaurant()
abc.open_restaurant()
abc.set_number_served(10)
abc.describe_restaurant()
abc.increment_number_served(25)
abc.describe_restaurant()

abc1: IceCreamStand = IceCreamStand("DEF", "Gelato", ["fragola", "limone", "pistacchio", "crema", "mango"])

abc1.describe_restaurant()
abc1.open_restaurant()

abc2: Restaurant = Restaurant("GHI", "Sushi")

abc2.describe_restaurant()
abc2.open_restaurant()

abc3: Restaurant = Restaurant("LMN", "Cinese")

abc3.describe_restaurant()
abc3.open_restaurant()

print("#"*50)
print("#"*50)
print("#"*50)
print("#"*50)

from user import User
from user import Admin

Lorenzo: User = User("Lorenzo", "Colitto", 23, "M", 3933140037)
Luce: Admin = Admin("Luce", "Rossi", 2, "F", 39331543437, ["can delete post", "can add post", "can make comments", "can ban user"])
Ana: User = User("Anna", "Bianchi", 93, "F", 3931234537)

Lorenzo.describe_user()
Lorenzo.greet_user()
Lorenzo.increment_login_attempts()
Lorenzo.increment_login_attempts()
Lorenzo.increment_login_attempts()
Lorenzo.increment_login_attempts()
Lorenzo.increment_login_attempts()
Lorenzo.increment_login_attempts()
Lorenzo.increment_login_attempts()
Lorenzo.describe_user()
Lorenzo.reset_login_attempts()
Lorenzo.describe_user()

Luce.describe_user()
Luce.greet_user()
Luce.priv.show_privileges()
print("")

Ana.describe_user()
Ana.greet_user()


from car import Car

tesla = Car("S", 10, 45)

print(tesla.get_range())

tesla.battery.upgrade_battery()

print(tesla.get_range())