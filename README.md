# CS103-Finals
Submission for CS103 Final Output

PROBLEM 1: Inheritance, Instances, Polymorphism

SchoolBus is a subclass that inherits from the Vehicle class, and the SchoolBus class uses the super() function to call the constructor of the Vehicle class, allowing it to initialize the name and model attributes

school_bus is an instance of the SchoolBus class. When it creates school_bus = SchoolBus("Toyota", "Hiace", 15), it's also creating an object of the SchoolBus class with specific attributes

The display_info method is overridden in the SchoolBus class. If it called school_bus.display_info(), it executes the overridden method in the SchoolBus class, which first calls the display_info method from the Vehicle class and then adds additional information specific to the SchoolBus

-

PROBLEM 2: Abstraction

The Employee class encapsulates the properties and behaviors of an employee. 

The use of alternative constructors (from_name, from_name_and_id, and from_full_info) allows for flexibility in creating Employee objects.

The display_info method provides a way to present the employee's information. Simply formats and prints the information based on the attributes of the instance

-

PROBLEM 3: Encapsulation, Aggregation

The Student class encapsulates the properties of a student (name and grades) and provides methods to calculate the average grade and GPA. The internal state (grades) is not directly accessible from outside the class. Instead, it is manipulated through methods.

The SchoolOne and SchoolTwo classes encapsulate the behavior and data related to each school, including a list of students and methods to add students and display their information.

Both SchoolOne and SchoolTwo classes aggregate Student objects. Each school has a list of students (self.students), which means that a school "has" students. 

The Student objects exist independently of the SchoolOne and SchoolTwo classes, which is a key characteristic of aggregation.

-

PROBLEM 4: Overloading Operator

The Vector class successfully overloads the + operator, allowing you to add two Vector instances together using the + operator.

This makes the code more intuitive and readable, as it allows to use natural mathematical expressions with your custom objects.

-

PROBLEM 5: Composition

The Book class uses composition by including an instance of the Author class, demonstrating how a book "has an author" rather than "is an author"

This design choice promotes better code organization and flexibility, aligning with the principles of composition
