# CS103-Finals
Submission for CS103 Final Output

PROBLEM 1: Inheritance, Instances, Polymorphism
Inheritance allows a class (the child class) to inherit attributes and methods from another class (the parent class). This is demonstrated since:

SchoolBus is a subclass that inherits from the Vehicle class, and the SchoolBus class uses the super() function to call the constructor of the Vehicle class, allowing it to initialize the name and model attributes

An instance is a specific object created from a class. This is demonstrated since:
school_bus is an instance of the SchoolBus class. When I created school_bus = SchoolBus("Toyota", "Hiace", 15), I am creating an object of the SchoolBus class with specific attributes

Polymorphism allows methods to do different things based on the object that it is acting upon. This is demonstrated since:
The display_info method is overridden in the SchoolBus class. I call school_bus.display_info(), it executes the overridden method in the SchoolBus class, which first calls the display_info method from the Vehicle class and then adds additional information specific to the SchoolBus
