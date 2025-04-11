""" Determine if School bus is also an instance of the Vehicle class. """

class Vehicle:
    # This is the class representing a generic vehicle.
    
    def __init__(self, name, model):

        self.name = name
        self.model = model

    def display_info(self):

        return f"Vehicle: {self.name}, Model: {self.model}"


class SchoolBus(Vehicle):

    def __init__(self, name, model, capacity):

        super().__init__(name, model)  # Call the constructor of the Vehicle class
        self.capacity = capacity

    def display_info(self):

        vehicle_info = super().display_info()  # Get vehicle info from the parent class
        return f"{vehicle_info}, Capacity: {self.capacity} seats"


# OUTPUT HERE.

if __name__ == "__main__":

    school_bus = SchoolBus("Toyota", "Hiace", 15)

    print(school_bus.display_info())

    if isinstance(school_bus, Vehicle):
        print("The school bus is an instance of the Vehicle class.")
    else:
        print("The school bus is NOT an instance of the Vehicle class.")