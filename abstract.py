from abc import ABC, abstractmethod
import math

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


rect = Rectangle(5, 10)
circle = Circle(7)

print("Rectangle area:", rect.area())
print("Rectangle perimeter:", rect.perimeter())

print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())
