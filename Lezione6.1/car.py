#9-9. Battery Upgrade: Use the final version of electric_car.py from this section. 
#Add a method to the Battery class called upgrade_battery(). 
#This method should check the battery size and set the capacity to 65 if it isn’t already. 
#Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. 
#You should see an increase in the car’s range.

class Car:

    def __init__(self, model, autonomy, cap) -> None:
        self.model = model
        self.autonomy = autonomy
        self.battery = Battery(cap)

    def get_range(self) -> float:
        return self.autonomy*self.battery.get_battery()

class Battery:
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
    
    def upgrade_battery(self) -> None:
        self.capacity = 65
    
    def get_battery(self) -> int:
        return self.capacity
