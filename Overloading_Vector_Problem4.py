""" Operator Overloading Create a Vector class that supports addition using the + operator, allowing you to add two vectors. """

class Vector:
    # This is the class representing a mathematical vector in 2D space.
    
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __add__(self, other):

        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented  # You can see return NotImplemented if other is not a Vector

    def __repr__(self):

        return f"Vector({self.x}, {self.y})"

# OUTPUT HERE. WITH RESPECTIVE INSTANCES, VECTOR RESULTS, AND PRINTING THE OUTPUT AFTERWARDS.
if __name__ == "__main__":

    vector1 = Vector(2, 3)
    vector2 = Vector(4, 5)
    

    result_vector = vector1 + vector2
        
    print(f"The result of adding {vector1} and {vector2} is {result_vector}.")