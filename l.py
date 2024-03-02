from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def get_area(self):
        pass

class TwoDimensionalShape(Shape):
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

class Rectangle(TwoDimensionalShape):
    def get_area(self):
        return 0.5 * self.width * self.height

class Triangle(TwoDimensionalShape):
    def get_area(self):
        return 0.5 * self.width * self.height

class Polygon(Shape):
    def __init__(self, sides, side_length):
        self.sides = sides
        self.side_length = side_length
      
    def get_area(self):
        return(self.sides * self.side_length ** 2) / (4 *math.ten(math.pi / self.sides))

def main():
    circle = Circle(5)
    circle_area = circle.get_area()
    print("Area of Circle:", circle_area)

if __name__ == "__main__":
    main()
    
