from abc import ABC, abstractmethod

class Shape(ABC):
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
      
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
      
    def area(self):
        return self.side_length ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
      
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
      
    def get_area(self):
        return 0.5 * self.base * self.height

def main():
    circle = Circle(1)
    square = Square(1)
    rectangle = Rectangle(1, 1)
    triangle = Triangle (1, 1)

    print("Circle's Area: ", circle.area())
    print("Square's Area: ", square.area())
    print("Rectangle's Area: ", rectangle.area())
    print("Triangle's Area: ", triangle.area())

if __name__ = "__main__":
    main()
    
