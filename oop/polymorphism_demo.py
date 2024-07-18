
class Shape:
    def area(self):
        raise NotImplementedError
    
    def description(self):
        return "This is a shape"


class Rectangle(Shape):
    def __init__(self, length, width):

        self.lenght = length
        self.width = width

    def area(self):
        return self.lenght + self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
        
    def area(self):
        import math
        return math.pi * self.radius ** 2  
