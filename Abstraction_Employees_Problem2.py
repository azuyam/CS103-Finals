""" Build a class Employee with multiple constructors that can initialize an employee object in different ways. """

class Employee:
    # This is the class representing an employee.
    
    def __init__(self, name, employee_id=None, salary=None):

        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    @classmethod
    def from_name(cls, name):

        return cls(name)

    @classmethod
    def from_name_and_id(cls, name, employee_id):

        return cls(name, employee_id)

    @classmethod
    def from_full_info(cls, name, employee_id, salary):

        return cls(name, employee_id, salary)

    def display_info(self):

        info = f"Name: {self.name}"
        if self.employee_id is not None:
            info += f", ID: {self.employee_id}"
        if self.salary is not None:
            info += f", Salary: ${self.salary:.2f}"
        print(info)


# OUTPUT PRINTING. Comment for each information

if __name__ == "__main__":
    # Create an Employee using the default constructor
    emp1 = Employee("Juan Dela Cruz")
    
    # Create an Employee using the from_name alternative constructor
    emp2 = Employee.from_name("Seth Lowell")
    
    # Create an Employee using the from_name_and_id alternative constructor
    emp3 = Employee.from_name_and_id("Mary Grace", 12345)
    
    # Create an Employee using the from_full_info alternative constructor
    emp4 = Employee.from_full_info("Maria Makiling", 67890, 80000)

    # Display information for all employees
    emp1.display_info()
    emp2.display_info()
    emp3.display_info()
    emp4.display_info()
